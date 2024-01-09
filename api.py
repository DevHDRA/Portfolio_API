import httpx
import os
import base64
import json

USER = os.environ.get('GITHUB_USER')
TOKEN = os.environ.get('GITHUB_TOKEN')

def apiHandler(req):
    params = req.get("queryStringParameters", {})
    repo = None
    res = ''
    
    if params is not None:
        repo = params.get("repo")
    
    if repo is None:
        res = getAllRepos()
    else:
        res = getSingleRepo(repo)
        
    return res

    
def getAllRepos():
    response = ''
    body = []
    headers = {
        "accept": "application/vnd.github.v3+json",
        "Authorization": f"Bearer {TOKEN}"
    }
    url = f'https://api.github.com/users/{USER}/repos'
    
    try:
        response = httpx.get(url, headers=headers)
    except Exception as error:
        raise Exception(error)
        
    if response.status_code == 200:
        data = json.loads(response.content)
        for repoInfo in data:
            body.append({
                'name': repoInfo['name'],
                'html_url': repoInfo['html_url'],
                'description': repoInfo['description'],
                'language': repoInfo['language'],
                'created_at': repoInfo['created_at'][0:10],
                'updated_at': repoInfo['updated_at'][0:10],
            })
        return {
            'statusCode': 200,
            'body': body
        }
    else:
        print(f"Error: {response.status_code}, {response}")
        return {
            'statusCode': response.status_code,
            'body': {}
        }



def getSingleRepo(repo):
    readme = getReadMe(repo)
    language = getLanguages(repo)
    if readme['success'] == True and language['success'] == True:
        return {
            'statusCode': 200,
            'body': {
                'readme': readme['body'].decode("utf-8"),
                'languages': language['body']
            }
        }
    else:
        return {
            'statusCode': 400,
            'body': {}
        }


def getReadMe(repo):
    print(f"getting readme from {repo}")
    headers = {
        "accept": "application/vnd.github.v3+json",
        "Authorization": f"Bearer {TOKEN}"
    }
    url = f'https://api.github.com/repos/devHDRA/{repo}/readme'
    response = httpx.get(url, headers=headers)
    
    if response.status_code == 200:
        data = json.loads(response.content)
        decoded_content = base64.b64decode(data["content"])
        return {
            'success': True,
            'body': decoded_content
        }
    else:
        print(f"Error: {response.status_code}, {response}")
        return {
            'success': False,
            'body': {}
        }
        

def getLanguages(repo):
    print(f"getting languages from {repo}")
    headers = {
        "accept": "application/vnd.github.v3+json",
        "Authorization": f"Bearer {TOKEN}"
    }
    url = f'https://api.github.com/repos/{USER}/{repo}/languages'
    response = httpx.get(url, headers=headers)
    
    if response.status_code == 200:
        data = json.loads(response.content)
        return {
            'success': True,
            'body': data
        }
    else:
        print(f"Error: {response.status_code}, {response}")
        return {
            'success': False,
            'body': {}
        }
