import os
first = True
lineToWrite = []

with open("cardInformation.txt", "r") as inFile:
	with open('cardInfo.py','w') as outFile:
		for line in inFile:
			if first:
				outFile.write("### THIS FILE IS AUTOGENERATED\n")
				outFile.write("### DO NOT HAND EDIT\n")
				outFile.write("### TO REGENERATE: run python infoStrip.py\n")
				outFile.write("cards = [\n")
				first = False
			if "CARD PAGE" in line:
				outFile.write("# " + line)
			if "Name        :" in line:
				lineToWrite.append("{'name' : '")
				cardName = ("%15s") %line.split(":")[1].strip("\n")
				lineToWrite.append(cardName)
				lineToWrite.append("' , ")
				outFile.write(''.join(lineToWrite))
				lineToWrite = []
			if "Elemental   :" in line:
				lineToWrite.append("'elemental' : '")
				cardElemental = ("%7s") %line.split(":")[1].strip("\n")
				lineToWrite.append(cardElemental)
				lineToWrite.append("' , ")
				outFile.write(''.join(lineToWrite))
				lineToWrite = []
			if "Statistics  :" in line:
				lineToWrite.append("'stats' : ['")

				top        = line.split(":")[1].strip(" ").strip("\n")
				middleVals = next(inFile, "").strip(" ")
				left       = middleVals.split(" ")[0]
				right      = middleVals.split("  ")[1].strip(" ").strip("\n")
				bottom     = next(inFile, "").strip(" ").strip("\n")

				lineToWrite.append(top)
				lineToWrite.append("', ")
				lineToWrite.append("'")
				lineToWrite.append(left)
				lineToWrite.append("', ")
				lineToWrite.append("'")
				lineToWrite.append(right)
				lineToWrite.append("', ")
				lineToWrite.append("'")
				lineToWrite.append(bottom)
				lineToWrite.append("'] } ,\n")
				outFile.write(''.join(lineToWrite))
				lineToWrite = []
		outFile.write("]")