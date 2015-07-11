#!/usr/bin/env python
import argparse

# Setup argument parser for taking in number
parser = argparse.ArgumentParser(description="Converts nearly"
    " any number into a palindromic number.")
parser.add_argument('-n',
    '--number',
    help='Number to convert to palindrome',
    required=True,
    type=int)
parser.add_argument('-i',
    '--iterations',
    help='Max number of iterations to run',
    required=False,
    default=100,
    type=int)
args = vars(parser.parse_args())

def make_palindrome(number):
    """
    Creates palidromes from number in arguments
    """
    num, i = number, 0
    pal = lambda x : x == int(str(x)[::-1])
    new = lambda x : x + int(str(num)[::-1])
    while not pal(num) and not i > args['iterations']:
        (num, i) = (new(num), i+1)
    return '{}, gets palindromic after {} steps : {}'.format(number,i,num)

def main():
    print make_palindrome(args['number'])
    
if __name__ == '__main__':
    main()
