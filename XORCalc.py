
while True:
	textIn = input("Type 'exit0' to leave\nInsert Text: ")

	if textIn == "exit0":
                break

	keyIn = input("Insert HexaDecimal (Ex: 0x45 or just 45): ")

	if keyIn == "exit0":
                break

	try:
		keyIn = int(keyIn, 16)
	except ValueError:
		print("Invalid Input!")

	resultOut = ''.join(chr(ord(c) ^ keyIn) for c in textIn)
	print(resultOut)
	print("")

