def non_repeating_elements(nums):
    seen, repeated = set(), set()
    for num in nums:
        if num in seen:
            repeated.add(num)
        else: 
            seen.add(num)
    print(repeated)
    print(seen)
    return list(seen - repeated)

non_repeating_elements([1,2,3,4,5,6,32,1,3,4,43,234])

def unique_elements(list1,list2):
    set1 = set(list1)
    set2 = set(list2)
    unique_to_1 = sorted(list(set1 - set2))
    unique_to_2 = sorted(list(set2 - set1))
    return (unique_to_1,unique_to_2)