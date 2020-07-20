import requests
import os
import json
import time


headers = {"Authorization": "token 08182fe95bce80deae3492ae91da4c9cda34fa47"}

def run_query(query): # A function to use post to make the API call.,
    request = requests.post('https://api.github.com/graphql', json={'query': query}, headers=headers)
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception("Query failed to run by returning code of {}. {}".format(request.status_code, query))
        
def get_repositories(query):
    result = run_query(query)
    return result
    

page_entry_size = 100
last_page_cursor = None
repositories = []
languages = ['java', 'javascript', 'c', 'c++']
total_repos_searched = -1
search_text = "stars:>2 forks:>2 pushed:>=2017-01-01"
query = """
{{
  search(type:REPOSITORY, query: "{0}", first: {1}, after: {2}) {{
    repositoryCount
    repos: nodes {{
        ... on Repository {{
          url
          name
        }}
    }}

    pageInfo {{
      endCursor
      hasNextPage
    }}    
  }}
}}
""".replace("\n","")

#initialize the working directory
current_dir = os.getcwd()

#seach for all the languages
for language in languages:
    if os.path.exists(current_dir + "/" + language + "/repos.json"):
        continue
    
    repositories = []
    result = {}

    #make dir of the language name
    if not os.path.exists(current_dir + "/" + language ):
        os.mkdir(current_dir + "/" + language)

    last_page_cursor = None
    search_text_with_language = search_text + " language:{0}".format(language)

    while True:
        result = get_repositories(query.format(search_text_with_language, page_entry_size, last_page_cursor if last_page_cursor is not None else 'null'))
        repositories += result['data']['search']['repos']    

        page_cursor = result['data']['search']['pageInfo']['endCursor']
        if page_cursor is not None:
            last_page_cursor = "\"{0}\"".format(page_cursor)
        else:
            break
    
    #save the respository list file: repos.csv into it
    with open(current_dir + "/" + language + '/repos.json', 'w') as outfile:
        json.dump(repositories, outfile)


task_counter = 0

#clone all repostory for each language
for language in languages:
    with open(current_dir + "/" + language + '/repos.json') as json_file:
        repositories = json.load(json_file)
      
    for repository in repositories:
        if os.path.exists(current_dir + "/" + language + "/{0}.csv".format(repository['name'])):
            continue

        os.popen("cd {0} && git clone --no-checkout {1} && cd {2} && git log --pretty=format:\"%ae|%aN|%aD|\" --shortstat --no-merges >> ../{3}.csv && cd .. && rm -rf {4}/"
        .format(language, repository['url'], repository['name'], repository['name'], repository['name']))

        task_counter += 1

        #if task_counter >= 100:
         #   time.sleep(600) #sleep for twenty seconds
         #   task_counter = 0
               
        #create a cloned file for this respository
        # open(current_dir + "/" + language + "/{0}.done".format(repository['name'].replace("-","_")), 'w') 

#convert all repository into git logs csv files
#delete all cloned repos








