class Solution(object):
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
        maximum_area = 0  # Initialize this outside the loop
        
        while left < right:  # Use < to stop when pointers meet
            width = right - left
            heigh = min(height[left], height[right])
            area = width * heigh
            
            # Update maximum_area if the current area is larger
            if area > maximum_area:
                maximum_area = area
            
            # Move the pointers
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return maximum_area  # Return the maximum area found