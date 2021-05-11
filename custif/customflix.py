#!/usr/bin/env python3

message = 'The movie is about to begin, we recommend '

moviechoice = int(input("What movie would you like to see? (Choose a number from 1-4)"))

# if input value was higher or equal to 25
if moviechoice == 1:
    message = message + 'Harry Potter and the Python of Stuart'
elif moviechoice == 2:
    message = message + 'Hobbit & Lord of the Rings'
elif moviechoice == 3:
    message = message + 'Chronicles of Narnia'
elif moviechoice == 4:
    message = message + 'Indiana Jones'
else:
    message = message + "...actually the movie has been cancelled, sorry"
print(message)

