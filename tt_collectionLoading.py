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

def printCollection():
	print "Your current cards are as follows"
	print "          NAME        COUNT"
	#print currentCollection
	for name, count in currentCollection.items():
		print "%15s" %name + "%10s" % count

def addToCollection(cardName, count):
	print "Adding %s copies of %s to your collection" % (count, cardName)
	currentCollection[cardName] = count

def saveCollection(collectionName):
	print "Saving your current collection under name %s" % collectionName
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
	print "Opening collection %s" % collectionName
	filename = os.path.join(memCardDir, collectionName + '.txt')
	with open(filename,'r') as inFile:
		for line in inFile:
			name = line.split(',')[0].strip()
			count = line.split(',')[1].strip()
			addToCollection(name, count)

def loadDefaultCollection(saveName):
	print "New collection!"
	print "Saving collection first.."
	saveCollection(saveName)

def main():
	print "Type 'New Game' to begin a new collection"
	print "Type your collection's name to load from a previous save"
	print "The current collections are as follows:"
	print "\n"
	print "%s" % os.listdir(memCardDir)
	print "\n"
	collectionChoice = raw_input("New game or load previous from list above (type file name without extension)?\n")

	if collectionChoice.lower() == "new game":
		print "You will begin with the basic set of cards"
		saveName = raw_input("Please give your current collection a new name: \n")
		loadDefaultCollection(saveName)
	elif collectionChoice.lower() != "new game" and len(os.listdir(memCardDir)) == 0:
		print "You do not have any saved collections"
		print "You will begin with the basic set of cards"
		loadDefaultCollection()
	else:
		for file in os.listdir(memCardDir):
			if os.path.exists(os.path.join(memCardDir, collectionChoice + ".txt")):
				loadCollection(collectionChoice)
				saveName = collectionChoice
				break

	print "Let's start the game!"
	collectionView = raw_input("Would you like to see your collection one more time (yes or no)?\n")
	print "\n"
	if collectionView.lower() == "yes": 
		printCollection()
		print "\n"

	#saveGame = raw_input("Would you like to save your progress?")
	#if saveGame.lower() == "yes": 
	#	saveCollection(saveName)
if __name__ == "__main__":
    main()