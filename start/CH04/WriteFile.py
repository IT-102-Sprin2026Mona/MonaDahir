#!/usr/bin/env python3
# Sample script that writes to a file
# By 

'''
Write a cript that saves user input into a file,
that gathers data about the user
'''

#These variable are question that need to be answered
name = input("What is your name? ")
color = input("What is your favorite color?")
pet = ("What is your first pets name?")
maiden = ("What is your mother mainden name?")
school =("What elementray school did your intend?")

with open("hackme.txt", "w") as file:
    file.write(f"Name: {name}\n")
    file.write(f"Favorit Color: {color}\n")
    file.write(f"First Pet: {pet}\n")
    file.write(f"Mothers Maiden Name {maiden}\n")
    file.write(f"Elementary School: {school}\n")

print("Save to hackme.txt Great work!")

