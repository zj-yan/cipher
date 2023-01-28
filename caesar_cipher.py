import re
import string
alphabet = string.ascii_uppercase

def plainText():
    global plain
    original = input("Type the plain text\n")
    cop = re.compile("[^a-z^A-Z]")
    plain = cop.sub('', original).upper()
    print("The plain text is")
    print(plain)

def encrypt(num):
    global cipher 
    cipher = ''
    for char in plain:
        cipher += chr((ord(char) + num - 65) % 26 + 65)
    print("The cipher text is")
    print(cipher)


plainText()
encrypt(3)
