import requests
def get_operation(url):
    r = requests.get(url)
    if(r.status_code != 200):
        print(f'{url} request is failed')
        return None
    if('text/html' in r.headers['Content-Type']):
        return 'WebPage-Response'
    else:
        return 'Data-Response'


for var in ['https://www.google.com','https://api.github.com/users/hadley/orgs']:
    print(get_operation(var))
    

    