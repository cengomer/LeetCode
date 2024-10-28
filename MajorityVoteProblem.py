def MajorityVoteProblem(listA):
    count_dict = {}
    for element in listA:
        count_dict[element] = count_dict.get(element,0) + 1
        if count_dict[element] > len(listA) // 2:
            return element