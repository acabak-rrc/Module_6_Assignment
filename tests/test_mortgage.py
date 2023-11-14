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

    good_amount = 5000
    good_rate = MortgageRate.FIXED_1
    good_frequency = MortgageFrequency.WEEKLY
    good_amortization = VALID_AMORTIZATION[1]

    def test__init__invalid_amount(self):
        #Arrange
        bad_amount = -5000 #negative

        #Act
        with self.assertRaises(ValueError) as context:
            temporary_mortgage = Mortgage(bad_amount, self.good_rate, self.good_frequency, self.good_amortization)

        #Assert
        expected_value = "Loan amount must be a positive number."
        self.assertEqual(str(context.exception), expected_value)

    def test__init__invalid_rate(self):
        #Arrange
        bad_rate = "I am not a mortgage rate"

        #Act
        with self.assertRaises(ValueError) as context:
            temporary_mortgage = Mortgage(self.good_amount, bad_rate, self.good_frequency, self.good_amortization)

        #Assert
        expected_value = "Rate provided is invalid."
        self.assertEqual(str(context.exception), expected_value)

    def test__init__invalid_frequency(self):
        #Arrange
        bad_frequency = "I am not a mortgage frequency"

        #Act
        with self.assertRaises(ValueError) as context:
            temporary_mortgage = Mortgage(self.good_amount, self.good_rate, bad_frequency, self.good_amortization)

        #Assert
        expected_value = "Frequency provided is invalid."
        self.assertEqual(str(context.exception), expected_value)

    def test__init__invalid_amortization(self):
        #Arrange
        bad_amortization = "I am not a valid amortization value"

        #Act
        with self.assertRaises(ValueError) as context:
            temporary_mortgage = Mortgage(self.good_amount, self.good_rate, self.good_frequency, bad_amortization)

        #Assert
        expected_value = "Amortization provided is invalid."
        self.assertEqual(str(context.exception), expected_value)

    #ANOTHER TEST HERE LATER FOR TESTING PROPER VALUES SETTING

    def test_mortgage_loan_amount_negative(self):
        #Arrange
        bad_amount = -5000 #negative

        #Act
        temporary_mortgage = Mortgage(self.good_amount, self.good_rate, self.good_frequency, self.good_amortization)
        with self.assertRaises(ValueError) as context:
            temporary_mortgage.loan_amount = bad_amount

        #Assert
        expected_value = "Loan Amount must be a positive number."
        self.assertEqual(str(context.exception), expected_value)

    def test_mortgage_loan_amount_zero(self):
        #Arrange
        bad_amount = 0 #negative

        #Act
        temporary_mortgage = Mortgage(self.good_amount, self.good_rate, self.good_frequency, self.good_amortization)
        with self.assertRaises(ValueError) as context:
            temporary_mortgage.loan_amount = bad_amount

        #Assert
        expected_value = "Loan Amount must be a positive number."
        self.assertEqual(str(context.exception), expected_value)

    def test_mortgage_loan_amount_positive(self):
        #Arrange
        another_good_amount = 12345

        #Act
        temporary_mortgage = Mortgage(self.good_amount, self.good_rate, self.good_frequency, self.good_amortization)
        temporary_mortgage.loan_amount = another_good_amount
        actual = temporary_mortgage.loan_amount

        #Assert
        expected_value = 12345
        self.assertEqual(actual, expected_value)

    def test_mortgage_rate_setter(self):
        #Arrange
        another_good_rate = MortgageRate.VARIABLE_1

        #Act
        temporary_mortgage = Mortgage(self.good_amount, self.good_rate, self.good_frequency, self.good_amortization)
        temporary_mortgage.rate = another_good_rate
        actual = temporary_mortgage.rate

        #Assert
        expected_value = MortgageRate.VARIABLE_1
        self.assertEqual(actual, expected_value)

    def test_mortgage_rate_setter_invalid(self):
        #Arrange
        bad_rate = "I am not a mortgage rate"

        #Act
        temporary_mortgage = Mortgage(self.good_amount, self.good_rate, self.good_frequency, self.good_amortization)
        with self.assertRaises(ValueError) as context:
            temporary_mortgage.rate = bad_rate

        #Assert
        expected_value = "Rate provided is invalid."
        self.assertEqual(str(context.exception), expected_value)

    def test_mortgage_frequency_setter(self):
        #Arrange
        another_good_frequency = MortgageFrequency.MONTHLY

        #Act
        temporary_mortgage = Mortgage(self.good_amount, self.good_rate, self.good_frequency, self.good_amortization)
        temporary_mortgage.frequency = another_good_frequency
        actual = temporary_mortgage.frequency

        #Assert
        expected_value = MortgageFrequency.MONTHLY
        self.assertEqual(actual, expected_value)

    def test_mortgage_frequency_setter_invalid(self):
        #Arrange
        bad_frequency = "I am not a mortgage frequency"

        #Act
        temporary_mortgage = Mortgage(self.good_amount, self.good_rate, self.good_frequency, self.good_amortization)
        with self.assertRaises(ValueError) as context:
            temporary_mortgage.frequency = bad_frequency

        #Assert
        expected_value = "Frequency provided is invalid."
        self.assertEqual(str(context.exception), expected_value)
