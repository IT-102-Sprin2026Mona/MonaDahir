#!/usr/bin/env python3
# Sample script that writes to a file
# By Ed Goad
# 12/12
"""
Write a script that saves user input into a file, that gathers data about the user
"""

#These variables are questions that need to be answerd
name = input("What is your name? ")
color = input("What is your favorite color? ")
pet = input("What is your first pets name? ")
maiden = input("What is your mother maiden name? ")
school = input("What elementry school did you intend? ")

with open("hackme.txt", "w") as file:
    file.write(f"Name: {name}\n")
    file.write(f"favorite Cole: {color}\n")
    file.write(f"First Pet: {pet}\n")
    file.write(f"Mothers Maiden Name: {maiden}\n")
    file.write(f"Elementary School: {school}\n")

print("Saved to kackme.txt Great work!")


