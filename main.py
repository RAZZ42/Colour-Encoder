# Target values
BLUE = list("0000ff")
GREEN = list("00ff00")
GENERIC = str("0x000000")

# User input
input_encoder = input("Input: ").lower()

# Converts into a list.
lst_input_encoder = list(input_encoder)

# defines both two functions to discriminate whether it is a blue or green hexadecimal, else it is confused.
def not_blue():
    encoded_lst = []
    if lst_input_encoder[-2:-1] >= BLUE[-2:-1]:  # This only works with two last FFs
        if lst_input_encoder[0] != GENERIC[1]:  # This checks to confirm if # exists - if not, it creates into encoder.
            lst_input_encoder[:0] = ["0x"]  # Places '0x' at the start of the string.
            hex_num = "".join(lst_input_encoder)  # Joins the string together.
            encoded_lst = hex_num  # Converts into hexadecimal by going into a list.
            print(encoded_lst)  # Checks to see if it works or not.
        print("Blue")  # Prints the outcome.
    else:
        print("Not Blue")  # Self-explanatory.

# Description above applies to the def below. They are both the same.

def not_green():
    encoded_lst = []
    if lst_input_encoder[-4:-2] >= GREEN[-4:-2]:  # This only works with two middle FFs
        if lst_input_encoder[0] != GENERIC[1]:
            lst_input_encoder[:0] = ["0x"]
            hex_num = "".join(lst_input_encoder)
            encoded_lst = hex_num
            print(encoded_lst)
        print("Green")
    else:
        print("Not Green")


not_blue()
not_green()



#---------------------------------
#       Quick to do list:
# 1 Learn this fancy code:
#       i = 0xhelloworld
#       hex_string = f'0x{i:>010X}'
#       print(hex_string)
# 2 Scrape data off web and test
#   the script out.
#
#
#
#---------------------------------