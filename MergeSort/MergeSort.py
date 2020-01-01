import math
def mergeSort(listOfElements):
	if len(listOfElements) < 2 :
		return listOfElements
	mid = math.floor(len(listOfElements)/2)
	# print('mid',mid)
	leftList = listOfElements[:mid]
	rightList = listOfElements[mid:]
	mergeSort(leftList)
	mergeSort(rightList)
	merge(leftList,rightList,listOfElements)

def merge(leftList,rightList,listOfElements):
	# print(leftList,rightList, listOfElements)
	i = 0
	j = 0
	k = 0
	nl = len(leftList)
	nr = len(rightList)
	print('Before->',leftList,rightList, listOfElements)
	while (i < nl) and (j < nr):
		if(leftList[i] > rightList[j]):
			listOfElements[k] = rightList [j]
			j = j + 1
		else:
			listOfElements[k] = leftList [i]
			i = i + 1
		k = k + 1		
	while i < nl :
		listOfElements[k] = leftList[i]
		i = i + 1
		k = k + 1
	while j < nr :
		listOfElements[k] = rightList[j]
		j = j + 1
		k = k + 1
	print('After->',leftList,rightList, listOfElements)

l = [3,2,1,7,0,1,1,2,2]
mergeSort(l)
print(l)
