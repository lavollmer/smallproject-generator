import requests
import os

token = os.environ.get("GITHUB_TOKEN")
headers = {"Authorization": f"token {token}"}

username ='lavollmer'
response = requests.get(f'https://api.github.com/users/{username}', headers=headers)


response = requests.get('https://api.github.com/events')
print(response.status_code)

if response.status_code == 200:
    user_data = response.json()
    print(f"Name: {user_data.get('name')}")

print(response.text)
print(response.json())

