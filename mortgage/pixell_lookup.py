"""
Description: Enumerations to keep track of valid mortgage rates 
and payment frequencies. A list to keep track of valid amortization periods.
Author: ACE Department
Edited By: Aidan Cabak
Date: 2023-11-14
Usage: The enumerations and list in this file may be used when working 
with mortgages to ensure only valid rates, frequencies and amortization 
periods are used.
"""


from enum import Enum

VALID_AMORTIZATION = [5, 10, 15, 20, 25, 30] 

class MortgageRate(Enum):
    """
    An enumeration of the different mortage rate options.

    Values:
    - FIXED_5: a fixed-rate mortgage
    - FIXED_3: a fixed-rate mortgage
    - FIXED_1: a fixed-rate mortgage
    - VARIABLE_5: a variable-rate mortgage
    - VARIABLE_3: a variable-rate mortgage
    - VARIABLE_1: a variable-rate mortgage
    """

    FIXED_5 = 0.0500
    FIXED_3 = 0.0579
    FIXED_1 = 0.0589
    VARIABLE_5 = 0.0650
    VARIABLE_3 = 0.0660
    VARIABLE_1 = 0.0679

class MortgageFrequency(Enum):
    """
    An enumeration of different mortgage frequencies.

    Values:
    - MONTHLY: a monthly mortgage
    - BI_WEEKLY: a bi-weekly mortgage
    - WEEKLY: a weekly mortgage
    """

    MONTHLY = 12
    BI_WEEKLY = 26
    WEEKLY = 52