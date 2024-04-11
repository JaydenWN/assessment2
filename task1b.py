# Developers: 
# Jayden Naylon
# https://github.com/JaydenWN
# A00150649
#
# Payal -
# A00135758
# -------------------------------

# imports the tkinter module used for GUI
# This documentation was followed during the development process:
# https://tkdocs.com/tutorial/widgets.html
from tkinter import *
from tkinter import ttk

# Fucntions for math equations
def add(x,y):
   result = x + y
   return result

def subtract(x,y):
   result = x - y
   return result

def divide(x,y):
   result = x / y
   return result

def multiply(x,y):
   result = x * y
   return result

# Global variable to determine what step the user is on
onSecondStep = False

# Performs the calculations, takes in the number displayed on the tkk.Entry
# and the operation the user clicked.
def calculate(displayNumber, selectedOp):
   
   # Setting global scoped variables
   global firstVal
   global selectedOperator
   global secondVal
   global onSecondStep

   # collects the operator the user pressed
   pressedOperator = selectedOp

   # if the user presses clear, the screen is cleared,
   # and the function exists using the return statement
   if pressedOperator == 'clear':
      return screenDisplay.set('')
      
   # if the user is on the first input, converts the string variable
   # from displayNumber into a float, clears the screen and lets the application know
   # the user will now be on the second step.
   if onSecondStep == False:
      firstVal = float(displayNumber)
      onSecondStep = True
      selectedOperator = pressedOperator
      screenDisplay.set('')

   # if the user is on the second step, meaning they have supplied a number and an operator,
   # we take their second input converted into a float from displayNumber, and if the user
   # presses '=' then the mathematical function will run and return a number.
   elif onSecondStep == True:
      onSecondStep = False
      secondVal = float(displayNumber)
      if pressedOperator == '=' and selectedOperator == '+':
         screenDisplay.set(add(firstVal,secondVal))
      elif pressedOperator == '=' and selectedOperator == '-':
         screenDisplay.set(subtract(firstVal,secondVal))
      elif pressedOperator == '=' and selectedOperator == '/':
         screenDisplay.set(divide(firstVal,secondVal))
      elif pressedOperator == '=' and selectedOperator == 'x':
         screenDisplay.set(multiply(firstVal,secondVal))
      

# Init tkinter
root = Tk()

# Edits the window title
root.title('Task1b | Calculator')
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.config(padx=10, pady=10)


# ttk frame to hold the number buttons
numPad = ttk.Frame(root, relief='sunken', padding=10)
numPad.grid(column=0, row=1, sticky=(S, E))


# Global variables used to determine what row/col a number should be on.
currentRow = 0
currentCol = 0

# Using a for loop with range to generate buttons from 9 - 0.
for number in range (9,-1,-1):
    ttk.Button(numPad, text=number, command=lambda num = number: screenDisplay.set(screenDisplay.get()+str(num))).grid(column=currentCol, row=currentRow)
    currentCol+=1
    if currentCol == 3:
       currentCol = 0
    if number == 7 or number == 4:
       currentRow+=1
    elif number == 1:
       currentRow+=1
       currentCol = 1


# Create the 'screen' of the calculator
# global variable that is connected to ttk.entry textvariable.
screenDisplay= StringVar()
screen = ttk.Entry(root, state='readonly', textvariable=screenDisplay, width=25)
screen.grid(column=0, row=0)


# Creates the operator buttons
operators = ['clear','+', '-', 'x', '/', '=',]
operatorFrame = ttk.Frame(root, relief='sunken', padding=5)
operatorFrame.grid(column=1, row=1)

# for each of the operators we have declared in our operators list, we generate a button.
# Using the enumerate function we can access both the index and values of the operator list.
# https://treyhunner.com/2016/04/how-to-loop-with-indexes-in-python/
# In our command we wish to pass the operator selected, so we can use a lambda function.
# https://www.w3schools.com/python/python_lambda.asp
# If we were to use a normal function, tkinter will run that function straight away.
# https://tcl.tk/man/tcl8.6/TkCmd/ttk_button.htm
for index, operator in enumerate(operators):
   ttk.Button(operatorFrame, text=operator, command=lambda op=operator: calculate(screenDisplay.get(), op)).grid(row=index)


def showTimesTable(num):
   # Creates a new pop up window.
   tableWindow = Toplevel(root)
   tableWindow.config(padx=40, pady=40,)

   # We must access our value from tkinters DoubleVar by using .get()
   number = num.get()

   tableFrame = ttk.Frame(tableWindow, relief='raised', padding=10)
   tableFrame.grid(column=0,row=0)
   for i in range(1,11):
      ttk.Label(tableFrame, text=f'{number} x {i} = {number * i}').grid(column=0,row=i)
      


# Create times table list
timesTableFrame = ttk.Frame(root)
timesTableFrame.grid(column=0, row=3)

ttk.Label(timesTableFrame, text='Input a number to view its times table.').grid(column=0,row=0)

userInput = DoubleVar()
timesTableInput = ttk.Entry(timesTableFrame, textvariable=userInput, )
timesTableInput.grid(column=0, row=1)

timesTableButton = ttk.Button(timesTableFrame, text='Calculate', command=lambda num = userInput: showTimesTable(num))
timesTableButton.grid(column=0, row=3)






# Init tkinter program cycle
root.mainloop()