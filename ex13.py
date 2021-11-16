from sys import argv
""" 
To run this script you should pass 4 variable, one of it is a script name itself
exapmle: python3 ex13.py 1 2 3
"""
script, first, second, third = argv

print("The script is called", script)
print("Your first variable is", first)
print("Your second variable is", second)
print("Your third variable is", third)