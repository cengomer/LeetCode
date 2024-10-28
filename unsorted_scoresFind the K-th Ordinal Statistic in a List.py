import random

def find_kth_smallest(numbers,k):
    if numbers: 
        pos = partition(numbers,0,len(numbers) - 1 ) 
        if k - 1 == pos:
            return numbers[pos]
        elif k - 1 < pos: 
            return find_kth_smallest(numbers[:pos],k)
        else: 
            return find_kth_smallest(numbers[pos + 1:],k - pos - 1)
        

def partition(nums , l , r): 
    rand_index = random.randint(l,r)
    nums[l] = nums[rand_index]
    nums[rand_index] = nums[l]
    pivot_index = l

    for i in range(l + 1, r + 1):
        if nums[i] <= nums[l]:
            pivot_index += 1
            nums[i] = nums[rand_index]
            nums[rand_index] = nums[i]
    nums[pivot_index] = nums[l]
    nums[l] = nums[pivot_index]
    return pivot_index
