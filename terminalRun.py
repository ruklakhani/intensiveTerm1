import time #Imports a module to add a pause
import sys
import random

#Figuring out how users might respond
answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
answer_D = ["D", "d"]
answer_E = ["E", "e"]
answer_F = ["F", "f"]
yes = ["Y", "y", "yes"]
no = ["N", "n", "no"]

required = ("\nUse A, B, C, D, E, or F\n") #Cutting down on duplication

#broken into sections, starting with "intro"
def intro():
    print ("Hello! How are you today?:")
    print ("""  
    A. Great
    B. Good
    C. Ok
    D. Bad
    E. Awful""")
    choice = input(">>> ") #Here is your first choice.
    if choice in answer_A:
        option_positive()
    elif choice in answer_B:
        option_positive()
    elif choice in answer_C:
        option_neutral()
    elif choice in answer_D:
        option_negative()
    elif choice in answer_E:
        option_negative()
    else:
        print (required)
        intro()

def option_positive(): 
    print ("\nI'm glad today is going well!! What are you expecting from today's session?:")
    time.sleep(1)
    print ("""  
    A. Practice Gratitude
    B. Capture the Moment
    C. Set Goals""")
    choice = input(">>> ")
    if choice in answer_A:
        option_gratitude()
    elif choice in answer_B:
        option_capture()
    elif choice in answer_C:
        option_goals()
    else:
        print (required)
        option_positive()

def option_neutral():
    print ("\nI hope today starts to get better! What are you expecting from today's session?:")
    time.sleep(1)
    print ("""  
    A. Practice Gratitude
    B. Capture the Moment
    C. Set Goals""")
    choice = input(">>> ")
    if choice in answer_A:
        option_gratitude()
    elif choice in answer_B:
        option_capture()
    elif choice in answer_C:
        option_goals()
    else:
        print (required)
        option_neutral()

def option_negative():
    print ("\nI'm sorry things aren't going so hot :^( What do you need from today's session?:")
    time.sleep(1)
    print (""" 
    A. Practice Gratitude
    B. Capture the Moment
    C. Set Goals""")
    choice = input(">>> ")
    if choice in answer_A:
        option_gratitude()
    elif choice in answer_B:
        option_capture()
    elif choice in answer_C:
        option_goals()
    else:
        print (required)
        option_negative()

def option_gratitude():
    print ("\nExpress Gratitude!")
    time.sleep(1)
    gratitude = input("Write about anything important happening at this present moment: ")
    print ("You entered:" + gratitude)    

def option_capture():
    print ("\nCapturing the Moment!")
    time.sleep(1)
    capture = input("Write about anything important happening at this present moment: ")
    print ("You entered:" + capture)

def option_goals():
    print ("\nWriting Goals!")
    time.sleep(1)
    goals = input("Write some of your goals for the future: ")
    print ("You entered:" + goals)


intro()