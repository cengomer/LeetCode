def rob(self,nums):
    if len(nums) == 0 : 
        return 0 
    if len(nums) == 1 :
        return nums[0]
    if len(nums) == 2 : 
        return max(nums[0],nums[1])
    
    memo = {0 : nums[0] , 1 : max(nums[0] , nums[1])}

    def f(x):
        if x in memo:
            return memo[x]
        else:
            memo[x] = max(f(x - 1) , f(x - 2) + nums[x])
            return memo[x]
    
    return f(len(nums - 1 ))


