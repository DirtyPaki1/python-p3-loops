#!/usr/bin/env python3

def happy_new_year():
    for i in range(10, 0, -1):  # Countdown from 10 to 1
        print(i)
    print("Happy New Year!")  # Print "Happy New Year!" after the countdown


def square_integers(numbers):
    result = []
    for number in numbers:
        result.append(number ** 2)
    return result



def fizzbuzz():
    '''prints 1 to 100 with fizz 3s, buzz 5s, fizzbuzz 3and5s'''
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

