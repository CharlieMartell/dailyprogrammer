#!/usr/bin/env python
import argparse

# Setup argument parser 
parser = argparse.ArgumentParser(description="Balances input words\n"
    "The formula to calculate the weight of the word is "
    "to look at the letter position in the English alphabet"
    "(so A=1, B=2, C=3 ... Z=26) as the letter weight, then "
    "multiply that by the distance from the balance point, "
    "so the first letter away is multiplied by 1, the second away by 2, etc.")
parser.add_argument('-w',
    '--word',
    help='Word to be balanced',
    required=True)
args = vars(parser.parse_args())

def balance_word(word):
    """
    Attempts to balance a word around some letter in it.
    """
    calc = lambda w,i,l : (
        sum((ord(w[j]) - 64) * (i - j) for j in range(i)) if l else
        sum((ord(w[j]) - 64) * (j - i) for j in range(i + 1, len(w))))
    for i in range(1, len(word) - 1):
        if calc(word, i, True) == calc(word, i, False):
            return "{} {} {} - {}".format(
                word[:i], word[i], word[i + 1:], calc(word, i, True))
        return word + " does not balance"

def main():
    print balance_word(args['word'].upper())
    
if __name__ == '__main__':
    main()
