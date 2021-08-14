# Target values
BLUE = list("0000ff")
GREEN = list("00ff00")
GENERIC = 0x000000

# install libraries
#import numpy as np

# Encoder
input_encoder = input("Input: ").lower()

lst_input_encoder = list(input_encoder)

def not_blue():
    if lst_input_encoder[-2:-1] >= BLUE[-2:-1]:  # This only works with two last FFs

        for n in lst_input_encoder:
            if n[0] != GENERIC[0]:
                hex_num = "#" + str(lst_input_encoder[0:])
                hex_joined = "".join(hex_num)
        print(hex_joined)

        print("Blue")
    else:
        print("Not Blue")

def not_green():
    if lst_input_encoder[-4:-2] >= GREEN[-4:-2]:  # This only works with two middle FFs
        print("Green")
    else:
        print("Not Green")


not_blue()
not_green()
#----------------------------
#  Quick to do list:
#  Explain each line of code.
#  Fix up the #.
#-----------------------------