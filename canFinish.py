from collections import defaultdict

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        # Step 1: Build graph (adjacency list)
        graph = defaultdict(list)
        for course, pre in prerequisites:
            graph[pre].append(course)

        visited = set()
        rec_stack = set()

        def dfs(course):
            # If course is in the recursion stack, we found a cycle
            if course in rec_stack:
                return False
            
            # If course is already fully processed, skip it
            if course in visited:
                return True

            # Mark course as visited and add to recursion stack
            rec_stack.add(course)

            # Visit all neighbors
            for neighbor in graph[course]:
                if not dfs(neighbor):
                    return False

            # Remove from recursion stack and add to visited set
            rec_stack.remove(course)
            visited.add(course)
            return True
        # Step 2: Check each course for cycles
        for course in range(numCourses):
            if course not in visited:
                if not dfs(course):
                    return False

        return True