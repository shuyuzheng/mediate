import json
import requests

api_key
api_url_base = "https://api.nytimes.com/svc/movies/v2"


def get_movies(query):
    api_url = '{0}/reviews/search.json?'.format(api_url_base)
    query.update({'api-key': api_key})
    response = requests.get(api_url, params=query)
    if response.status_code == 200:
        movies = json.loads(response.content.decode('utf-8'))["results"]
        return [i["display_title"] for i in movies ]
    else:
        return None

def get_info(moviename):
    api_url = '{0}/reviews/search.json?'.format(api_url_base)
    query = {'query': moviename, 'api-key': api_key}
    response = requests.get(api_url, params=query)
    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))["results"][0]
    else:
        return None
