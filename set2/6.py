"""
6. Travel Recommendation System
Write a program that suggests a mode of travel based on distance and conditions.

Input Variables:
distance (float): The distance to travel (in miles).
is_sunny (boolean): Whether it’s sunny (True or False).
owns_bike (boolean): Whether the person owns a bike (True or False).
is_rush_hour (boolean): Whether it’s rush hour (True or False).
Travel Recommendations:
If the distance is less than 5 miles:
If it’s sunny, recommend "walking".
If it’s raining, recommend "driving".
If the distance is 5-20 miles:
If the person owns a bike, recommend "cycling".
Otherwise, recommend "bus".
If the distance is over 20 miles:
If the person has a car and it’s not rush hour, recommend "driving".
If it’s rush hour, recommend "train".
"""