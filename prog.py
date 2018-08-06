#!/usr/bin/python
# https://docs.python.org/2/howto/argparse.html
import argparse
parser = argparse.ArgumentParser()
#parser.add_argument("square", help="echo the string you use here", type=int)
#parser.add_argument("--verbosity", help="increase output verbosity", action="store_true")
#parser.add_argument("--verbosity", help="increase output verbosity")

#parser.add_argument("x", type=int, help="the base")
#parser.add_argument("y", type=int, help="the exponent")
#parser.add_argument("-v", "--verbosity", action="count",
                     #default=0, help="increase output verbosity")

parser.add_argument("square", type=int,
                    help="display a square of a given number")

group = parser.add_mutually_exclusive_group()
group.add_argument("-v", "--verbose", action="store_true")
group.add_argument("-q", "--quiet", action="store_true")

parser.add_argument("x", type=int, help="the base")
parser.add_argument("y", type=int, help="the exponent")
parser.add_argument("-v", "--verbosity", action="count", default=0)

args = parser.parse_args()

answer =  args.square**2

if args.verbosity >= 2:
    print "the square of {} equals {}".format(args.square, answer)
    print "Running '{}'".format(__file__)
elif args.verbosity >= 1:
    print "{}^2 == {}".format(args.square, answer)
else:
    print answer
