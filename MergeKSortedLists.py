lists = [[1,4,5],[1,3,4],[2,6]]
stack_lists= []
for i in lists:
    for j in i:
        stack_lists.append(j)
sorted = sorted(stack_lists,key=int,reverse=False)
print (sorted)