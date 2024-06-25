#!/usr/bin/env python3
"""Conditionals - Life of Brian guessing game using While Loop"""

round = 0 # initialize counter 
while True: # Set up an infinite loop condition
    round += 1 # increase the counter after each loop
    print('Finish the movie title, "Monty Python\'s The Life of ______"')
    answer = input("Your guess--> ") # Get an answer from the user
    if answer == "Brian": # Check if answer is correct
        print("You're Correct!")
        break # Break from loop if anwser is correct
    elif round == 3: # Check to ensure guess count hasn't reached 3
        print("Sorry, you've run out of guesses")
        break # Break from loop when guess limit is reached
    else:
        print("Sorry, Try Again!")                        
