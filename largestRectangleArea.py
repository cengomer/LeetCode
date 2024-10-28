class Solution(object):
    def largestRectangleArea(self, heights):
        stack = []
        max_area = 0
        
        for i ,height in enumerate(heights):
            while stack and height < heights[stack[-1]]:
                idx = stack.pop()
                h = heights[idx]

                width = i if not stack else i - stack[-1] - 1

                max_area = max(max_area, h * width)

            stack.append(i)

        
        while stack:
            idx = stack.pop()
            h = heights[idx]
            width = len(heights) if not stack else len(heights) - stack[-1] - 1
            max_area = max(max_area, h * width)

        return max_area
        