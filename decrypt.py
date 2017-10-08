# Program to decrypt the cipher
# This program takes the input from the user which was received as an output from the Fake_Passport_Main.py
# It takes only one line as input at a time and shifts the value 4 to the right only for alphabets.
# The Decrypted text is displayed onto the screen.

# Get the Encrypted text from the user. One line input
dec_ip = input("Please enter the encrypted text : ")


# The function takes one line input of Encrypted text, checks each character at a time and checks if it has
# alphabets in it. Decryption is done by shifting 4 characters to the right only for alphabets. Other characters
# are kept as it is.
def decrypt_text(input_name):
    decrypted_text = ''
    for temp_char in input_name:
        if temp_char.isalpha():
            number = ord(temp_char) + 4

            if temp_char.isupper():
                if number > ord('Z'):
                    number -= 26

            elif temp_char.islower():
                if number > ord('z'):
                    number -= 26

            decrypted_text += chr(number)

        else:
            decrypted_text += temp_char

    return decrypted_text


# Function is called by passing the input encrypted text from the user
dec_op = decrypt_text(dec_ip)

# Output of the function would be stored in dec_op and it would be displayed on the screen
print("Decrypted text is : " + dec_op)
