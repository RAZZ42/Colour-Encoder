# constants
BLUE = list("0000ff")
GREEN = list("00ff00")
GENERIC = str("0x000000")

def encoder(user_input):
    encoded_lst = []
    if user_input[0] != GENERIC[1]:  # This checks to confirm if 0x exists.
        user_input[:0] = ["0x"]  # If it does exists, places '0x' at the start of the string.
        hex_num = "".join(user_input)  # Joins the string together.
        encoded_lst = hex_num  # Converts into hexadecimal by going into a list.
        print(encoded_lst)  # Checks to see if it works or not.

def main():
    """
    takes in user input and outputs "Green", "Blue" or "not Green or Blue" based on the input"""
    user_input = list(input("Input: ").lower())
    encoded_lst = []
    if user_input[-4:-3] >= GREEN[-4:-3] or user_input[-3:-2] >= list(GREEN[-3:-2]):
        encoder(user_input)
        print("Green")
    elif user_input[-2:-1] >= list(BLUE[-2:-1]) or user_input[-1:] >= list(BLUE[-1:]):
        encoder(user_input)
        print("Blue") 
    else:
        print("not Green or Blue")

main()

# ---------------------------------
#       Quick to do list:
# 1 Learn this fancy code:
#       i = 0xhelloworld
#       hex_string = f'0x{i:>010X}'
#       print(hex_string)
# 2 Feed data into this script
#   and print the outcome.
#
# ---------------------------------
