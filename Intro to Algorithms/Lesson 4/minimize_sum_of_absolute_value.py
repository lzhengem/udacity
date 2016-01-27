#
# Given a list of numbers, L, find a number, x, that
# minimizes the sum of the absolute value of the difference
# between each element in L and x: SUM_{i=0}^{n-1} |L[i] - x|
# 
# Your code should run in Theta(n) time
#



def minimize_absolute(L):
    L.sort()
    l_length = len(L)
    if l_length % 2 ==1: #if L is odd, then return the median
    	return L[int(l_length/2)]
    else: #if L is even, then the median is the average of the 2 numbers in the middle
    	return (L[int(l_length/2.0 - 1)]   +  L[int(l_length/2.0)] )/2.0
    