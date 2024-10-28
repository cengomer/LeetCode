from collections import deque
import string

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        
        # Convert the wordList to a set for O(1) lookups
        wordSet = set(wordList)
        
        # If endWord is not in the wordList, there is no valid transformation
        if endWord not in wordSet:
            return 0
        
        # Initialize BFS queue (word, transformation length)
        queue = deque([(beginWord, 1)])
        visited = set([beginWord])
        
        # BFS loop
        while queue:
            current_word, distance = queue.popleft()
            
            # If we reached the endWord, return the distance
            if current_word == endWord:
                return distance
            
            # Generate all possible neighbors (words that differ by one letter)
            for i in range(len(current_word)):
                for letter in string.ascii_lowercase:
                    neighbor = current_word[:i] + letter + current_word[i+1:]
                    
                    # If the neighbor is in wordSet and hasn't been visited
                    if neighbor in wordSet and neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, distance + 1))
        
        # If there's no valid transformation
        return 0