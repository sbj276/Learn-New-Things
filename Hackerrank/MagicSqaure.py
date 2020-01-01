def formingMagicSquare(s):
	for i in range(3):		
		if sum(s[i]) != 15:
			print(s[i])



s = []
for _ in range(3):
	s.append(list(map(int, input().rstrip().split())))
formingMagicSquare(s)