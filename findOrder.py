from collections import defaultdict

class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        # Create a graph from prerequisites
        graph = defaultdict(list)
        for course, pre in prerequisites:
            graph[pre].append(course)
        
        visited = set()  # To track visited courses
        rec_stack = set()  # To detect cycles
        visited_order = []  # To store the order of courses

        def dfs(course):
            if course in rec_stack:  # Cycle detected
                return False
            if course in visited:  # Already visited, no need to process again
                return True
            
            rec_stack.add(course)  # Add to recursion stack
            
            # Visit all neighbors (courses that depend on this course)
            for nei in graph[course]:
                if not dfs(nei):
                    return False  # If cycle detected in neighbor
            
            rec_stack.remove(course)  # Remove from recursion stack
            visited.add(course)  # Mark course as visited
            visited_order.append(course)  # Append to order after visiting all dependencies
            
            return True

        # Start DFS for each course
        for course in range(numCourses):
            if course not in visited:
                if not dfs(course):  # If a cycle is found
                    return []  # Return empty if impossible to finish

        # Reverse the order to get correct topological sorting
        return list(reversed(visited_order))