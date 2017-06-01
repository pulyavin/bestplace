def findMissing(arr):
	sub = 0
	for i in range(len(arr)):
		sub += (arr[i]+1) - arr[i]

	return sub