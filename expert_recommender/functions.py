import requests



headers = {"Authorization": "token 18cb512915f8542aa62070c4b3e981d7c132264b"}

def run_query(query): # A function to use post to make the API call.,
    request = requests.post('https://api.github.com/graphql', json={'query': query}, headers=headers)
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception("Query failed to run by returning code of {}. {}".format(request.status_code, query))
        
