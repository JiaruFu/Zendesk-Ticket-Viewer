import unittest 
import api_request as ar
import zendesk_ticket_viewer as ztv
from unittest.mock import patch
from io import StringIO

# The TestCases class contains all the related unit tests.
class TestCases(unittest.TestCase):
    # The helper method for getting all the tickets
    def getAllTicketsTestHelper(self, given_answer, expected_out, parameter):
        with patch('builtins.input', return_value=given_answer), patch('sys.stdout', new=StringIO()) as fake_out:
            ztv.getAllTickets(parameter)
            self.assertEqual(fake_out.getvalue().strip(), expected_out)

    # The helper method for getting a specific method
    def getSpecificTicketTestHelper(self, given_answer, expected_out, parameter):
        with patch('builtins.input', return_value=given_answer), patch('sys.stdout', new=StringIO()) as fake_out:
            ztv.getSpecificTicket(parameter, given_answer)
            self.assertEqual(fake_out.getvalue().strip(), expected_out)

    def authenticate(self):
        credentials = 'jfu57@wisc.edu', 'apJIARU1293403'
        data = ar.makeRequest(credentials = credentials)
        tickets_posts = data['tickets']
        return tickets_posts

    # The method tests the function of getAllTickets if all the tickets typed in exist
    def testGetAllTickets(self):
        tickets_posts = self.authenticate()
        result = ("Id: 1; Subject: Sample ticket: Meet the ticket; Created by 405960585111 on 2020-11-05T23:13:28Z\n"
         " Id: 2; Subject: I need help; Created by 405960585111 on 2020-11-05T23:13:45Z\n"
         " Id: 3; Subject: velit eiusmod reprehenderit officia cupidatat; Created by 405960585111 on 2020-11-06T02:55:45Z\n"
         " Id: 4; Subject: excepteur laborum ex occaecat Lorem; Created by 405960585111 on 2020-11-06T02:55:45Z\n"
         " Id: 5; Subject: ad sunt qui aute ullamco; Created by 405960585111 on 2020-11-06T02:55:45Z")

        self.getAllTicketsTestHelper('1 2 3 4 5', result, tickets_posts)
        self.maxDiff 

    # The method tests the function of getAllTickets if some of the tickets typed in do not exist
    def testGetAllTicketsNotExist(self):
        tickets_posts = self.authenticate()
        result = ("Id: 1; Subject: Sample ticket: Meet the ticket; Created by 405960585111 on 2020-11-05T23:13:28Z\n"
         " Id: 2; Subject: I need help; Created by 405960585111 on 2020-11-05T23:13:45Z\n"
         " Id: 3; Subject: velit eiusmod reprehenderit officia cupidatat; Created by 405960585111 on 2020-11-06T02:55:45Z\n"
         " Id: 4; Subject: excepteur laborum ex occaecat Lorem; Created by 405960585111 on 2020-11-06T02:55:45Z\n"
         " The typed ticket number 1000 is not found.")

        self.getAllTicketsTestHelper('1 2 3 4 1000', result, tickets_posts)
        self.maxDiff 

    # The method tests the function of getSpecificTicket if the ticket exists
    def testGetSpecificExistingTicket(self):
        tickets_posts = self.authenticate()
        result = 'Id: 2; Subject: I need help; Created by 405960585111 on 2020-11-05T23:13:45Z'
        self.getSpecificTicketTestHelper('2', result, tickets_posts)

    # The method tests the function of getSpecificTicket if the ticket does not exist
    def testGetSpecificNonexistingTicket(self):
        tickets_posts = self.authenticate()
        result = ''
        self.getSpecificTicketTestHelper('1000', result, tickets_posts)

    # The method tests the function of getSpecificTicket if the ticket typed in is not a valid number
    def testGetSpecificInvalidTicket(self):
        tickets_posts = self.authenticate()
        result = ''
        self.getSpecificTicketTestHelper('abc', result, tickets_posts)

if __name__ == '__main__':
    unittest.main()