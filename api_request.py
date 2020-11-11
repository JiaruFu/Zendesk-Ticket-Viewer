import requests

# This menthod connects to the Zendesk API and get the data
def makeRequest(credentials = None):
    if credentials == None:
        return

    session = requests.Session()
    session.auth = credentials
    zendesk = 'https://jiarufu.zendesk.com'

    url = zendesk + '/api/v2/tickets.json'
    response = session.get(url)
    if response.status_code != 200:
        print('Error with status code {}'.format(response.status_code))
        print('The API is unavailable.')
        exit()
    data = response.json()   
    return data
