alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# List index
# https://www.w3schools.com/python/ref_list_index.asp

# TODO-1: Create a function called 'encrypt()' that takes
#  'original_text' and 'shift_amount' as 2 inputs.

# TODO-2: Inside the 'encrypt()' function, shift each letter
#  of the 'original_text' forwards in the alphabet
#  by the shift amount and print the encrypted text.

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
    shift_message = f'Here is the encoded message: {shift_message}'
    return shift_message


# TODO-4: What happens if you try to shift z forwards by 9?
#  Can you fix the code?

# TODO-3: Call the 'encrypt()' function and pass in the user inputs.
#  You should be able to test the code and encrypt a message.

message = encrypt(text, shift)

print(message)
