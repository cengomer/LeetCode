from collections import deque

# Represents the forest as a dictionary
forest = {
    'Amazon_Rainforest': ['Congo_Basin', 'Southeast_Asian_Rainforests'],
    'Congo_Basin': ['Guinea_Rainforests', 'New_Guinea_Rainforests'],
    'Southeast_Asian_Rainforests': ['Sundaland_Rainforests', 'Wallacea_Rainforests'],
    'Guinea_Rainforests': [],
    'New_Guinea_Rainforests': ['Papua_New_Guinea_Rainforests'],
    'Sundaland_Rainforests': [],
    'Wallacea_Rainforests': ['Celebes_Rainforests'],
    'Papua_New_Guinea_Rainforests': [],
    'Celebes_Rainforests': []
}

def BFS(forest, root='Amazon_Rainforest'):
    ''' BFS algorithm to visit all forests '''
    queue = deque()  # Queue to hold forest regions
    queue.append(root)  # Starting search from root
    visited = []  # List to hold visited forests

    while queue:
        current_forest = queue.popleft()
        visited.append(current_forest)  # Mark current forest as visited

        # Queuing the forests not yet visited
        if current_forest in forest:
            for neighbouring_forest in forest[current_forest]:
                if neighbouring_forest not in visited:
                    queue.append(neighbouring_forest)
    
    return visited

print(' -> '.join(BFS(forest, root='Amazon_Rainforest')))  # Using Amazon Rainforest as root