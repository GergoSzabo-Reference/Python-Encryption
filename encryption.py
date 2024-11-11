import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters # szóköz + szimbólumok + számok + betűk
chars = list(chars) # listává alakítjuk a chars sztringet
key = chars.copy() # készítünk egy másolatot belőle

random.shuffle(key) # minden egyes karakter a 'chars'-ból referálni fog a 'key' listában az adott karakter indexén lévő karakterre

#ENCRYPT
plain_text = input("Enter a message to encrypt: ")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter) # jelöljük a jelenlegi indexet a 'chars' listában lévő karakterek közül
    cipher_text += key[index] # refálunk az adott indexre a 'key' listából

print(f"Encrypted message: {cipher_text}")

#DECRYPT
cipher_text = input("Enter a message to decrypt: ")
plain_text = ""

for letter in cipher_text:
    index = key.index(letter) # jelöljük a jelenlegi indexet a 'key' listában lévő karakterek közül
    plain_text += chars[index] # refálunk az adott indexre a 'chars' listából

print(f"Decrypted message: {plain_text}")