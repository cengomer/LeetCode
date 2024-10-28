class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # Initialize parent array where par[i] is the parent of node i
        par = [i for i in range(len(edges) + 1)]
        
        # Initialize rank array for union by rank, where rank[i] indicates the size of the tree
        rank = [1] * (len(edges) + 1)

        # Find function to find the root of the set that contains node n
        def find(n):
            p = par[n]
            # Path compression: flatten the structure to speed up future queries
            while p != par[p]:
                par[p] = par[par[p]]  # Point node's parent to the grandparent
                p = par[p]
            return p  # Return the root parent

        # Union function to connect two nodes n1 and n2
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)  # Find the roots of both nodes
            
            if p1 == p2:
                # If both nodes have the same root, they are already connected
                return False
            
            # Union by rank: attach the smaller tree under the root of the larger tree
            if rank[p1] > rank[p2]:
                par[p2] = p1  # Set parent of p2 to p1
                rank[p1] += rank[p2]  # Update the rank
            else:
                par[p1] = p2  # Set parent of p1 to p2
                rank[p2] += rank[p1]  # Update the rank

            return True  # Successfully connected the two components

        # Iterate over all edges to process unions
        for n1, n2 in edges:
            # If union returns False, it means adding this edge creates a cycle
            if not union(n1, n2):
                return [n1, n2]  # Return the edge that creates the cycle