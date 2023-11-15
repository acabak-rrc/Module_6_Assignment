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
        """
        Initialization function for Mortgage class. Reads from args and sets attribute values.
        """
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
        
    @property
    def loan_amount(self):
        """Getter for loan_amount attribute."""
        return self._loan_amount
    
    @loan_amount.setter
    def loan_amount(self, value):
        """Setter for loan_amount attribute"""
        if value > 0:
            self._loan_amount = value
        else:
            raise ValueError("Loan Amount must be a positive number.")
        
    @property
    def rate(self):
        """Getter for rate attribute."""
        return self._rate
    
    @rate.setter
    def rate(self, value):
        """Setter for loan_amount attribute"""
        if isinstance(value, self.MortgageRate):
            self._rate = value
        else:
            raise ValueError("Rate provided is invalid.")
        
    @property
    def frequency(self):
        """Getter for frequency attribute."""
        return self._frequency
    
    @frequency.setter
    def frequency(self, value):
        """Setter for frequency attribute"""
        if isinstance(value, self.MortgageFrequency):
            self._frequency = value
        else:
            raise ValueError("Frequency provided is invalid.")
        
    @property
    def amortization(self):
        """Getter for amortization attribute."""
        return self._amortization
    
    @amortization.setter
    def amortization(self, value):
        """Setter for amortization attribute"""
        if value in self.VALID_AMORTIZATION:
            self._amortization = value
        else:
            raise ValueError("Amortization provided is invalid.")
        
    def calculate_payment(self) -> float:
        """
        Args:
            N/A

        Returns:
            float: Calculated mortgage payment value

        Raises:
            N/A
        """
        monthly_rate = self.rate.value / 12 
        number_of_payments = (self.amortization * self.frequency.value)
        calculated_payment = self.loan_amount * ((monthly_rate * (1 + monthly_rate) ** number_of_payments)/(((1 + monthly_rate) ** number_of_payments) - 1))
        return calculated_payment
    
    def __str__(self):
        """
        String representation of Mortgage object.
        """
        displayed_rate = self.rate.value * 100       
        return (f"Mortgage amount: ${float(self.loan_amount):,.2f}\n"
                f"Rate: {float(displayed_rate)}%\n"
                f"Amortization: {int(self.amortization)}\n"
                f"Frequency: {self.frequency.name.capitalize()} -- Calculated Payment: ${float(self.calculate_payment()):,.2f}\n")
            
        



