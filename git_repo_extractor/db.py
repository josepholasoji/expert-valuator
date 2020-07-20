
import mysql.connector
from mysql.connector import Error
import os
import re
import json
import codecs
from datetime import datetime
import requests

headers = {"Authorization": "token 08182fe95bce80deae3492ae91da4c9cda34fa47"}

def run_query(query): # A function to use post to make the API call.,
    request = requests.post('https://api.github.com/graphql', json={'query': query}, headers=headers)
    if request.status_code == 200:
        # print(request.json())
        return request.json()
    else:
        print("Query failed to run by returning code of {}. {}".format(request.status_code, query))
        return None
        
def get_developer(query):
    result = run_query(query)
    return result

def load_dir_to_db(dir_apth, languages):
    connection = None
    committer_cache = {}

    try:
        connection = mysql.connector.connect(host='localhost',
                                            database='github_repos',
                                            user='root',
                                            password='')
        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
    except Error as e:
        print("Error while connecting to MySQL", e)

    #clone all repostory for each language
    for language in languages:
        with open(dir_apth + "/" + language + '/repos.json') as json_file:
            repositories = json.load(json_file)
        
        for repository in repositories:
            file_path = dir_apth + "/" + language + "/{0}.csv".format(repository['name'])
            procesed_file_path = dir_apth + "/" + language + "/{0}.processed.csv".format(repository['name'])

            #insert into db...
            cursor = connection.cursor()

            #insert into repo                                        
            val = (repository['name'].strip(), language, 'not-needed', repository['url'].strip())
            cursor.execute("""
                            INSERT IGNORE INTO `repositories`
                            SET `name` = %s,
                            `language` = %s,
                            `owner` = %s,
                            `url` = %s
                            """, val)
            connection.commit()
            repo_index = cursor.lastrowid
            if(repo_index == 0):
                val = (repository["url"])
                cursor.execute("select `index` from repositories where `url` like '%s' limit 1", val)
                repo_index = cursor.fetchone()[0]

            if os.path.exists(file_path):
                with codecs.open(file_path, encoding='utf-8') as file:
                    for line in file:
                        if not line: continue
                        entries = line.split("|")
                        email = entries[0]
                        auto_name = entries[1]

                        #e.g: Sat, 30 Nov 2019 14:55:15 +0800
                        try:
                            date = datetime.strptime(entries[2], "%a, %d %b %Y %H:%M:%S %z")
                        except ValueError as e:
                            continue

                        files_changed = 0
                        code_insertions = 0
                        code_deletion = 0

                        for cd in entries[3].split(","):
                            cdentry = cd.split(":")                            
                            if cdentry[0] == 'F':
                                files_changed = int(cdentry[1].replace('\n',''))
                            if cdentry[0] == 'I':
                                code_insertions = int(cdentry[1].replace('\n',''))
                            if cdentry[0] == 'D':
                                code_deletion = int(cdentry[1].replace('\n',''))


                        #insert into committer
                        committer_id = 0
                        if committer_cache.__contains__(email) is False:
                            cursor = connection.cursor()
                            val = (email.strip(), auto_name.strip())
                            cursor.execute("INSERT IGNORE INTO `developers` set `email`=%s, `name`=%s", val)
                            connection.commit()
                            committer_id = cursor.lastrowid

                            if(committer_id == 0):
                                cursor.execute("select `id` from developers where `email` = '" + email + "' limit 1")
                                committer_id = cursor.fetchone()[0]
                                committer_cache[email] = committer_id

                            committer_cache[email] = committer_id
                        else:
                             committer_id = committer_cache[email]

                        #insert into commits
                        cursor = connection.cursor()
                        val = (date.isoformat(), committer_id, repo_index, files_changed, code_insertions, code_deletion)
                        cursor.execute("select `id` from commits where `date`=%s and `committer`=%s and `repository`=%s limit 1",(date.isoformat(), committer_id, repo_index))
                        if cursor.fetchone() is None:
                            cursor.execute("INSERT INTO commits (date, committer, repository, files_changed, insertions, deletions) VALUES (%s, %s, %s, %s, %s, %s)", val)
                            connection.commit()

                #rename the procesed file so it never be processed again
                os.rename(file_path, procesed_file_path)                              
    
    if (connection.is_connected()):
        cursor.close()
    connection.close()
    print("MySQL connection is closed")


#initialize the working directory
# languages = ['java', 'javascript']
# current_dir = os.getcwd()
# load_dir_to_db(current_dir, languages)

