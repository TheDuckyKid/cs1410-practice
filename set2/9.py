"""
9. Hotel Room Pricing
Write a program to calculate the price of a hotel room based on multiple factors.

Input Variables:
nights (integer): Number of nights staying.
is_weekend (boolean): Whether the stay includes weekends (True or False).
room_type (string): "standard", "deluxe", or "suite".
has_membership (boolean): Whether the person has a membership (True or False).
Pricing Rules:
    Base prices:
        Standard: $100/night.
        eluxe: $150/night.
        Suite: $250/night.
    If it’s a weekend:
        Add $20/night for Standard and Deluxe rooms.
        Add $50/night for Suites.
    If the person has a membership, apply a 10% discount.
    If the stay is longer than 5 nights, apply an additional 5% discount.
"""
nights = int(input("How many night will you be staying"))
is_weekend = input(" q")
room_type = input("Please Select a room:")
has_membership = input("chickens")

if is_weekend.lower() == "yes" or is_weekend.lower() == "y":
    is_weekend = True
if is_weekend.lower() == "no" or is_weekend.lower() == "n":
    is_weekend = False

if has_membership.lower() == "yes" or has_membership.lower() == "y":
    has_membership = True
if has_membership.lower() == "no" or has_membership.lower() == "n":
    has_membership = False

if 