
# Prints out the clue, with what we know at the top 
# followed by the remaining characters (with each
# character on their own line repeated for as many times as 
# it appears
def printClue(wwk,d):
  print "What we know"
  print wwk + "\n"
  print "Remaining Characters:"
  for key, value in sorted(d.items()):
    if value > 0:
      keyline = ""
      for index in range(value):
        if key == "\n":
          keyline+= "\\n"
        else:
          keyline += key
      print keyline
    elif value < 0:
      print "Warning: character '"+key+"' used too many times in given WhatWeKnow"

# Given a sting, constructs a dictionary with keys
# being a character and values being the # of occurances
def readClue(clueStr):
  d = {}
  for i in clueStr:
    if not d.has_key(i):
      d[i]=1
    else:
      d[i] = d[i] + 1
  return d

# Takes a clue dictionary and a what we know dictionary
# and decrements the character counts of clue by the amount
# listed in wwk
def updateClue(clue, wwk):
  for key, value in sorted(wwk.items()):
    clue[key] = clue[key] - 1
  return clue

# First read in the clue and what we know
obj = open("clue.txt")
clue=obj.read()
wwkobj = open("whatweknow.txt")
wwk = wwkobj.read()

# Convert clue and wwk to dictionaries
dClue = readClue(clue)
dWWK = readClue(wwk)
dClue = updateClue(dClue, dWWK)

# And then print out the result
printClue(wwk,dClue)
     
