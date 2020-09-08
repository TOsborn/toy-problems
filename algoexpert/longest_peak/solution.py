def longestPeak(array):
	"""Finds the longest peak within an array."""
	if array == []:
		return 0
	
	maxPeak = 1
	peakLength = 1
	hasFlipped = False
	for i in range(1, len(array)):
		if not hasFlipped:
			if array[i-1] < array[i]:
				peakLength += 1
			elif array[i-1] > array[i]:
				hasFlipped = True
				peakLength += 1
			else:
				assert(array[i-1] == array[i])
				peakLength = 1
		elif array[i-1] > array[i]:
			peakLength += 1
		elif array[i-1] < array[i]:
			hasFlipped = False
			peakLength = 2
		else:
			assert(array[i-1] == array[i])
			hasFlipped = False
			peakLength = 1
			
		print(array[i], i, peakLength, hasFlipped)
			
		maxPeak = max(peakLength, maxPeak)
		
	return maxPeak