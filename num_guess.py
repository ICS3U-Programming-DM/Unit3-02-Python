# Created by Dylan Melo
# Created on December 2021
# This program gets the user to guess a number
# between 0 and 9 and tells them if it's correct.
import constants

def main():
    
    # input
    user_number = float(input("Guess a number between 0 and 9: "))
    print("")
    
    # Check number
    if user_number >= 10:
        print("Number must be between 0 and 9 silly")
        
    elif user_number <= -1:
        print("Number must be between 0 and 9 silly")
        
    # Process and output
    elif user_number == constants.CORRECT_GUESS:
        print ("You've guess correctly!")
    
    else:
        print ("You've guessed incorrectly!") 
    
    
if __name__ == "__main__":
    main()
    