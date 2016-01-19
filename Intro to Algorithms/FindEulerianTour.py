# Find Eulerian Tour
#
# Write a function that takes in a graph
# represented as a list of tuples
# and return a list of nodes that
# you would follow on an Eulerian Tour
#
# For example, if the input graph was
# [(1, 2), (2, 3), (3, 1)]
# A possible Eulerian tour would be [1, 2, 3, 1]

#look at the rest of the graph and sees what the next tuple is, given the connecting point
def find_next_tup(secondPoint, graph):
    for point in graph:
        if secondPoint in point:
            return point

#given the tuple and the leading point, find the next connecting point
def find_next_point(firstPoint, nextTup):
    pointA, pointB = nextTup
    if firstPoint == pointA:
        return pointB
    else:
        return pointA

def find_eulerian_tour(graph):
    # your code here
    tour = []
    firstPoint, secondPoint = graph.pop(0) #get the first tuple
    tour.append(firstPoint)
    tour.append(secondPoint)

    while len(graph) > 0: #if there are still tuples in graph, keep adding to the tour
        secondTup = find_next_tup(secondPoint,graph)
        graph.remove(secondTup)
        secondPoint = find_next_point(secondPoint, secondTup)
        tour.append(secondPoint)
    if secondPoint == firstPoint:
        #if the first point and the last point matches,then it has successfuly found a Eularien tour
        return tour
    else:
        print("oh no failed")

#test it
find_eulerian_tour([(1, 2), (2, 3), (3, 1)])