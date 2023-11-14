"""
Description: A class meant to manage Mortgage options.
Author: Aidan Cabak
Date: 2023-11-14
Usage: Create an instance of the Mortgage class to manage mortgage records and 
calculate payments.
"""

class Mortgage:
    """
    This class manages mortgage data from Pixell River Financial.

    Attributes:
    _loan_amount (float): Dollar value of loan.
    _rate (MortgageRate): Interest rate of mortgage.
    _frequency (MortgageFrequency): Frequency of mortgage.
    _amortization (int): Amortization value of loan.
    """

    from mortgage.pixell_lookup import MortgageRate, MortgageFrequency, VALID_AMORTIZATION

    def __init__(self, loan_amount: float, rate: MortgageRate, frequency: MortgageFrequency, amortization: int):

        if loan_amount > 0:
            self._loan_amount = loan_amount
        else:
            raise ValueError("Loan amount must be a positive number.")
        
        if isinstance(rate, self.MortgageRate):
            self._rate = rate
        else:
            raise ValueError("Rate provided is invalid.")
        
        if isinstance(frequency, self.MortgageFrequency):
            self._frequency = frequency
        else:
            raise ValueError("Frequency provided is invalid.")
        
        if amortization in self.VALID_AMORTIZATION:
            self._amortization = amortization
        else:
            raise ValueError("Amortization provided is invalid.")

