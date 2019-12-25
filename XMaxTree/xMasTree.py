def printXmasTree(lengthOfTree):	
	firstNode = ""	
	otherNodes = ""
	starsToPrint = ""	
	for i in range(0,lengthOfTree):
		#to print top of the tree
		if i == 0:
			firstNode = concateSpaces(lengthOfTree - i)
			firstNode = firstNode + "*"
			print(firstNode)
		else:			
			otherNodes = concateSpaces(lengthOfTree - i)
			starsToPrint = starsToPrint = concateStars(totalStars(i))
			print(otherNodes+starsToPrint)
	#for trunck
	otherNodes = concateSpaces(lengthOfTree - 1)
	starsToPrint = starsToPrint = concateStars(totalStars(1))
	for i in range(3):
		print(otherNodes+starsToPrint)

		

def concateStars(noOfStars):
	stars = ""
	for i in range(noOfStars):
		stars = stars + "*"
	return stars

def concateSpaces(noOfSpaces):
	spaces = ""
	for i in range(noOfSpaces):
		spaces = spaces + " "
	return spaces

def totalStars(i):
	return (i+(i-1))+2

lengthOfTree = int(input("Enter the length of the tree : "))
printXmasTree(lengthOfTree)