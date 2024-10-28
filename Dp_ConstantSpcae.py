def fib(self , n: int) -> int: 
    if n == 0:
        return 0
    
    if n == 1:
        return 1

    prev = 0
    cur = 1

    for i in range(2 , n+1):
        prev , cur = cur , prev+cur
        # at the same time it updates prev to be cur 
        # and cur to be cur + prev these essentially always 
        # keeps cur as the new number which is the sum of the prev 2 
        # and also always keep prev as the one  behind and the end of these 
        # you would just return cur 
    
    return cur

    # Time Complexity  = O(n)
    # Space Complexity = O(1)