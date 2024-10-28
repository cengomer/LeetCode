class Solution(object):
    def generateParenthesis(self, n):
        res = []
        def backtrack(current_str,openP,closeP):
            if openP ==0 and closeP == 0:
                res.append(current_str)
                return
            
            if openP > 0:
                backtrack(current_str + '(', openP - 1,closeP)

            if closeP > openP :
               backtrack(current_str + ')', openP,closeP - 1)
        
        backtrack('',n,n)
        return res