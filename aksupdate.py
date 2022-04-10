import requests
import re
import datetime

api = 'https://api.github.com/repos/MicrosoftDocs/azure-docs/commits'
weburl= 'https://github.com/MicrosoftDocs/azure-docs/articles/aks'
api2 = 'https://api.github.com/repos/MicrosoftDocs/azure-docs/commits/bc2553acb76d6d969f2bd9cf4ee5470be2a9c529'


#获取当前时间前一天的日期
def get_yesterday_date():
    today = datetime.date.today()
    yesterday = today - datetime.timedelta(days=1)
    yesterday_date = yesterday.strftime('%Y-%m-%d')
    return yesterday_date

path='/articles/aks'
since_date='2022-04-02'

parameter={
    'path': path,
    'since': since_date
}

# r = requests.get(api,params=data)
# commit_api = r.json()[0]['url']
# r2 = requests.get(commit_api)
# print(len(r.json()))
# 创建字典

    
def get_commit_info_for_chosen_repo(repo_api):
    request_parameter = parameter
    commit_info=requests.get(repo_api,params=request_parameter)
    #jso格式显示
    commit_info_json=commit_info.json()
    return commit_info_json

def get_commit_time(commit_api):
    r2 = requests.get(commit_api)
    commit_time = r2.json()['commit']['author']['date']
    return commit_time
# 创建函数，获取commit更新时间并只保留日期
def get_commit_date(commit_time):
    commit_date = re.findall(r'\d{4}-\d{2}-\d{2}', commit_time)
    return commit_date[0]
#测试函数  
# print(get_commit_date(get_commit_time(api2)))











# changefiles = r2.json()['files']

# for file in iter(changefiles):
#     print(file['filename'])
#     print(file['patch'])
# print(r2.json()['files'][0]['patch'])


# api.github.com/repos/:owner/:repo/commits?path=/articles/aks


# https://api.github.com/repos/MicrosoftDocs/azure-docs/commits?path=/articles/aks

# https://api.github.com/repos/MicrosoftDocs/azure-docs/compare/bc2553acb76d6d969f2bd9cf4ee5470be2a9c529..ea36acc295ed8eec360416cd1c12b03445d7590d