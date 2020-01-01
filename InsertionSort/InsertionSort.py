def insertionSort(s):
	for i in range(1,len(s)):
		j =  i - 1 		
		key  = s[i]
		while (j >= 0) and (s[j] > key):
			print(s,'j->',j,'i->',s[j],'>',s[i])			
			s[j+1] = s[j]
			j = j - 1			
		s[j+1] = key
			
	print(s)

insertionSort([7,5,3,2,4,1,0])