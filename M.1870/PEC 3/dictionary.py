#! /usr/bin/env python
"""
Generates all possible passwords for a given name
Uses pattern: name first letter surname first letter and all possible birthdates
Example name: Cristiano Ronaldo would generate passwords like: CR05021985
Birth dates range from 1900 up to today
"""

__author__ = "Aaron Castro"
__author_email__ = "aaron.castro.sanchez@outlook.com"
__copyright__ = "Aaron Castro"
__license__ = "MIT"

import argparse, string
from datetime import date, timedelta

""" Generates all possible passwords from the name """ 
def generate_dictionary(fullname):
    start_date = date(1900, 1, 1)
    end_date = date.today()
    time_frame = end_date - start_date
    for _ in range(time_frame.days):
        print(fullname[0][0] + fullname[1][0] + (start_date + timedelta(days = _)).strftime("%d%m%Y"))

parser = argparse.ArgumentParser()
parser.add_argument("-n", "--name", nargs="+", required = True, help  = "User full name")

if __name__ == "__main__":
    args = parser.parse_args()
    print("Generating all possible passwords for: ", end = "")
    print(" ".join([str(_) for _ in args.name]))
    generate_dictionary(args.name)