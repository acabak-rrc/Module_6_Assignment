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
        bad_amortization = 9999

        #Act
        with self.assertRaises(ValueError) as context:
            temporary_mortgage = Mortgage(self.good_amount, self.good_rate, self.good_frequency, bad_amortization)

        #Assert
        expected_value = "Amortization provided is invalid."
        self.assertEqual(str(context.exception), expected_value)

    def test__init__valid_args(self):
        #Arrange
        #good values already arrranged in class scope

        #Act
        temporary_mortgage = Mortgage(self.good_amount, self.good_rate, self.good_frequency, self.good_amortization)
        actual_amount = temporary_mortgage.loan_amount
        actual_rate = temporary_mortgage.rate
        actual_frequency = temporary_mortgage.frequency
        actual_amortization = temporary_mortgage.amortization

        #Assert     
        expected_amount = self.good_amount
        expected_rate = self.good_rate
        expected_frequency = self.good_frequency
        expected_amortization = self.good_amortization

        self.assertEqual(actual_amount, expected_amount)
        self.assertEqual(actual_rate, expected_rate)
        self.assertEqual(actual_frequency, expected_frequency)
        self.assertEqual(actual_amortization, expected_amortization)

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

    def test_mortgage_amortization_setter(self):
        #Arrange
        another_good_amortization = VALID_AMORTIZATION[4]

        #Act
        temporary_mortgage = Mortgage(self.good_amount, self.good_rate, self.good_frequency, self.good_amortization)
        temporary_mortgage.amortization = another_good_amortization
        actual = temporary_mortgage.amortization

        #Assert
        expected_value = VALID_AMORTIZATION[4]
        self.assertEqual(actual, expected_value)

    def test_mortgage_amortization_setter_invalid(self):
        #Arrange
        bad_amortization = "I am not a mortgage amortization"

        #Act
        temporary_mortgage = Mortgage(self.good_amount, self.good_rate, self.good_frequency, self.good_amortization)
        with self.assertRaises(ValueError) as context:
            temporary_mortgage.amortization = bad_amortization

        #Assert
        expected_value = "Amortization provided is invalid."
        self.assertEqual(str(context.exception), expected_value)

    def mortgage_calculate_payment_scenario_1(self):
        #Arrange
        test_amount = 4723.24
        test_rate = MortgageRate.FIXED_3
        test_frequency = MortgageFrequency.MONTHLY
        test_amortization = VALID_AMORTIZATION[5]

        #Act
        temporary_mortgage = Mortgage(test_amount, test_rate, test_frequency, test_amortization)
        actual = Mortgage.calculate_payment()

        #Assert
        expected = 27.68
        self.assertAlmostEquals(expected, actual, 2)
    
    def mortgage_calculate_payment_scenario_2(self):
        #Arrange
        test_amount = 81858.23
        test_rate = MortgageRate.VARIABLE_1
        test_frequency = MortgageFrequency.WEEKLY
        test_amortization = VALID_AMORTIZATION[2]

        #Act
        temporary_mortgage = Mortgage(test_amount, test_rate, test_frequency, test_amortization)
        actual = Mortgage.calculate_payment()


        #Assert
        expected = 468.93
        self.assertAlmostEquals(expected, actual, 2)

    def mortgage_calculate_payment_scenario_3(self):
        #Arrange
        test_amount = 7264
        test_rate = MortgageRate.FIXED_5
        test_frequency = MortgageFrequency.BI_WEEKLY
        test_amortization = VALID_AMORTIZATION[3]

        #Act
        temporary_mortgage = Mortgage(test_amount, test_rate, test_frequency, test_amortization)
        actual = Mortgage.calculate_payment()

        #Assert
        expected = 34.20
        self.assertAlmostEquals(expected, actual, 2)

    def mortgage_calculate_payment_scenario_4(self):
        #Arrange
        test_amount = 142.12
        test_rate = MortgageRate.VARIABLE_5
        test_frequency = MortgageFrequency.MONTHLY
        test_amortization = VALID_AMORTIZATION[1]

        #Act
        temporary_mortgage = Mortgage(test_amount, test_rate, test_frequency, test_amortization)
        actual = Mortgage.calculate_payment()

        #Assert
        expected = 1.61
        self.assertAlmostEquals(expected, actual, 2)

    def test_mortgage__str__monthly(self):
        #Arrange
        test_amount = 142.12
        test_rate = MortgageRate.VARIABLE_5
        test_frequency = MortgageFrequency.MONTHLY
        test_amortization = VALID_AMORTIZATION[1]

        #Act
        temporary_mortgage = Mortgage(test_amount, test_rate, test_frequency, test_amortization)
        actual = str(temporary_mortgage)

        #Assert
        expected = (f"Mortgage amount: $142.12\n"
                    f"Rate: 6.5%\n"
                    f"Amortization: 10\n"
                    f"Frequency: Monthly -- Calculated Payment: $1.61\n")
        self.assertEqual(expected, actual)

    def test_mortgage__str__biweekly(self):
        #Arrange
        test_amount = 142.12
        test_rate = MortgageRate.VARIABLE_5
        test_frequency = MortgageFrequency.WEEKLY
        test_amortization = VALID_AMORTIZATION[1]

        #Act
        temporary_mortgage = Mortgage(test_amount, test_rate, test_frequency, test_amortization)
        actual = str(temporary_mortgage)

        #Assert
        expected = (f"Mortgage amount: $142.12\n"
                    f"Rate: 6.5%\n"
                    f"Amortization: 10\n"
                    f"Frequency: Weekly -- Calculated Payment: $0.82\n")
        self.assertEqual(expected, actual)

    def test_mortgage__str__weekly(self):
        #Arrange
        test_amount = 142.12
        test_rate = MortgageRate.VARIABLE_5
        test_frequency = MortgageFrequency.BI_WEEKLY
        test_amortization = VALID_AMORTIZATION[1]

        #Act
        temporary_mortgage = Mortgage(test_amount, test_rate, test_frequency, test_amortization)
        actual = str(temporary_mortgage)

        #Assert
        expected = (f"Mortgage amount: $142.12\n"
                    f"Rate: 6.5%\n"
                    f"Amortization: 10\n"
                    f"Frequency: Bi_weekly -- Calculated Payment: $1.02\n")
        self.assertEqual(expected, actual)
        
    def test_mortgage__repr__value(self):
        #Arrange
        test_amount = 142.12
        test_rate = MortgageRate.VARIABLE_5
        test_frequency = MortgageFrequency.BI_WEEKLY
        test_amortization = VALID_AMORTIZATION[1]

        #Act
        temporary_mortgage = Mortgage(test_amount, test_rate, test_frequency, test_amortization)
        actual = repr(temporary_mortgage)

        #Assert
        expected = "[142.12, 0.065, 10, 26]"
        self.assertEqual(expected, actual)



    
