alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# TODO-1: Create a function called 'decrypt()' that takes 'original_text' and 'shift_amount' as inputs.
# TODO-2: Inside the 'decrypt()' function, shift each letter of the 'original_text' *backwards* in the alphabet
#  by the shift amount and print the decrypted text.
# TODO-3: Combine the 'encrypt()' and 'decrypt()' functions into one function called 'caesar()'.
#  Use the value of the user chosen 'direction' variable to determine which functionality to use.

# List index
# https://www.w3schools.com/python/ref_list_index.asp

def encrypt(v_text, v_shift):
    # will act as the container for the test
    shift_message = ""

    for letter in v_text:
         # Take modulus to stay within the array bounds (index % 26,
         # returning a range between 0-25 in the alphabet array of size 26):
         shifted_position = (alphabet.index(letter) + v_shift) % 26
         # print(alphabet.index(letter), letter, shifted_position, (alphabet[shifted_position]))
         # create a letter by passing in the value of the shifted index value
         shift_message += alphabet[shifted_position]
    # shift_message = f'Here is the encoded message: {shift_message}'
    return shift_message


def decrypt(v_text, v_shift):
    shift_message = ""

    for letter in v_text:
         # Take modulus to stay within the array bounds (index % 26,
         # returning a range between 0-25 in the alphabet array of size 26):
         shifted_position = (alphabet.index(letter) - v_shift) % 26
         # print(alphabet.index(letter), letter, shifted_position, (alphabet[shifted_position]))
         # create a letter by passing in the value of the shifted index value
         shift_message += alphabet[shifted_position]
    # shift_message = f'Here is the decoded message: {shift_message}'
    return shift_message


def caesar(v_direction, v_text, v_shift):
    if v_direction == 'encode':
        message = encrypt(v_text, v_shift)
    elif v_direction == 'decode':
        message = decrypt(v_text, v_shift)
    return message


my_message = caesar(direction, text, shift)

print(my_message)
