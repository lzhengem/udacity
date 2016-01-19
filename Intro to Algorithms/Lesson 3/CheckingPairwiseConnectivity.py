##################################################################
# Traversal...
# Call this routine on nodes being visited for the first time
#use mark_component to find if v1 is connected to v2
def mark_component(G, node, marked):
    marked[node] = True
    total_marked = 1
    for neighbor in G[node]:
        if neighbor not in marked:
            total_marked += mark_component(G, neighbor, marked)
    return total_marked

#G = {a:{g:1, d:1},g:{a:1,d:1,c:1},c:{g:1},d:{a:1, g:1}, b:{f:1},f:{b:1, e:1},e:{f:1,h:1}, h:{e:1}}
#v1="a"
#v2="c"
def check_connection(G, v1, v2):
    # Return True if v1 is connected to v2 in G
    # or False if otherwise
    #write your code here

    marked = {}
    #as mark_component runs, it will add all the nodes into marked. so then you can check if the node v2 is in marked
    mark_component(G, v1, marked)
    return v2 in marked
    
def make_link(G, node1, node2):
    if node1 not in G:
        G[node1] = {}
    (G[node1])[node2] = 1
    if node2 not in G:
        G[node2] = {}
    (G[node2])[node1] = 1
    return G

def test():
    edges = [('a', 'g'), ('a', 'd'), ('g', 'c'), ('g', 'd'), 
             ('b', 'f'), ('f', 'e'), ('e', 'h')]
    G = {}
    for v1, v2 in edges:
        make_link(G, v1, v2)
    assert check_connection(G, "a", "c") == True
    assert check_connection(G, 'a', 'b') == False
    


