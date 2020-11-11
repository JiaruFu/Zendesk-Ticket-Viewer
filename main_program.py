import zendesk_ticket_viewer as ztv
import api_request as ar

# The main program runs and executes the entire program. 
def program(credentials):
    data = ar.makeRequest(credentials = credentials)
    ztv.homePage(data)

if __name__ == "__main__":
    credentials = 'jfu57@wisc.edu', 'apJIARU1293403'
    program(credentials)
