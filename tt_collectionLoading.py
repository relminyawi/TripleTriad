import os
import stat
import sys
import cardInfo as ci

memCardDir = os.path.join(os.path.dirname(__file__), 'Memory Card')

# Starts out as default cards, more are added to dict
currentCollection = {
'Geezard' : 1 ,
'Funguar' : 1 ,
'Bite Bug': 1 ,
'Red Bat' : 1 ,
'Blobra'  : 1 ,
}

currentHand = []

def printCollection():
	print "Your current cards are as follows"
	print "          NAME        COUNT"
	for name, count in currentCollection.items():
		print "%15s" % name + "%10s" % count

def addToCollection(cardName, count):
	print "\nAdding %s copies of %s to your collection" % (count, cardName)
	currentCollection[cardName] = count

def saveCollection(collectionName):
	print "\nSaving your current collection under name %s" % collectionName
	filename = os.path.join(memCardDir, collectionName + '.txt')
	os.chmod(filename, stat.S_IWUSR|stat.S_IREAD)
	with open(filename,'w') as outFile:
		for name, count in currentCollection.items():
			outFile.write(name)
			outFile.write(", ")
			outFile.write("%s" %count)
			outFile.write("\n")
	os.chmod(filename, stat.S_IREAD|stat.S_IRGRP|stat.S_IROTH)

def loadCollection(collectionName):
	print "\nOpening collection %s" % collectionName
	filename = os.path.join(memCardDir, collectionName + '.txt')
	with open(filename,'r') as inFile:
		for line in inFile:
			name = line.split(',')[0].strip()
			count = line.split(',')[1].strip()
			addToCollection(name, count)

def loadDefaultCollection(saveName):
	print "\nNew collection!"
	print "Saving collection first.."
	saveCollection(saveName)

def beginGameOptions():
	collectionChoice = raw_input("\nNew game or load previous from list above (type file name without extension)?\n")

	if collectionChoice.lower() == "new game":
		print "You will begin with the basic set of cards"
		saveName = raw_input("Please give your current collection a new name: \n")
		if os.path.exists(os.path.join(memCardDir, saveName + ".txt")):
			overWrite = raw_input("%s collection already exists. Overwrite?\n" % saveName)
			if overWrite.lower() == "yes":
				loadDefaultCollection(saveName)
				return saveName
			else:
				beginGameOptions()
	elif collectionChoice.lower() != "new game" and len(os.listdir(memCardDir)) == 0:
		print "You do not have any saved collections"
		print "You will begin with the basic set of cards"
		saveName = raw_input("Please give your current collection a new name: \n")
		loadDefaultCollection(saveName)
		return saveName
	else:
		for file in os.listdir(memCardDir):
			if os.path.exists(os.path.join(memCardDir, collectionChoice + ".txt")):
				loadCollection(collectionChoice)
				saveName = collectionChoice
				break
		return saveName

def addToHand():
	print "\nFrom your list of cards, select 5 to use in your hand"
	cardsInHand = 0
	while cardsInHand < 5:
		cardName = raw_input("Please select a card to add to your hand\n")
		if cardName not in currentCollection.keys():
			print "You do not have that card, choose another"
		else:
			currentHand.append(cardName)
			cardsInHand += 1

def main():
	print "\nType 'New Game' to begin a new collection"
	print "Type your collection's name to load from a previous save"
	print "The current collections are as follows:"
	print "\n"
	print "%s" % os.listdir(memCardDir)
	print "\n"

	saveName = beginGameOptions()

	print "Let's start the game!\n"
	collectionView = raw_input("Would you like to see your collection one more time (yes or no)?\n")
	if collectionView.lower() == "yes": 
		printCollection()
		print "\n"

	saveGame = raw_input("Would you like to save your progress before you begin?\n")
	if saveGame.lower() == "yes": 
		saveCollection(saveName)

	addToHand()
if __name__ == "__main__":
    main()