# Funny binary converter
# created by skye wilson

import os
from string import join

z = "enter message here: "

try:
    os.system("say Dont be a dick. this converter will change all letters into uppercase, it also does not recognize symbols and signs. enter message here.")

    print """Don't be a dick! This converter will change all letters into 
        uppercase. It also does not recognize symbols and signs."""
except:
    print """Don't be a dick! This converter will change all letters into 
    uppercase only, it also does not recognize symbols and signs."""

bin_list = {"A": "01000001", "B": "01000010", "C": "01000011", "D": "01000100", "E": "01000101", "F": "01000110", 
            "G": "01000111", "H": "01001000", "I": "01001001", "J": "01001010", "K": "01001011", "L": "01001100", 
            "M": "01001101", "N": "01001110", "O": "01001111", "P": "01010000", "Q": "01010001", "R": "01010010", 
            "S": "01010011", "T": "01010100", "U": "01010101", "V": "01010110", "W": "01010111", "X": "01011000", 
            "Y": "01011001", "Z": "01011010", " ": "00100000"}

user_message = raw_input(z)  # type: str

user_message = user_message.upper()

user_output = []

user_list = list(user_message)


for x in user_list:
    if x in bin_list: user_output.append(bin_list[x])
    else:
        os.system("say you fuck. Character not found")

print_2_user = join(user_output)

print print_2_user