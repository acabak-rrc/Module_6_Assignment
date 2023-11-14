"""
Description: A class used to test the Mortgage class.
Author: Aidan Cabak
Date: 2023-11-14
Usage: Use the tests encapsulated within this class to test the MortgagePayment class.
"""

from unittest import TestCase
from mortgage.mortgage import Mortgage
from mortgage.pixell_lookup import MortgageRate, MortgageFrequency, VALID_AMORTIZATION

class MortgageTests(TestCase):
    def test__init__invalid_amount(self):
        #Arrange
        bad_amount = -5000 #negative
        good_rate = MortgageRate.FIXED_1
        good_frequency = MortgageFrequency.WEEKLY
        good_amortization = VALID_AMORTIZATION[1]

        #Act
        with self.assertRaises(ValueError) as context:
            temporary_mortgage = Mortgage(bad_amount, good_rate, good_frequency, good_amortization)

        #Assert
        expected_value = "Loan amount must be a positive number."
        self.assertEqual(str(context.exception), expected_value)

    def test__init__invalid_rate(self):
        #Arrange
        good_amount = 5000
        bad_rate = "I am not a mortgage rate"
        good_frequency = MortgageFrequency.WEEKLY
        good_amortization = VALID_AMORTIZATION[1]

        #Act
        with self.assertRaises(ValueError) as context:
            temporary_mortgage = Mortgage(good_amount, bad_rate, good_frequency, good_amortization)

        #Assert
        expected_value = "Rate provided is invalid."
        self.assertEqual(str(context.exception), expected_value)

    def test__init__invalid_frequency(self):
        #Arrange
        good_amount = 5000
        good_rate = MortgageRate.FIXED_1
        bad_frequency = "I am not a mortgage frequency"
        good_amortization = VALID_AMORTIZATION[1]

        #Act
        with self.assertRaises(ValueError) as context:
            temporary_mortgage = Mortgage(good_amount, good_rate, bad_frequency, good_amortization)

        #Assert
        expected_value = "Frequency provided is invalid."
        self.assertEqual(str(context.exception), expected_value)

    def test__init__invalid_amortization(self):
        #Arrange
        good_amount = 5000
        good_rate = MortgageRate.FIXED_1
        good_frequency = MortgageFrequency.WEEKLY
        bad_amortization = "I am not a valid amortization value"

        #Act
        with self.assertRaises(ValueError) as context:
            temporary_mortgage = Mortgage(good_amount, good_rate, good_frequency, bad_amortization)

        #Assert
        expected_value = "Amortization provided is invalid."
        self.assertEqual(str(context.exception), expected_value)

    #ANOTHER TEST HERE LATER FOR TESTING PROPER VALUES SETTING