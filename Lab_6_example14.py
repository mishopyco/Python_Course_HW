#  Да се напише програма, която да генерира число на случен принцип и да
# подкани потребителя да познае това число. Да извежда следните стойности too low, too
# high, или exactly right, в случай, че потребителя е познал, или не числото.
import random
x = random.randint(0,100)

while True:
    guess=int(input('enter your guess between 1 and 100:'))
    if guess<x:
        print('your guess is too low. Try again!')
    elif guess > x:
        print('your guess is too high. Try again!')
    else:
        print('exactly right')
        break

    