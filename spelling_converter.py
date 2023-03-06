"""Converts NZ English string to US English string by checking over
spelling patterns in words"""
from easygui import *


# different spellings patterns will be stored as nz:us value pairs
SPELLINGS = {
    "our": "or",
    "ise": "ize",
    "yse": "yze"
}


def main():
    nz_input = enterbox("Enter your sentence in NZ English", "Enter Sentence")
    us_output = nz_input

    # for every pattern in SPELLINGS, check if it is in sentence,
    # and replace that part of the string if so
    for i in SPELLINGS:
        if i in us_output:
            us_output = us_output.replace(i, SPELLINGS[i])
            
    if us_output == nz_input:
        msgbox("No change in spelling", "Output")
    else:
        msgbox(f"New sentence in US English:\n\n{us_output}", "Output")

    if ynbox("Would you like to convert another sentence?", "Repeat "
                                                            "Conversion"):
        main()
    else:
        msgbox("Goodbye", "End program")


main()


