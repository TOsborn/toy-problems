# solution.py

from typing import List

def getNthFib(n):
    if n == 1:
        return 0
	
    a, b = 0, 1
    for _ in range(n-2):
        a, b = b, a+b

    return b
