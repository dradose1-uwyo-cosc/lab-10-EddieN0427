# Eddie Neitenbach
# UWYO COSC 1010
# Submission Date: 11/24/2024
# Lab 10
# Lab Section: 11
# Sources, people worked with, help given to: 
# your
# comments
# here

#import modules you will need 

from hashlib import sha256 
from pathlib import Path

def get_hash(to_hash):
    """You can use """
    return sha256(to_hash.encode('utf-8')).hexdigest().upper()

try:
    hash_pash = Path('hash')  
    with hash_pash.open('r') as file:
        target = file.read().strip()  
except Exception as sus:
    print(f"Error in 'hash' file: {sus}")
    exit(1)
try:
    rock_file = Path('rockyou.txt')  
    with rock_file.open('r') as file:
        for password in file:
            password = password.strip()
            hashed_password = get_hash(password)
            if hashed_password == target:
                print(f"The password is: {password}")
                break  
        else:
            print("Password is not found.")
except Exception as sus:
    print(f"Error in 'rockyou.txt' file: {sus}")




# Files and Exceptions

# For this assignment, you will be writing a program to "crack" a password. You will need to open the file `hash` as this is the password you are trying to "crack."

# To begin, you will need to open the 'rockyou.txt' file:
# - This file contains a list of compromised passwords from the rockyou dump.
# - This is an abridged version, as the full version is quite large.
# - The file contains the plaintext version of the passwords. You will need to hash them to check against the password hash you are trying to crack.
#   - You can use the provided `get_hash()` function to generate the hashes.
#   - Be careful, as "hello" and "hello " would generate a different hash.

# You will need to include a try-except-catch block in your code.
# - The reading of files needs to occur in the try blocks.


# - Read in the value stored within `hash`.
#   - You must use a try and except block.


# Read in the passwords in `rockyou.txt`.
# - Again, you need a try-except-else block.
# Hash each individual password and compare it against the stored hash.
# - When you find the match, print the plaintext version of the password.
# - End your loop.
