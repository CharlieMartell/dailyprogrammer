#!/usr/bin/env python
import argparse, itertools

# Setup argument parser for taking in numbers to do stuffs with
parser = argparse.ArgumentParser(
        description="Permutes int to make int higher"
        "than second argument using slots of int.")
parser.add_argument('-f',
    '--first',
    help='first number',
    required=True)
parser.add_argument('-s',
    '--second',
    help='second number',
    required=True)
args = vars(parser.parse_args())

def next_larger(a, b):
    return [x for x in sorted(int(''.join(map(str,list(p))))
            for p in itertools.permutations([int(x)
                for x in a], len(str(a)))) if x >= int(b)][0]

def main():
    print next_larger(args['first'], args['second'])

if __name__ == '__main__':
    main()
