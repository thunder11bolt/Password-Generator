# THIS CODE BY THUNDERBOLT

import random

Character = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!$%#@&~`*)(^"

while 1:
    print("# ThunderBolt Password Generator")
    account_name = input("What is your account : ")
    password_lenght = int(input("what lenght that you wont your password be : "))
    password_count = int(input("How many passwords would you like :  "))

    for x in range(0, password_count):
        ThePassword = ""
        for x in range(0, password_lenght):
            password_character = random.choice(Character)
            ThePassword = ThePassword + password_character
        print("For This Account : ", account_name, " , Your Password Is: ", ThePassword)
