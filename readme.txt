# Ramy Elminyawi
# FFVIII Triple Triad
# Info/Notes/Whatever I need to keep track of

# Cards are split up into levels with 11 cards per level (110 total)
## Level 01
## Level 02
## Level 03
## Level 04
## Level 05
## Level 06
## Level 07
## Level 08
## Level 09
## Level 10

# Cards have the following information

## Four stats indicating "strength values"
### Top 
### Left
### Right
### Bottom

## Elemental
### None
### Thunder
### Earth
### Ice 
### Wind
### Poison
### Fire
### Water
### Holy

# Dictionary of cards will look as follows
## card = {'name': 'Geezard', 'elemental': 'None', 'stats': ['1',  '5',  '4',   '1']}
## 															(top, left, right, bottom)

# Things that need to happen still
## Implement basic game functionality
### 5 cards in hand
### 3x3 playing grid
### Higher value on playing face wins
### 2 players
### Visuals will look like
#### Turn 1: P1 plays Blobra 
####  ________
     | 1|  |  |  1 = Blobra
#### |__|__|__|
#### |__|__|__|
#### |__|__|__|
####
#### Turn 2: P2 plays Bite Bug 
####  ________
     | 1|  | 2|  1 = Blobra
#### |__|__|__|  2 = Bite Bug
#### |__|__|__|
#### |__|__|__|
####
### Player input will be of form (cardName, position) where position on grid is 1-9 as follows
####
####  1 2 3
####  4 5 6
####  7 8 9
####
## Implement game modes
## Implement ability to store persistent users collection
## Implement AI
##
##