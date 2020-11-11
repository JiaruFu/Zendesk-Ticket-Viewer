import argparse
import textwrap

# This method shows the homepage for the CLI and provides all the options 
# users can choose
def homePage(data = None):
    tickets_posts = data['tickets']
    if tickets_posts is None:
        print(" Error. The API is unavailable.")
        return

    print(" Welcome to the Zendesk Ticket Viewer Application\n")

    if len(tickets_posts) == 0:
        print(" There is no ticket created yet. Please create a ticket to start.")
        return

    while True:
        ip = input(" Type 'menu' to view options or 'quit' to exit... \n ")
        if ip == 'menu':
            option = showMenu()
            if option == '1':
                # Option 1 returns back 5 specified tickets
                getAllTickets(tickets_posts = tickets_posts)
            elif option == '2':
                # Option 2 returns back 1 specified ticket
                while True:
                    print(" Enter ticket number between 1 and " + str(len(tickets_posts)) +
                    " or 'return' to return to the main page.")
                    number = input(" Your input: ")

                    if number == 'return':
                        break

                    found = False
                    if number.isnumeric():      
                        found = getSpecificTicket(tickets_posts = tickets_posts, number = number)  
                        print() 
                        if found:
                            break
                        else:
                            print(" The typed ticket number is not found. Please type in a valid ticket number.\n")
                            continue 
                    else:
                        print(" Please type in a valid ticket number.\n")
                        continue                        
            elif option == '3':
                # Option 3 returns back the total number of tickets
                showStatistics(data)
            elif option == 'quit':
                quit()
        elif ip == 'quit':
            quit()
        else:
            print(" Please type in a valid option.\n")
            continue

# This method shows the main menu options
def showMenu():
    print("\n Select view options: ")
    print(" * press 1 to view all tickets.")
    print(" * press 2 to view a ticket")
    print(" * press 3 to view the statistics")
    print(" * Type 'quit' to exit")
    while True:
        option = input ( " Your option: ")
        if option == '1' or option == '2' or option == '3' or option == 'quit':
            return option
        else:
            print(" Please type in a valid option.\n")
            continue

# This method prints out all the tickets information
# If there are more than 25 tickets, ask users to specify the 5 tickets they want to see.
def getAllTickets(tickets_posts = None):
    length = len(tickets_posts)
    if length > 25:
        while True:
            specify = input (" Specify 5 tickets you want to view: [# # # # #] between 1 and " + str(len(tickets_posts)) +
                    " or type 'return' to return to the main page \n")
            if specify == 'return':
                return
            numbers = specify.split()
            if len(numbers) != 5:
                print(" Please only type in 5 numbers")
                continue
            for num in numbers:
                if num.isnumeric():      
                    found = getSpecificTicket(tickets_posts, num)
                    if found is False:
                        print((" The typed ticket number {} is not found.").format(num))
                else:
                    print(" " + num + " is not a valid number.")
            print()
            break
    else:
        for post in tickets_posts:
            msg = " Id: {}; Subject: {}; Created by {} on {}".format(
            post['id'], post['subject'], post['submitter_id'], post['created_at'])
            print(msg)

# This method prints out the information for a specific ticket
def getSpecificTicket(tickets_posts = None, number = None):
    found = False
    for post in tickets_posts:
        if number == str(post['id']):
            msg = " Id: {}; Subject: {}; Created by {} on {}".format(
            post['id'], post['subject'], post['submitter_id'], post['created_at'])
            print(msg)
            found = True
            break  
    return found

# This method shows the statistics for the ticket system
def showStatistics(data = None):
    # the total number of tickets ...
    print("\n Total number of tickets: " + str(data['count']) + "\n")

# This method quits the program
def quit():
    print(" Thank you for using the Zendesk Ticket Views!\n")
    exit()
