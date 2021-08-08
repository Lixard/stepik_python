from simplecrypt import *

with open("/Users/lixard/Downloads/encrypted.bin", "rb") as inp:
    encrypted = inp.read()

with open("/Users/lixard/Downloads/passwords.txt", "r") as pass_inp:
    passwords = pass_inp.readlines()

for p in passwords:
    try:
        print("Try to decrypt with pass: ", p)
        print(decrypt(p.strip(), encrypted))
    except DecryptionException:
        print("Failed to decrypt with pass: ", p)
