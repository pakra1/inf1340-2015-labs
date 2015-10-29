#!/usr/bin/env python3

""" Module to test lab3.py """

__author__ = 'Paniz Pakravan'
__email__ = "p.pakravan@mail.utoronto.ca"
__copyright__ = "2015 Paniz Pakravan"
__date__ = "29 October 2015"

from lab3 import days_in_month

MONTHS_WITH_31 = ["January", "March", "May", "July", "August", "October", "December"]
MONTHS_WITH_30 = ["April", "June", "September", "November"]
MONTHS_WITH_28_or_29 = ["February"]


def test_months_with_31():
    """
    Test months with 31 days
    """
    for item in MONTHS_WITH_31:
        assert days_in_month(item) == 31

def test_months_with_less():
    for item in MONTHS_WITH_30 or MONTHS_WITH_28_or_29:
        assert True

    try:
        days_in_month(item) == 30 or 29 or 28
    except ValueError:
        assert True

def lower_days_in_month():
    for item in MONTHS_WITH_31 or MONTHS_WITH_30 or MONTHS_WITH_28_or_29:
        item = item.lower()
        assert lower_days_in_month(item) == 31
        assert lower_days_in_month(item) == 30
        assert lower_days_in_month(item) == "28 or 29"

def days_in_month_exception():
    try:
        item = MONTHS_WITH_28_or_29 or MONTHS_WITH_30 or MONTHS_WITH_31
    except ValueError:
        Print ("Oops")

# Write a test function for the months with 30 days

# Write a test function for the months with 28 or 29 days

# Write a test function for months that are not capitalized properly
# Hint: use the lower() string method

# Write a test function for unexpected input
# Hint: use a try/except block to deal with the exception
# Hint: use data types other than strings as input

