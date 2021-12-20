"""
File: hailstone.py
Name:
-----------------------
This program should implement a console program that simulates
the execution of the Hailstone sequence, defined by Douglas
Hofstadter. Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""


def main():
    """
    1. judge whether n is equal to 1
    2. If n is odd, multiply n by 3 and add 1
       If n is even, divide n by 2
    3. count steps(while)
    """
    print('This program computes Hailstone sequences.')
    number = int(input('Enter a number: '))
    i = 0
    while number != 1:
        if number % 2 == 0:
            number = number // 2
            i += 1
            print(str(number) + ' is even, so I take half: ' + str(number))
        else:
            number = (3 * number) + 1
            i += 1
            print(str(number) + ' is odd, so I take 3n+1: ' + str(number))
    print('It took ' + str(i) + ' steps to reach 1.')
    '''
    It took 111 steps for 27 to reach 1.
    '''




###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
    main()
