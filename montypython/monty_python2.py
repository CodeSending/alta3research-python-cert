#!/usr/bin/env python3
round = 0# integer round initiated to 0
answer = " "

while round < 3 and answer.lower() != "brian":
    round += 1     # increase the round counter
    answer = input('Finish the movie title, "Monty Python\'s The Life of ______": ')
    if answer.lower() == 'brian': # logic to check if user gave correct answer
        print('Correct!')
    elif answer.lower() == 'shrubbery' : #because why not
        print('We are the knights of Ni!')
        break
    elif round == 3:    # logic to ensure round has not yet reached 3
        print('Sorry, the answer was Brian.')
    else:                 # if answer was wrong, and round is not yet equal to 3
        print('Sorry. Try again!')

