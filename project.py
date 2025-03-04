import requests
import os

token = os.environ.get("GITHUB_TOKEN")
headers = {"Authorization": f"token {token}"}

username ='lavollmer'
response = requests.get(f'https://api.github.com/users/{username}', headers=headers)

def main():
    response = requests.get('https://api.github.com/events')
    print(response.status_code)
    print(response.text)
    print(response.json())

__name__="__main__":
    main()