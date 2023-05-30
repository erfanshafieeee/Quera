def hamneheshti( X, Y):
	
	n = max(X, Y)

	for i in range(2, n + 1):

		if (X % i == Y % i):
			print(i,end=" ")

X, Y = map(int, input().split())
hamneheshti(X, Y)