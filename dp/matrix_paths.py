# matrix_paths.py

def matrix_paths_recursive(m, n, i, j):
    # base case
    if i == m - 1 and j == n - 1:
        return 1
    # recurse into cells to the right and below if within bounds
    count = 0
    if i+1 < m:
        count += matrix_paths_recursive(m, n, i+1, j)
    if j+1 < n:
        count += matrix_paths_recursive(m, n, i, j+1)
    return count

print matrix_paths_recursive(10, 10, 0, 0)

def matrix_paths(m, n):
    # initialize m by n matrix
    counts = [[0 for i in range(m)] for j in range(n)]
    # set first row and first column to all 1's
    for i in xrange(m):
        counts[i][0] = 1
    for j in xrange(n):
        counts[0][j] = 1
    # compute count of remaining cells, by adding
    # the count of the cell to the left and above.
    for i in xrange(1, m):
        for j in xrange(1, n):
            counts[i][j] = counts[i-1][j] + counts[i][j-1]
    return counts[m-1][n-1]

print matrix_paths(100, 100)

