import requests
API_KEY = "AIzaSyBzqIWp6jM7u-Zo3VjR819jHKnwJc9qecA"
SEARCH_ENGINE_ID = "76f2b5a93605e4ddc"
search_query = 'cat'
url = 'https://www.googleapis.com/customsearch/v1?key=' + API_KEY + '&cx=' + SEARCH_ENGINE_ID + '&q=' + search_query
params = {
    'searchType': 'image'
}
response = requests.get(url, params=params)
results = response.json()
for item in results:
    print(item['link'])
