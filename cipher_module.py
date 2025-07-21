
import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)

def key():
    key = chars.copy()
    random.shuffle(key)
    return key

def save_key(key, filename= 'key.txt'):
    with open(filename, "w") as f:
        f.write("".join(key))

def load_key(filename= 'key.txt'):
    with open(filename, "r") as f:
        return list(f.read())
    
def encrypt(plain_text, key):
    cipher_text = ""
    for letter in plain_text:
        if letter in chars:
            index = chars.index(letter)
            cipher_text += key[index]
        else:
            cipher_text += letter
    return cipher_text

def decrypt(cipher_text, key):
    plain_text = ""
    for letter in cipher_text:
        if letter in key:
            index = key.index(letter)
            plain_text += chars[index]
        else:
            plain_text += letter
    return plain_text

def check_password(input_password, correct_pass= "godecryp"):
    return input_password == correct_pass
    