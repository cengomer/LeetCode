def sort_tuples_ties(values):
    return values.sort(key=lambda x: (x[1], x[0]))

# This code will now sort the values list, first sorting
# by the x[1] value and, in case of a tie, sorting by the x[0] value.


def sort_tuples(tuples):
    return sorted(tuples, key=lambda x: x[1])

# The lambda function x: x[1] takes an element from tuples and returns its second element
# (i.e., x[1]). The sorted() function uses these second elements to sort the tuples.