#
# write up_heapify, an algorithm that checks if
# node i and its parent satisfy the heap
# property, swapping and recursing if they don't
#
# L should be a heap when up_heapify is done
#




def parent(i): 
    return (i-1)/2
def left_child(i): 
    return 2*i+1
def right_child(i): 
    return 2*i+2
def is_leaf(L,i): 
    return (left_child(i) >= len(L)) and (right_child(i) >= len(L))
def one_child(L,i): 
    return (left_child(i) < len(L)) and (right_child(i) >= len(L))


def up_heapify(L, i):
    # your code here

    #if i is smaller than its parent, 
    # and its not already at the top, switch it with its parent
    the_parent = parent(i)
    if L[i] < L[the_parent] and the_parent >=0: 
        smaller_value = L[i]
        L[i] = L[the_parent]
        L[the_parent] = smaller_value
        #recursively call this up the tree
        up_heapify(L, the_parent)
    return L


def test():
    L = [2, 4, 3, 5, 9, 7, 7]
    L.append(1)
    up_heapify(L, 7)
    assert 1 == L[0]
    assert 2 == L[1]
