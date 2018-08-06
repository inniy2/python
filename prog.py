#!/usr/bin/python
# https://docs.python.org/2/howto/argparse.html
import argparse
parser = argparse.ArgumentParser()
#parser.add_argument("square", help="echo the string you use here", type=int)
#parser.add_argument("--verbosity", help="increase output verbosity", action="store_true")
parser.add_argument("--verbosity", help="increase output verbosity")
parser.add_argument("-v", "--verbose", help="increase output verbosity", action="store_true")
parser.add_argument("square", type=int,
                    help="display a square of a given number")

args = parser.parse_args()
answer =  args.square**2


if args.verbose:
    print "the square of {} equals {}".format(args.square, answer)
else:
    print answer

