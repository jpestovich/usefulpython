#Generates passwords from 8-20 characters
#by Joe Pestovich 11/29/22
import random
import string

print("\n--------------------------------------\n----Super Cool Password Generator-----\n--------------------------------------\n")
charset = string.ascii_letters + string.digits + string.punctuation
print("Current character set: " + charset + "\n")

#define functions to get password length and generate password
def get_length():
    while True:
        try:
            passlength = int(input("\nEnter Password Length (8-20 characters): "))
        except ValueError:
            print("Sorry didn't catch that \_O_/ Make sure you enter something I can understand")
            continue
        if passlength < 8 or passlength > 20:
            print("Password must be at least 8 characters and no more than 20")
            continue
        else:
            return passlength

def gen_password(passlength):
    print("\nPassword will be " + str(passlength) + " characters long!")
    password = ''
    i = 0
    while i < passlength:
        password += (random.choice(charset))
        i = i + 1
    print("Here's your password:\n" + password +"\n")

#call functions & give user option to generate more passwords
passlength = get_length()
gen_password(passlength)
while True:
    try:
        another = str.lower(input(("Want another password? y/n: ")))
    except ValueError:
        print("Sorry didn't catch that \_O_/ Make sure you enter something I can understand")
        continue
    if another == "y" or another == '':
        print("Here we go again!")
        passlength = get_length()
        gen_password(passlength)
        continue
    if another == "n":
        print("\nOk, see ya next time :D\n")
        break
    else:
        print("\nEnter 'N' or 'n' to exit!\n")
        continue