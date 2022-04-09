import requests
import regex

api = 'https://api.github.com/repos/MicrosoftDocs/azure-docs/commits'
weburl= 'https://github.com/MicrosoftDocs/azure-docs/articles/aks'
api2 = 'https://api.github.com/repos/MicrosoftDocs/azure-docs/commits/bc2553acb76d6d969f2bd9cf4ee5470be2a9c529'


path='/articles/aks'
since_date='2022-04-02'

data={
    'path': path,
    'since': since_date
}

r = requests.get(api,params=data)
commit_api = r.json()[0]['url']
r2 = requests.get(commit_api)
print(len(r.json()))













# changefiles = r2.json()['files']

# for file in iter(changefiles):
#     print(file['filename'])
#     print(file['patch'])
# print(r2.json()['files'][0]['patch'])


# api.github.com/repos/:owner/:repo/commits?path=/articles/aks


# https://api.github.com/repos/MicrosoftDocs/azure-docs/commits?path=/articles/aks

# https://api.github.com/repos/MicrosoftDocs/azure-docs/compare/bc2553acb76d6d969f2bd9cf4ee5470be2a9c529..ea36acc295ed8eec360416cd1c12b03445d7590d