#! /usr/bin/env python
"""
Looks for hash collisions on a given string using digest generated by Blake2 algorithm

-Length param allows to cut the first -length- characters of the hash to speed up matches
"""

__author__ = "Aaron Castro"
__author_email__ = "aaron.castro.sanchez@outlook.com"
__copyright__ = "Aaron Castro"
__license__ = "MIT"

import argparse, random, string, time, itertools
from hashlib import blake2b

class BreakOuter (Exception): pass

""" Creates all possible strings for a given length using the printable ASCII characters """
def all_strings(length):
    output = []
    set = []

    """ Prepare the character set """
    for _ in range(32, 126):
        set.append(chr(_))
    """ Create all possible combinations """
    for _ in itertools.product(set, repeat = length):
        output.append("".join(map(str, _)))

    return(output)

""" Recursive all_strings version """
def all_strings_r(prefix, length):
    string = ""

    for _ in range(32, 126):
        string = prefix + chr(_)
        print(string)
        if length != 1:
            all_strings_r(string, length - 1)

""" Hashes a string given returning the cutted in length hash """
def hash_input(input_s, length):
    hash = blake2b()
    hash.update(input_s.encode("utf-8"))
    return hash.hexdigest()[0:length]

""" Iterates over all the possible strings until it finds a collision """
def find_collision(prefix, input_s, length, length_c):
    start = time.time()

    input_h = hash_input(input_s, length)
    for _ in range(32, 126):
        string = prefix + chr(_)
        hashed_test = hash_input(string, length)
        if input_h == hashed_test and input_s != string:
            print(string + " has a hash of " + hashed_test + " and matches " + input_h + "... We found a collision!!!", end = "\r")
            print("\nElapsed time: " + str(time.time() - start))
            raise BreakOuter
        else:
            print(string + " has a hash of " + hashed_test + " and should match " + input_h, end = "\r")
            if length_c >= 1:
                find_collision(string, input_s, length, length_c - 1)

    return(time.time() - start)

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input", required = True, help  = "Input string to be hashed")
parser.add_argument("-l", "--length", required = True, help = "Length of characters in hash to be matched")

if __name__ == "__main__":
    args = parser.parse_args()
    try:
        find_collision("", args.input, int(args.length), int(args.length))
    except BreakOuter:
        pass