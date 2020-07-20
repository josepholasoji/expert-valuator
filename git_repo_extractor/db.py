
import mysql.connector
from mysql.connector import Error
import os
import re
import json
import codecs
from datetime import datetime


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
languages = ['java', 'javascript']
current_dir = os.getcwd()
load_dir_to_db(current_dir, languages)
                

