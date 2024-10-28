class Solution(object):
    def dailyTemperatures(self, temperatures):
        stack = []
        result =[0] * len(temperatures)

        for i,temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                idx = stack.pop()
                result[idx] = i - idx
            stack.append(i)
        return result