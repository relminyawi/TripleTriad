import sys
import cardInfo as ci

def getInfoByCardName(cardName):
	for card in ci.cards:
		if card["name"].strip() == cardName:
			print "name:      " + card["name"].strip()
			print "top:       " + card["stats"][0].strip()
			print "bottom:    " + card["stats"][1].strip()
			print "left:      " + card["stats"][2].strip()
			print "right:     " + card["stats"][3].strip()
			print "elemental: " + card["elemental"].strip()
			print "\n"

def main():
	# print command line arguments
    for arg in sys.argv[1:]:
        getInfoByCardName(arg)

if __name__ == "__main__":
    main()