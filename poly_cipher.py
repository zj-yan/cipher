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

def getIndexWord():
    global index
    key = input("Pick a keyword\n")
    index = [alphabet.find(char) for char in key]
 
def encrypt():
    global cipher 
    cipher = ''
    for i in range(len(plain)):
        orig_index = alphabet.find(plain[i])
        method = index[i % len(index)]
        new_index = (orig_index + method) % len(alphabet)
        cipher += alphabet[new_index]
    print("The cipher text is")
    print(cipher)

plainText()
getIndexWord()
encrypt()