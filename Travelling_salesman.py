def solve_tsp(G):
    
    allNodes = len(G) #Stores all nodes in graph as numbers ranging from 0 (starter node) to the size of the graph - 1
    route = [] #Saves the route traveled by the end of the algorithm
    visited = [False] * allNodes #Tracks nodes visited (used to decide next node to check later)
    
    #Makes sure first node is marked in output
    currentNode = 0
    route.append(currentNode)
    visited[currentNode] = True
    
    #Iterate through each node. Choose the closest neighbor each time
    for i in range(allNodes - 1):

        #Initializing variables to be used in next loop
        nearestNeighbor = None
        currentClosestNode = float('inf')
        
        #Checks all neighboring nodes to find shortest unvisited route
        for neighbor in range(allNodes):
            if not visited[neighbor] and G[currentNode][neighbor] < currentClosestNode:
                nearestNeighbor = neighbor
                currentClosestNode = G[currentNode][neighbor]
        
        #Go to next node
        currentNode = nearestNeighbor
        route.append(currentNode)
        visited[currentNode] = True
    
    #Hack fix to always end in loop
    route.append(route[0])
    
    return route