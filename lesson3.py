import sys
import random

while True :
    your_input = input("\n\nplease enter a number:\n1 : stone\n2 : paper\n3 : scissors\n\n")

    if your_input.lower() == 'quit' :
        break
    if your_input.isdigit() :
        your_choice = int(your_input)
        if( your_choice <0 or your_choice > 3) :
            print("you must enter 1 or 2 or 3")
            sys.exit()
        computer_value = random.choice("123")
        computer_choice = int(computer_value)

        print("your choice is " + your_input + "\ncomputer choice is " + computer_value)
        
        if your_choice == 1 and computer_choice ==3 :
            print("you win!")
        elif your_choice == 2 and computer_choice == 3 :
            print("you win!")
        elif your_choice == 3 and computer_choice == 2 :
            print("you win!")
        elif your_choice == computer_choice :
            print("tie game")
        else :
            print("computer win!")

    else :
        print("you must enter a valid number.")




