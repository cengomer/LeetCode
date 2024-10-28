def binary_search_recursive(data, target, low, high):
    if high - low <= 1:
        return low if data[low] == target else None
    mid = (low + high) // 2
    if target < data[mid]:
        return binary_search_recursive(data, target, low, mid)
    else:
        return binary_search_recursive(data, target, mid, high)