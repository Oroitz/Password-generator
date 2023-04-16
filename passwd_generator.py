#!/usr/bin/python

# This scpript generates locally a password

import random

# Number of characteres of the password

charnmbr = 12

# mode = 1 -> Mixes the lists, making the probability for each kind of character depend on the each character's list's size
# mode = 2 -> Without mixing the lists, making the same probability to use each kind of characters
# mode = 0 -> Use both modes

mode = 0

# Allows the lists of each kind of character
# minus, mayus, numbr, special, accmark

lists = [True, True, True, True, True]

# Error checking

if lists.count(True) == 0:
	print("Error, there is not character list activated")
	exit()

if charnmbr <= 0:
	print("Error, the minimun length of the password must be higher than 0")
	exit()

# Characters lists:

minus = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
mayus = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbr = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
special = ['!', '¡', '@', '#', '$', '%', '~', '€', '¬', '&', '/', '(', ')', '=', 'ç', 'Ç', '[', ']', '{', '}', '^', '`', '´', '+', '*', ',', ';', '.', ':', '-', '_']
accmark = ['á', 'é', 'í', 'ó', 'ú', 'à', 'è', 'ì', 'ò', 'ù', 'â', 'ê', 'î', 'ô', 'û', 'ä', 'ë', 'ï', 'ö', 'ü', 'ã']

# Mode 1

if mode == 1 or mode == 0:
	
	characters = []
	if lists[0] == True:
		characters.extend(minus)
	if lists[1] == True:
		characters.extend(mayus)
	if lists[2] == True:
		characters.extend(numbr)
	if lists[3] == True:
		characters.extend(special)
	if lists[4] == True:
		characters.extend(accmark)
	
	output = ''
	for n in range(charnmbr):
		output = output + characters[random.randint(0, len(characters)-1)]
	
	print(output)

# Mode 2

if mode == 2 or mode == 0:

	elements = []
	if lists[0] == True:
		elements.append('minus')
	if lists[1] == True:
		elements.append('mayus')
	if lists[2] == True:
		elements.append('numbr')
	if lists[3] == True:
		elements.append('special')
	if lists[4] == True:
		elements.append('accmark')

	output = ''
	for n in range (charnmbr):
		if len(elements) > 1:
			element = elements[random.randint(0, len(elements)-1)]
		else:
			element = elements[0]
		if element == 'minus':
			output = output + minus[random.randint(0, len(minus)-1)]
		if element == 'mayus':
			output = output + mayus[random.randint(0, len(mayus)-1)]
		if element == 'numbr':
			output = output + numbr[random.randint(0, len(numbr)-1)]
		if element == 'special':
			output = output + special[random.randint(0, len(special)-1)]
		if element == 'accmark':
			output = output + accmark[random.randint(0, len(accmark)-1)]

	print(output)
