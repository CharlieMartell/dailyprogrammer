#!/usr/bin/env python
import argparse
from string import punctuation as punc

# Setup argument parser for taking in String to mangle 
parser = argparse.ArgumentParser(description="Mangles string as such\n"
    "Input: This challenge doesn't seem so hard.\n"
    "Output: Hist aceeghlln denos't eems os adhr.")
parser.add_argument('-s',
    '--sentence',
    help='Sentence to mangle',
    required=True)
args = vars(parser.parse_args())

def mangle_sentence(sentence):
    """
    Mangles sentence
    """
    def mangle_word(word):
        sep = lambda x : [(i, c) for i, c in enumerate(x)]
        caps = [i for i, c in sep(word) if c.isupper()]
        puncs = [(i, c) for i, c in sep(word) if c in list(",.'-")]
        new_word = ''.join(sorted(''.join([c.upper()
            if i in caps else c for i,c in enumerate(word.lower())
            if c not in punc])))
        insert = lambda x,y,z : x[:y] + z + x[y:]
        for i,c in puncs: new_word = insert(new_word, i, c)
        return new_word
    return " ".join(mangle_word(word) for word in sentence.split())

def main():
    print mangle_sentence(args['sentence'])
    
if __name__ == '__main__':
    main()