def update_developer_details():
    connection = None
    committer_cache = {}

    query = """
    {{
        search(query: "{0}", type: USER, first: 1) {{
            edges {{
            node {{
                ... on User {{
                login
                bio
                email
                name
                location
                createdAt
                issueComments {{
                    totalCount
                }}
                issues {{
                    totalCount
                }}
                contributionsCollection {{
                    commitContributionsByRepository {{
                    contributions {{
                        totalCount
                    }}
                    repository {{
                        name
                        forkCount
                        primaryLanguage {{
                        name
                        id
                        }}
                        stargazers {{
                        totalCount
                        }}
                        id
                        watchers {{
                        totalCount
                        }}
                    }}
                    }}
                    totalCommitContributions
                    endedAt
                    hasActivityInThePast
                    hasAnyContributions
                    hasAnyRestrictedContributions
                    isSingleDay
                }}
                followers {{
                    totalCount
                }}
                isCampusExpert
                isBountyHunter
                isDeveloperProgramMember
                isHireable
                isSiteAdmin
                isViewer
                id
                projects {{
                    totalCount
                }}
                }}
            }}
            }}
        }}
    }}
    """.replace("\n","")    

    try:
        connection = mysql.connector.connect(host='localhost',
                                            database='github_repos',
                                            user='root',
                                            password='')

        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)

    except Error as e:
        print("Error while connecting to MySQL", e)

    #insert into db...
    cursor = connection.cursor()
    cursor.execute("select name, email from github_repos.developers where email not in (select `email` from github_repos.developers_metainfo) and metainfo_done=0")
    entries = cursor.fetchall()
    for entry in entries:
        try:
            print("getting data for {0}".format(entry[0]))
            result = get_developer(query.format(entry[0].replace("\"", "\\\"")))
            if result is not None:

                if "error" in result: 
                    cursor = connection.cursor()
                    cursor.execute("update github_repos.developers set `metainfo_done`=3 where email='{0}'".format(entry[1]))
                    connection.commit() 
                    continue

                if len(result) == 0 or not result["data"]['search']['edges'] or 'data' not in result: 
                    cursor = connection.cursor()
                    cursor.execute("update github_repos.developers set `metainfo_done`=2 where email='{0}'".format(entry[1]))
                    connection.commit()                     
                    continue

                data = result['data']['search']['edges'][0]['node']
            
                if not data: 
                    cursor = connection.cursor()
                    cursor.execute("")
                    connection.commit()                     
                    continue


                if data['name'] == None or data['name'] == '':
                    data['name'] = entry[0]
                
                data['email'] = entry[1]
                val = ( data["login"], 
                        data["bio"], 
                        data["email"], 
                        data["name"], 
                        data["location"], 
                        data["createdAt"], 
                        data["issueComments"]["totalCount"],
                        data["issues"]["totalCount"], 
                        data["followers"]["totalCount"],
                        data["isCampusExpert"], 
                        data["isBountyHunter"],
                        data["isDeveloperProgramMember"], 
                        data["isHireable"], 
                        data["id"],
                        data["isSiteAdmin"], 
                        data["isViewer"], 
                        data["projects"]["totalCount"], 
                        data["contributionsCollection"]["totalCommitContributions"], 
                        data["contributionsCollection"]["endedAt"], 
                        data["contributionsCollection"]["hasActivityInThePast"],
                        data["contributionsCollection"]["hasAnyContributions"], 
                        data["contributionsCollection"]["hasAnyRestrictedContributions"], 
                        data["contributionsCollection"]["isSingleDay"])
            
                cursor = connection.cursor()
                cursor.execute("""
                    INSERT IGNORE INTO `developers_metainfo` set `login`=%s,
                                                                `bio`=%s,
                                                                `email`=%s,
                                                                `name`=%s,
                                                                `location`=%s,
                                                                `createdAt`=%s,
                                                                `issueCommentsCount`=%s,
                                                                `issuesCount`=%s,
                                                                `followersCount`=%s,
                                                                `isCampusExpert`=%s,
                                                                `isBountyHunter`=%s,
                                                                `isDeveloperProgramMember`=%s,
                                                                `isHireable`=%s,
                                                                `id`=%s,
                                                                `isSiteAdmin`=%s,
                                                                `isViewer`=%s,
                                                                `projectsCount`=%s,
                                                                `totalCommitContributions`=%s,
                                                                `endedAt`=%s,
                                                                `hasActivityInThePast`=%s,
                                                                `hasAnyContributions`=%s,
                                                                `hasAnyRestrictedContributions`=%s,
                                                                `isSingleDay`=%s        

                    """, val)
                connection.commit()     

                cursor = connection.cursor()
                cursor.execute("update github_repos.developers set `metainfo_done`=1 where email='{0}'".format(entry[1]))
                connection.commit()                    

        except Error as e:
            cursor = connection.cursor()
            cursor.execute("update github_repos.developers set `metainfo_done`=4 where email='{0}'".format(entry[1]))
            connection.commit()      
            print("And error occured...", e)          
    
    if (connection.is_connected()):
        cursor.close()
    connection.close()
    print("MySQL connection is closed")


#initialize the working directory
# languages = ['java', 'javascript']
# current_dir = os.getcwd()
update_developer_details()