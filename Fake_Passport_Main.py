# Fake Passport Generator
# This program is to take two names from the user, two ages, current year and create a
# fake passport by following a specific logic. The final Fake passport is displayed to the user
# In addition to that the passport details are encrypted by using Ceaser Cipher by
# shifting 4 characters to the left. Ciphering is done only for the alphabets and not for other chracters
# and numbers. The file decrypt.py should be used by the user to get back the decrypted text.

# Importing the libraries
import random


# 1.1 New Name Generation

# Take First Name 1 and Last Name 1 input from user
first_name1 = input("Please enter First Name 1 : ")
last_name1 = input("Please enter Last Name 1 : ")

# Take First Name 2 and Last Name 2 input from user
first_name2 = input("Please enter First Name 2 : ")
last_name2 = input("Please enter Last Name 2 : ")


# 1.1 New Date of Birth Inputs
# Function to check integer. This function takes a string input and checks
# if has only digits in it. If no digits are found, the program would stop proceeding
# further and quit gracefully
def check_integer(value):
    if not value.isdigit():
        print("Please enter only integer value ")
        quit()

# Take two ages in years as input from user
first_age = input("Please enter Age 1 in Years : ")
# Check if the input age has only digits in it
check_integer(first_age)

sec_age = input("Please enter Age 2 in Years : ")
# Check if the input age has only digits in it
check_integer(sec_age)

# Take the input from the user for the current year
current_year = input("Please enter the current year : ")
# Check if the input year has only digits in it
check_integer(current_year)


# 1.1 Function to create new name. The function take 2 names name1 and name2 and returns a value new_name.
def create_name(name1, name2):

    # Creating First Half of the New name from Name1

    # Checking if the number of characters in Name1 is Odd or Even
    if (len(name1) % 2) == 0:
        # If the length of Name1 is Even, first half of the new name is created by splitting the name into exact half
        # and the first half is choosen for the new name
        first_half = name1[:int(len(name1)/2)]
    else:
        # If the length of Name1 is Odd, first half of the new name is created by splitting the name into half
        # and including the middle character to it
        first_half = name1[:int((len(name1)+1) / 2)]

    # Creating Second Half of the New name from Name2
    if (len(name2) % 2) == 0:
        # If the length of Name2 is Even, second half of the new name is created by splitting the name into exact half
        # and the second half is choosen for the new name
        sec_half = name2[int(len(name2) / 2):]
    else:
        # If the length of Name2 is Odd, second half of the new name is created by splitting the name into half
        # and including the middle character to it
        sec_half = name2[int((len(name2)) / 2):]

    new_name = first_half + sec_half

    return new_name

# 1.1 Passing the values First Name 1, First Name 2, Last Name 1. Last Name 2 which is received from the user and
# calling the functions create_name which generates the new name. New first name and Last names would be available
# in the variables new_first_name and new_last name
new_first_name = create_name(first_name1, first_name2)
new_last_name = create_name(last_name1, last_name2)


# 1.2 New Date of Birth

# Adding the digits from each Age1 and Age2 and then combining both of the values and using it for the new age
new_age = sum(int(number) for number in str(first_age)) + sum(int(number) for number in str(sec_age))

# Generating a random number from 1 to 12 for the month to be used in the fake passport
new_month = random.randint(1, 12)

# Applying a logic to generate a valid date based on the month which was picked

# If the month is 2 (Feb) we generate a random date to be in the range 1 to 29
if new_month == 2:
    new_date = random.randint(1, 29)

# If the months are anything in Jan, Mar, May, Jul, Aug, Oct, Dec, then we generate a random date
# in the range 1 to 31
elif new_month in [1, 3, 5, 7, 8, 10, 12]:
    new_date = random.randint(1, 31)

# If the above two conditions fail then the months should be surely within Apr, Jun, Sep, Nov.
# we generate a random date in the range 1 to 30
else:
    new_date = random.randint(1, 30)

# We convert the new date and new month to string and also making sure that the digits are 2 characters.
# We would append 0 in front in case if the date and month are single digits
new_date = str(new_date).zfill(2)
new_month = str(new_month).zfill(2)

# New Year to be used for the fake passport in calculated by subtracting the new age that we calculated
# from the current year which was received as input. Current year is type casted to int to perform the
# arithmetic operation
new_year = int(current_year) - new_age

# New Date of Birth (new_dob) is created by concatenating the values new date, new month and new year.
# new dob would be a string type with the format dd/mm/yyyy
new_dob = new_date + '/' + new_month + '/' + str(new_year)


# 1.3 New ID Generation

# New_ID would be the final ID to be used for the Passport. New_Age field is passed to the
# ID field
new_ID = str(new_age)

# Checking if the number of characters in the New_ID field is less than 10.
while len(new_ID) < 10:
    # Add the last two digits of the new_ID and store it at a temporary variable
    temp = int(new_ID[len(new_ID)-2]) + int(new_ID[len(new_ID)-1])
    # New_ID is appended with the remainder of temp/10 as per requirement
    new_ID += str(temp % 10)


# 1.4 Formatting the Passport
print("-----------------------------------Passport------------------------------------------")
print("-------------------------------------------------------------------------------------")
print("Name : %s %s \t \t \t \t \t \t \t \t ID : %10s" % (new_first_name, new_last_name, new_ID))
print("\n")
print("Date of Birth : " + new_dob)
print("\n")
print("----------------------------Authorized by Najam Zaidi---------------------------------")
print("-------------------------------------------------------------------------------------")

# Creating variables to store the details of the passport to be used for encryption.
encr_txt1 = 'Name : ' + new_first_name + ' ' + new_last_name + ' \t \t \t \t \t \t \t \t ID  : ' + str(new_ID)
encr_txt2 = "Date of Birth : " + str(new_dob)
encr_txt3 = "----------------------------Authorized by Najam Zaidi---------------------------------"


# 1.5 Encryption

# Encrypt_text is a function which takes a string as input and returns and encrypted text.
# Encryption is done by shifting the value to 4 ASCII value in the left.
def encrypt_text(input_name):
    # encrypted_text is initialized with blank value
    encrypted_text = ''
    # Reading the input one character per loop
    for temp_char in input_name:
        # Encryption is done only for Alphabets. Anything apart from alphabets are ignored
        if temp_char.isalpha():
            # Alphabets are shifted 4 places to the left
            number = ord(temp_char) - 4

            # Checking if the character is in upper case
            if temp_char.isupper():
                # In case the value went lower than the ASCII of 'A' it would be symbol.
                # So to maintain the circle, it is increased with 26 characters
                if number < ord('A'):
                    number += 26
            # Checking if the character is in lower case
            elif temp_char.islower():
                # In case the value went lower than the ASCII of 'a' it would be symbol.
                # So to maintain the circle, it is increased with 26 characters
                if number < ord('a'):
                    number += 26

            # Encrypted text is added with the encrypted character per loop
            encrypted_text += chr(number)

        else:
            # If the character is not an alphabet, then the character is added as it is
            encrypted_text += temp_char

    # After the loop, encrypted_text would now have the complete excrypted string which
    # would be returned
    return encrypted_text

# Printing the Encrypted Text by pasing the passport values
print("\n\n")
print("----------------------------Encrypted Passport---------------------------------------")
print("-------------------------------------------------------------------------------------")
print(encrypt_text(encr_txt1))
print("\n")
print(encrypt_text(encr_txt2))
print("\n")
print(encrypt_text(encr_txt3))
