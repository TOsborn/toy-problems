def spiralTraverse(array):
	"""Traverse a 2D array in a spiral.

	Flattens a two dimensional array. The order is created by 
	traversing the array in a clockwise spiral pattern starting
	at the top left corner (position (0, 0)).
	"""
	if array == [] or array[0] == []:
		return []
	
	loX, loY = 0, 0
	hiX, hiY = len(array) - 1, len(array[0]) - 1
	
	spiral = [array[0][0]]
	
	x, y = 0, 0
	dx, dy = 0, 1
	while loX <= hiX and loY <= hiY:
		while loX <= x + dx <= hiX and loY <= y + dy <= hiY:
			x, y = x + dx, y + dy
			spiral.append(array[x][y])
			
		if (dx, dy) == (0, 1):
			loX += 1
		elif (dx, dy) == (1, 0):
			hiY -= 1
		elif (dx, dy) == (0, -1):
			hiX -= 1
		else: # (dx, dy) == (-1, 0)
			loY += 1
		
		# 90 degrees right rotation
		dx, dy = dy, -dx
		
	return spiral
