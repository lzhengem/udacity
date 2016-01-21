#
# Write partition to return a new array with 
# all values less then `v` to the left 
# and all values greater then `v` to the right
#

def partition(L, v):
    P = [v]
    # your code here
    for value in L:
    	if value < v:
    		P.insert(0, value)
    	elif value > v:
    		P.append(value)
    return P

def rank(L, v):
    pos = 0
    for val in L:
        if val < v:
            pos += 1
    return pos



