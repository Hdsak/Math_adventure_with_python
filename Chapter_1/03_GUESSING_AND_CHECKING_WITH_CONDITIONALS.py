# Exercise 1
def factors(num):
    return [i for i in range(1, num+1) if num % i == 0]


def gcf(a, b):
    while b:
        a, b = b, a % b
    return a


# Exercise 2

from turtle import *
from random import randint



def wander():
    while True:
        fd(3)
        if xcor() >= 200 or xcor() <= - 200 or ycor()<= - 200 or ycor() >= 200:
            lt(randint(90,180))


# Exercise 3
def average(a,b):
    return (a + b)/2


def squareRoot(num,low,high):
    '''Finds the square root of num by
    playing the Number Guessing Game
    strategy by guessing over the
    range from "low" to "high"'''
    for i in range(20):
        guess = average(low,high)
        if guess**2 == num:
            print(guess)
        elif guess**2 > num: #"Guess lower."
          high = guess
        else: #"Guess higher."
            low = guess
    print(guess)

squareRoot(60,7,8)