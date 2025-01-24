"""
10. Loan Eligibility Checker
Write a program to determine if a person is eligible for a loan and calculate the interest rate.

Input Variables:
income (float): Annual income.
credit_score (integer): Credit score (300-850).
has_collateral (boolean): Whether the person has collateral (True or False).
loan_amount (float): Requested loan amount.
Eligibility and Interest Rate Rules:
If the credit score is above 750:
    If income is above $50,000, approve the loan with a 5% interest rate.
    Otherwise, approve with a 7% interest rate.
If the credit score is between 600 and 750:
    If the person has collateral, approve with a 10% interest rate.
    If the person does not have collateral, deny the loan.
If the credit score is below 600:
    Deny the loan regardless of other factors.
"""