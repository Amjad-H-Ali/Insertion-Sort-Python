print("Insertion Sort!")



array = [4, 2, 7, 96, 23, 45, 67, 3, 2, 3, 3, 9, 0, -1, 26, 0]

# Loop over Array starting from index one
for i in range(1, len(array)):
	# Store the index before the current element
	indx_B4 = i - 1