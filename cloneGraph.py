class Solution(object):
    def cloneGraph(self, node):
        if not node:
            return None 
        cloned_map = {}  
        queue = deque([node])  # Queue for BFS traversal
        cloned_map[node] = Node(node.val)  # Clone the initial node
        while queue:
            current_node = queue.popleft()
            # Iterate over each neighbor of the current node
            for neighbor in current_node.neighbors:
                if neighbor not in cloned_map:
                    # Clone the neighbor and add it to the cloned_map
                    cloned_map[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)  
                # Add the cloned neighbor to the neighbors list of the cloned node
                cloned_map[current_node].neighbors.append(cloned_map[neighbor])
                return cloned_map[node]