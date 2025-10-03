import numpy as np

def spiral(n, m):
	left, top, bottom, right = 0, 0, n, m
	res = np.zeros((n,m))
	
	num = 1
	while left < right and top < bottom:
		res[top, left:right] = np.arange(num, num + right - left)
		num += right - left
		top += 1
	
		res[top:bottom, right-1] = np.arange(num, num + bottom - top)
		num += bottom - top
		right -= 1
		
		if not (left < right and top < bottom):
			break
			
		res[bottom - 1, left:right][::-1] = np.arange(num, num + right - left)
		num += right - left
		bottom -= 1
		
		res[top:bottom, right-1][::-1] = np.arange(num, num + bottom - top)
		num += bottom - top
		left += 1
	
	return res

inp = [int(i) for i in input().split()] #ну, это если значения вводятся в строку через пробел.
print(spiral(inp[0],inp[1]))
