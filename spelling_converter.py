"""Converts NZ English string to US English string by checking over
individual spellings of words"""
from easygui import *


# different spellings patterns will be stored as nz:us value pairs
SPELLINGS = {
    "our": "or",
    "ise": "ize",
    "yse": "yze"
}


nz_input = input("Enter your sentence in NZ English")
us_output = nz_input
for i in SPELLINGS:
    if i in us_output:
        us_output = us_output.replace(i, SPELLINGS[i])
if us_output == nz_input:
    print("No change in spelling")
else:
    print(us_output)
