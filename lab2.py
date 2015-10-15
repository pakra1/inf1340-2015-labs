#!/usr/bin/env python3

""" Graded Lab #2 for Inf1340, Fall 2015 """

__author__ = 'Paniz Pakravan'
__email__ = "p.pakravan@mail.utoronto.ca"
__copyright__ = "2015 Paniz Pakravan"
__date__ = "October 15, 2015"


"""
Instructions: Add a function to get input from the user and use that
function in name_that_shape()

The function should prompt the user for input until a legal value is
entered. A legal value is any integer.

"""

def get_user_input():
    valid_input = False
    while valid_input is not True:
        user_input = raw_input("Number of sides?")
        try:
            user_input = int(user_input)
            valid_input = True
        except ValueError:
            print ("Please enter a number.")
    return user_input

def name_that_shape():
    """
    For a given number of sides in a regular polygon, returns the shape name

    Inputs | Expected Outputs
    -------------------------
      < 3  | Error
      3    | triangle
      4    | quadrilateral
      5    | pentagon
      6    | hexagon
      7    | heptagon
      8    | octagon
      9    | nonagon
      10   | decagon
      > 10 | Error

    Errors: ValueError when input is a string or float

    """

    sides = get_user_input()

    if sides == 3:
        print("triangle")
    elif sides == 4:
        print("quadrilateral")
    elif sides == 5:
        print("pentagon")
    elif sides == 6:
        print("hexagon")
    elif sides == 7:
        print("heptagon")
    elif sides == 8:
        print("octagon")
    elif sides == 9:
        print("nonagon")
    elif sides == 10:
        print("decagon")
    else:
        print("Error")

#name_that_shape()