
import heapq
import math

def a_aster(s_0, neighbors_function, goal_test_function, step_cost_function, h_cost_function):
    # Implements the A* algorithm
    #
    # Explored and Frontier states are keept sets following the same names respectively, so
    # no state appears twice in any of these conditions.
    #
    # The costs information is kept in a heap, is faster to pull out the next state to move to
    # from the frontier state. By using a min heap (priority queue) we perform this operation
    # in O (log n)
    #
    # A dictionary is used to build the final path, every time a state is added to the explored
    # set, an entry is created storing the state and its previous state, this way we have all
    # the information needed to build the final path
    explored, frontier = set(), set([s_0])
    costs = [(h_cost_function(s_0), s_0, 0, None)]
    neighbor_from = {}
    
    while frontier:
        # While there are states in the frontier, use the next state with minimum cost.
        _, id_, g_cost, from_ = heapq.heappop(costs)
        
        # If such state was already reached via a different path, move to the next minimum state.
        if id_ in explored:
            continue
            
        # Makes this new state an explored state.
        explored.add(id_)
        neighbor_from[id_] = from_

        # If the new state complies with the goal test, it means we reached the final state,
        # then we build the path and return it.
        if goal_test_function(id_):
            path = []
            while id_ is not None:
                path.append(id_)
                id_ = neighbor_from[id_]
            return path[::-1]
        
        # Iterates through each of the next (neighbors) states could be reached from the
        # current state and add them to the frontier set if they haven't been reached before.
        for neighbor in neighbors_function(id_):
            if neighbor in explored:
                continue

            frontier.add(neighbor)
            new_g_cost = g_cost + step_cost_function(id_, neighbor)
            new_h_cost = h_cost_function(neighbor)
            new_f_cost = new_g_cost + new_h_cost
            heapq.heappush(costs, (new_f_cost, neighbor, new_g_cost, id_))
            
    # Raise an exception if no path was ever found.
    raise Exception("Sorry, no path were found")      

def shortest_path(M,start,goal):
    
    # Used as the actions functions in the A* algorithm, it returns the new states s' 
    # that could be reached from the current state.
    neighbors_function = lambda x: M.roads[x]

    # The goal test function defined in the A* algorithm, it's true if the state
    # is equal to the goal intersecition and false otherwise
    goal_test_function = lambda x: x == goal
    
    # Euclidean distance, is the step cost function used in the A* algorithm.
    # It means that the cost from moving from intersection a to b is going to
    # be the Euclidean distance between the two coordinates.
    # sqrt((Y2 - Y1)^2 + (X2 - X1)^2)
    step_cost_function = lambda a, b: math.sqrt((M.intersections[b][1] - M.intersections[a][1]) ** 2 + (M.intersections[b][0] - M.intersections[a][0]) ** 2)
    
    # The heuristic function (direct estimate) is defined as the direct Euclidean
    # distance between the current intersection and the goal intersection.
    # It's guaranteed that this is an admissible or optimistic heuristic as the
    # direct distance won't never be bigger than the the distance following a valid
    # path through roads as the direct distance will always be the minimum possible distance
    # between any intersection.
    h_cost_function = lambda x: step_cost_function(x, goal)
    
    return a_aster(start, neighbors_function, goal_test_function, step_cost_function, h_cost_function)