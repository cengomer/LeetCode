# Mapping friends to numbers for simplicity: Alice: 0, Bob: 1, Carol: 2
n = 3  # number of friends
M = [[0] * n for _ in range(n)]  # Adjacency Matrix

# Alice is friends with Bob and Carol
M[0][1] = M[0][2] = 1
M[1][0] = M[2][0] = 1

# Print the matrix
for row in M:
    print(row)

# Output:
# [0, 1, 1]
# [1, 0, 0]
# [1, 0, 0]