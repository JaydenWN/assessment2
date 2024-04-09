import subprocess
import re
import platform

def main():
    # imports nicegui module
    # https://nicegui.io/
    # Used to create a html GUI for the task.
    from nicegui import ui

    # Gets the body tag of the html document and sets the background
    # to a dark grey color using tailwind.
    # https://tailwindcss.com/docs/customizing-colors
    # https://nicegui.io/documentation/section_styling_appearance#query_selector
    ui.query('body').classes('bg-stone-900')

    # Setting a global variable of how many tickets can be 'purchased'
    tickets_remaining = 200

    # Used to check if 50th ticket has been purchased.
    fiftyTrig = False

    # Defining functions that will be used when user interacts with the app

    # Function that will update the ui.label for remaining ticket display
    # This is ran when a user presses the buy button. Called in handleBuy function.
    # https://nicegui.io/documentation/label#label
    def updateTicketsRemaining():
        label.set_text(f'There are {tickets_remaining} tickets for Roberts lecture available for purchase.')

    # This function takes in the event handler provided by nicegui, then extracts the value
    # variable and sets it to a global scoped variable called username.
    # username is used to for notifications.
    # https://www.w3schools.com/python/python_variables_global.asp
    def setName(event):
        global username
        username = event.value

    # This function takes in the event handler provided by nicegui, then extracts the value
    # variable, converts the float returned into an int, then declares a global variable ticketQty.
    # ticketQty is the amount of tickets the user is 'purchasing'
    # https://www.w3schools.com/python/ref_func_int.asp
    def setTicketQty(event):
        global ticketQty
        ticketQty = int(event.value)

    # This function handles the logic for when a user 'purchases' tickets.
    def handleBuy():
        # Allows use of the fiftyTrig and tickets_remaining global scoped variable within the function
        global fiftyTrig
        global tickets_remaining

        # Checks to see if username or ticketQty isn't declared as a global variable.
        # If one of the two aren't declared, then a nicegui notification will pop up on the users screen.
        # https://nicegui.io/documentation/notify#notification
        if 'username' not in globals() or 'ticketQty' not in globals():
            ui.notify('You have either not inputted a username or a quantity of tickets to purchase. Try again.', type='warning')
        
        # If the users desired ticket purchase qty is greater than the amount of remaining tickets,
        # then a nicegui notification will alert the user.
        # Also ensures that the user is buying at least one ticket.
        if ticketQty > tickets_remaining and ticketQty >= 1:
            ui.notify(f'Sorry there are only {tickets_remaining} tickets left.', type='negative')

        # Otherwise if the users desired ticket purchase qty is less than the remaining amount
        # then the tickets_remaining will be reduced by the ticketQty amount, then assigned back to
        # tickets_remaining.
        else: 
            tickets_remaining = tickets_remaining - ticketQty
            ui.notify(f'{username}, you successfully Purchased {ticketQty} Tickets', type='positive')
            # Checks if the user has purchased the 50th ticket by checking if the remaining ticket count
            # is less than 50 and the fiftyTrig is set to false.
            # If the user purchases the 50th ticket, it will display a notification using nicegui.
            if tickets_remaining < 50 and fiftyTrig == False:
                ui.notify(f'Congratulations {username}, you successfully Purchased the 50th Ticket', type='positive')
                # Sets fiftyTrig to true to ensure the notification isn't displayed every time a 'purchase' is made
                # when the ticket_remaining count is less than 50.
                fiftyTrig = True
            # Update or 'refresh' the label that displays ticket count.
            updateTicketsRemaining()

    # +----------------------------------------------------Webpage / UI set up----------------------------------------------------+
        
    # Creates an image tag in html, styling with tailwind css to display a label for Movie4Us
    # The image is deployed on an amazon s3 bucket with public access.
    # https://nicegui.io/documentation/image#image
    # https://nicegui.io/documentation/label#label
    with ui.image('https://auditradar.s3.ap-southeast-2.amazonaws.com/python+cinema.jpg').style('max-height: 300px; max-width: 850px; margin: 0px auto'):
        ui.label('Welcome to Movie4Us').classes('absolute-center text-center')


    # Creates a div element, styled with a red background using tailwind, then displays a label informing how many tickets remain for purchasing.
    # https://nicegui.io/documentation/element#generic_element
    with ui.element('div').classes('p-3 bg-red-100 ml-auto mr-auto'):
        label = ui.label(f'There are {tickets_remaining} tickets for Roberts lecture available for purchase.')

    # Creates a 'card' component with tailwind styling.
    # https://nicegui.io/documentation/card#card
    with ui.card().classes('p-10 ml-auto mr-auto'):

        # Creates an input for username. Using on_change will trigger the setname function each time a user types something new.
        # https://nicegui.io/documentation/input 
        ui.input(label='Your Name', on_change=setName).classes('p-10')
    
        # Creates a 2 column css grid, with padding styling from tailwind.
        # https://nicegui.io/documentation/grid#grid_element
        with ui.grid(columns=2).classes('p-10'):

            # Number input for the amount of tickets a user wishes to purchase.
            # Will trigger the setTicketQty function each time the value is changed.
            # https://nicegui.io/documentation/number#clearable
            ui.number(label='Ticket Qty', min=1, max=tickets_remaining, format='%d', on_change=setTicketQty)

            # Creates a buy now button.
            # Triggers the handleBuy function once a user clicks on it.
            # https://nicegui.io/documentation/button#button
            ui.button(text='Buy Now', on_click=handleBuy)


    # Executes the nicegui application on localhost port 8080, Then launches web browser
    ui.run()


