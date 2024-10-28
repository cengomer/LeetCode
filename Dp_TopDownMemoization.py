"""
so the top-down dp memoization is acctuly 
let say we have something like a tree and the right hand we have Function(3)
and on the left hand we have also Function in somewhare its doesnot have be at
same range so the thing is when our codes find the answer of te Function(3)
its doesnot have to calculate that Function(3) again when he see it on the left side
so that saves us a nice time
"""

"so we will apply the memoiziation on a fibonnaci problem"

def fib(self,n:int) -> int:
    memo = {0:0, 1:1}

    def f(x):
        if x in memo:
            return memo[x]
        else:
            memo[x] = f(x-1) + f(x-2)
            return memo[x]
    
    return f(n)
# Time Complexity :  O(n)
# Space Complexity:  O(n)