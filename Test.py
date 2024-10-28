def anagrams(list1, list2):
    sorted_tuples_1 = set(tuple(sorted(word)) for word in list1)
    sorted_tuples_2 = set(tuple(sorted(word)) for word in list2)

    common_tuples = sorted_tuples_1 & sorted_tuples_2

    list_1_output = [word for word in list1 if tuple(sorted(word)) in common_tuples]
    list_2_output = [word for word in list2 if tuple(sorted(word)) in common_tuples]

    output = []

    for word1 in list_1_output:
        for word2 in list_2_output:
            if tuple(sorted(word1)) == tuple(sorted(word2)):
                output.append((word1,word2))

    return output

anagrams(list1=["omer","elmas","abdul","omer"] , list2=["moh","omer","morsi","abdul"])
