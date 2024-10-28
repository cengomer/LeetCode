def search_rotated_array(nums,target):
    start,end = 0,len(nums) - 1
    
    while start <= end:
        mid = (start + end) // 2

        if nums[mid] == target:
            return mid
        
        if nums[start] <= nums[mid]:
            #left half is sorted
            if nums[start] <= target < nums[mid]:
                end = mid - 1 #Target is in the left half
            else:
                start = mid + 1 #Target is in the right half
        
        else:
            #right half is sorted
            if nums[mid] < target <= nums[end]:
                start = mid + 1 # Target is in the right half
            else:
                end = mid - 1  # Target is in the left half

    return -1 # Target not found




