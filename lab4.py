#!/usr/bin/env python3

""" Graded Lab #4 for Inf1340, Fall 2015

    This program computes federal and provincial sales tax.
    Assume that the provincial sales tax is 5 percent and
    the federal sales tax is 2.5 percent. It displays the
    amount of the purchase, the provincial sales tax, the
    federal sales tax, the total tax, and the total of the
    sale.
"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"

# Rewrite this code to use global constants, local variables and functions
# Output the text to a file instead of printing it

PROVINCIAL_TAX = 0.05
FEDERAL_TAX = 0.025
TOTAL_TAX = 0.075
TOTAL_SALE = 1.075

def bill_of_sale(purchase):

    # print ("Amount of purchase: {0:.2f}".format(purchase))
    # print ("Provincial tax: {0:.2f}".format(purchase * .05))
    # print ("Federal tax: {0:.2f}".format(purchase * .025))
    # print ("Total tax: {0:.2f}".format(purchase * .075))
    # print ("Total sale: {0:.2f}".format(purchase * 1.075))

    file_name = "sales.txt"

    with open(file_name, "w") as output_file:
        output_file.write ("Amount of purchase: {0:.2f}\n".format(purchase))
        output_file.write ("Provincial tax: {0:.2f}\n".format(purchase * PROVINCIAL_TAX))
        output_file.write ("Federal tax: {0:.2f}\n".format(purchase * FEDERAL_TAX))
        output_file.write ("Total tax: {0:.2f}\n".format(purchase * TOTAL_TAX))
        output_file.write ("Total sale: {0:.2f}\n".format(purchase * TOTAL_SALE))

bill_of_sale(200)