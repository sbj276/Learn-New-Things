def printXmasTreeWithTier(lengthOfTree,noOftiers):
	firstTierNode = lengthOfTree + 1
	extraSpaces = 0
	for i in range(0,noOftiers):
		extraSpaces =  (noOftiers - i) + 1 
		printXmasTree(lengthOfTree+i,extraSpaces)

	#for trunck
	otherNodes = concateSpaces(lengthOfTree+noOftiers)
	starsToPrint = starsToPrint = concateStars(totalStars(1))
	for i in range(3):
		print(otherNodes+starsToPrint)


def printXmasTree(lengthOfTree,extraSpaces):
	firstNode = ""	
	otherNodes = ""
	starsToPrint = ""	
	for i in range(0,lengthOfTree):
		#to print top of the tree
		if i == 0:
			firstNode = concateSpaces((lengthOfTree - i)+extraSpaces)
			firstNode = firstNode + " * "
			print(firstNode)
		else:			
			otherNodes = concateSpaces((lengthOfTree - i)+extraSpaces)
			starsToPrint = starsToPrint = concateStars(totalStars(i))
			print(otherNodes+starsToPrint)
	# #for trunck
	# otherNodes = concateSpaces(lengthOfTree - 1)
	# starsToPrint = starsToPrint = concateStars(totalStars(1))
	# for i in range(2):
	# 	print(otherNodes+starsToPrint)

def concateStars(noOfStars):
	stars = ""
	for i in range(noOfStars):
		stars = stars + " * "
	return stars

def concateSpaces(noOfSpaces):
	spaces = ""
	for i in range(noOfSpaces):
		spaces = spaces + "   "
	return spaces

def totalStars(i):
	return (i+(i-1))+2

noOftiers = int(input("Enter the Number of Tiers : "))
lengthOfTree = int(input("Enter the length of the tree : "))
printXmasTreeWithTier(noOftiers,lengthOfTree)