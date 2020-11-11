# Zendesk Ticket Viewer

#### This is a CLI application

## Usage: 
#### 1. Open the terminal and go to the directory where all the files are included
#### 2. Type in ```python main_program.py``` to run the ticket viewer program
#### 3. Type in ```python tests.py``` to run all the unit tests
When "okay" shows on the command window, it means all the tests are passed.


## The execution flow: 
#### 1. When running the program and typing in 'menu', you can see the main page:

![alt text](https://github.com/JiaruFu/Zendesk-Ticket-Viewer/blob/main/images/main_page.png?raw=true?width=100)

#### 2. You can choose either 1, 2, 3, or quit based on preferences

#### 3. If you press in 1 (no space), if there are more than 25 tickets, the program would ask you to specify 5 tickets you want to view.
Type in 5 numbers with space(s) between them or you can type 'return' to return to the main page.
#### 4. Below is an example when "1 5 8 2 10" are typed in

![alt text](https://github.com/JiaruFu/Zendesk-Ticket-Viewer/blob/main/images/tickets_info.png?raw=true?width=100)

#### 5. If you press in 2 (no space), the program will ask you to specify 1 ticket you want to view.
Enter one ticket number or you can type 'return' to return to the main page.
#### 6. Below is an example when "89" is typed in

![alt text](https://github.com/JiaruFu/Zendesk-Ticket-Viewer/blob/main/images/specific_info.png?raw=true?width=100)

#### 7. If you press in 3 (no space), the program will print out the total number of tickets as below:

![alt text](https://github.com/JiaruFu/Zendesk-Ticket-Viewer/blob/main/images/total_number.png?raw=true?width=200)

#### 8. You can exit the program by typing in 'quit'


## Class Descriptions: 

#### 1. main_program.py runs and executes the entire program.
#### 2. api_request.py gets the information via Zendesk API
#### 3. zendesk_ticket_viewer.py contains all the functionalities for viewing a group of tickets or an individual ticket.
#### 4. tests.py contains potential test methods by unit testing
