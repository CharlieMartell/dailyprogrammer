#!/usr/bin/env python
import argparse

# Setup argument parser 
parser = argparse.ArgumentParser(description="Prints garland chain "
    "for a word if it exists")
parser.add_argument('-w',
    '--word',
    help='Word to be garland',
    required=True)
parser.add_argument('-i',
    '--iterations',
    help='# of times to garland word',
    required=True,
    type=int)
args = vars(parser.parse_args())

def garland(word, iterations):
    """
    Creates a garland of given word if it is possible
    """
    g_w = lambda x : next((i for i in reversed(range(len(x)))
        if x[:i] == x[-i:]), 0)
    return word + word[g_w(word):] * iterations

def main():
    print garland(args['word'].lower(), args['iterations'])
    
if __name__ == '__main__':
    main()
