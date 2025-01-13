#make rock paper scissors
import random
botchoice = ["rock","paper","scissors"]
rockingpaper = input("Pick Rock, Paper, or Scissors: ")
if rockingpaper.lower() == random.choice(botchoice):
    print("You TIE with the robot")
elif rockingpaper.lower() != random.choice(botchoice):
    if