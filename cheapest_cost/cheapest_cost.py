
def get_cheapest_cost(rootNode):
    """
    Idea:
    - Initialize min_price = inf
    - Traverse the tree depth-first
    - Once children is None, we've reached the local dealership.
    - At this point, calculate the total price
    - Compare to global min, update if necessary
    """
    min_price = float('inf')

    def dfs(root, curr_cost):
        if not root.children:
            # Finalize prize
            if curr_cost < min_price:
            min_price = curr_cost
            return

        for child in root.children:
            dfs(child, curr_cost+child.cost)

    curr_cost = rootNode.cost
    dfs(rootNode, curr_cost)
    
    return min_price
     

########################################## 
# Use the helper code below to implement #
# and test your function above           #
##########################################
  
# A node 
class Node:

  # Constructor to create a new node
    def __init__(self, cost, children=[]):
        self.cost = cost
        self.children = children


root = Node(0, [
Node(5, 
[Node(4)]), 
Node(3, 
[Node(2, 
[Node(1, [Node(1)])]), 
Node(0, 
[Node(10)])]), 
Node(6, [
Node(1), 
Node(5)]
)])

print(get_cheapest_cost(root))