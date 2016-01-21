#finds the top k using recursion
# List of distinct two-digit values.
# Where will 84 be located in the sorted version?
#
import random

L = [31, 45, 91, 51, 66, 82, 28, 33, 11, 89, 27, 36]

#separates out the left side and right side of v
def partition(L, v):
    smaller = []
    bigger = []
    for val in L:
        if val < v: smaller += [val]
        if val > v: bigger += [val]
    return (smaller, [v], bigger)

print partition(L, 84)
# >>>[31, 45, 51, 66, 82, 28, 33, 11, 27, 36, 84, 91, 89]

def top_k(L, k):
    v = L[random.randrange(len(L))]
    (left, middle, right) = partition(L, v)
    # middle used below (in place of [v]) for clarity
    #if v is at the edge or one more of the edge of K, then everything to the left
    # of v is in the top k
    if len(left) == k:   return left
    if len(left)+1 == k: return left + middle
    #if v is to the right of K, then keep cutting down L until we narrow it down to K
    if len(left) > k:    return top_k(left, k)
    #if v is in k (to the left), then everything to the left
    #of v is in k, then recurse on the rest of L
    return left + middle + top_k(right, k - len(left) - len(middle))

print top_k(L, 5)
# >>> [31, 28, 33, 11, 27]
# list order may vary due to random selection of v