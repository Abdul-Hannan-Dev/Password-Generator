#In this code, a unique password is generated to the user each time the code is run.

#Creating a function called "generate_password"
def generate_password():

#importing the random library
    import random

#generating new character each time, a total of 8 in our case.
    char1 = chr(random.randint(65, 90))
    char2 = chr(random.randint(65, 90))
    char3 = str(random.randint(0, 9))
    char4 = chr(random.randint(33, 47))
    char5 = chr(random.randint(97, 122))
    char6 = chr(random.randint(97, 122))
    char7 = chr(random.randint(33, 47))
    char8 = str(random.randint(0, 9))

#combining all the characters in a list called 'chars' (characters).
    chars = [char1, char2, char3, char4, char5, char6, char7, char8]

#shuffling the characters so that each time the function is called for different password, the special characters, letters and numbers are arranged in random order.
    random.shuffle(chars)

#addings the characters in variable named "password."
    password = ""
    for char in chars:
        password += char
    print(password)

#finally, calling our function.
generate_password()