## = = = = =                    Requirements Tester / Downloader                  = = = = = = ##
requirementList = ['nicegui']

# Collect all installed libs
installedLibs = subprocess.run(['pip3', 'list'], capture_output=True, text=True)
installedLibsStr = str(installedLibs.stdout)
libListListed = re.findall(r'[a-z_-]+', installedLibsStr)
currentOS = platform.system()

# If all the dependencies are already installed, then run the program.
# Otherwise install them.
if all(item in libListListed for item in requirementList):
    print('All dependencies installed, attempting to run application')
    main()
else:
    # Check for internet connection,
    # Chose to use 'ping' because its used on windows, linux, and mac os
    # Instead of standard outputting to terminal its redirected into a pipe for further manipulation,
    # Instead of outputting to terminal for instance
    print(f'Attempting to download dependencies for this project: \n{requirementList}')
    
    checkConnection = ''

    # if the OS is mac, then ping will continue until user terminates it.
    if currentOS == 'Darwin':
        checkConnection = subprocess.run(['ping', 'google.com', '-c', '1'], stdout=subprocess.PIPE)
    else:
        checkConnection = subprocess.run(['ping', 'google.com'], stdout=subprocess.PIPE)

    # If subprocess returns with an error code (1) then alert user, otherwise install dependencies
    if checkConnection.returncode == 0:
        # macos requires --user
        if currentOS == 'Darwin':
            checkForPipInstall = subprocess.run(['pip3', 'install', '--upgrade', 'pip', '--user'], capture_output=True, text=True)
            print(checkForPipInstall.stdout)
        else: 
            checkForPipInstall = subprocess.run(['pip3', 'install', '--upgrade', 'pip'], capture_output=True, text=True)
            print(checkForPipInstall.stdout)
        # Loop over requirementList and install each dependency using pip.
        for dependency in requirementList:
            # macos requires --user
            if currentOS =='Darwin':
                installDependencies = subprocess.run(['pip3', 'install', dependency, '--user'], capture_output=True, text=True)
                print(installDependencies.stdout)
            else: 
                installDependencies = subprocess.run(['pip3', 'install', dependency], capture_output=True, text=True)
                print(installDependencies.stdout)
        # Finally execute the file.
        main()
    else:
        print('You are not connected to the internet, please connect and try again!')