#!/usr/bin/env python3

""" Graded Lab #1 for Inf1340, Fall 2015 """

__author__ = 'Paniz Pakravan'
__email__ = "p.pakravan@mail.utoronto.ca"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"


def vowel_or_consonant():
    """
    Exercise: Vowel or Consonant
    Reads a letter of the alphabet from the user. (You can assume that it's
    lowercase.) If the user enters a, e, i, o or u then your program should
    display "vowel". If the user enters y then your program should display
    "sometimes a vowel, sometimes a consonant". Otherwise your program should
    display a message indicating that the letter is a "consonant".
    """

    respond = raw_input("what is your letter?")
    if len(respond) == 1:
        if respond == "a":
            print("vowel")
        elif respond == "e":
            print("vowel")
        elif respond == "i":
            print("vowel")
        elif respond == "o":
            print("vowel")
        elif respond == "u":
            print ("vowel")
        elif respond == "y":
            print("sometimes a vowel, sometimes a consonant")
        else:
            print("consonant")
    else:
        print("error")


