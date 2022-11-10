import requests

base_host = "https://api.stackexchange.com/questions"

params = {'site':'stackoverflow.com'}
response_url = base_host
response = requests.get(response_url, params=params)
data = response.json()

print(data)

# for question in data['items']:
#     if 'python' in question['tags']:
#         print(question['title'])


