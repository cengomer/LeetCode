def binary_search_iterative(data,target):
    low = 0
    high = len(data)

    while high - low > 1:
        mid = (low + high) // 2
        if target < data[mid]:
            high = mid
        else:
            low = mid
    return low if data[low] == target else None