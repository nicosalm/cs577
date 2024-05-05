
# parenthesization

# recurrence: DP(i, j) 
#       = min (i + 1 ≤ k < j) { DP (i, k) + DP(k, j) + cost
#           + cost of (Ai:k) * (Ak:j) } 

# time: theta n^3

import sys

def MatrixChainOrder(p, i, j):
    if i == j:
        return 0
 
    _min = sys.maxsize
 
    # Place parenthesis at different places
    # between first and last matrix, 
    # recursively calculate count of multiplications 
    # for each parenthesis placement 
    # and return the minimum count
    for k in range(i, j):
 
        count = (MatrixChainOrder(p, i, k)
                 + MatrixChainOrder(p, k + 1, j)
                 + p[i-1] * p[k] * p[j])
 
        if count < _min:
            _min = count
 
    # Return minimum count
    return _min

if __name__ == '__main__':
    arr = [1, 2, 3, 4, 3]
    N = len(arr)
     
    print("Minimum number of multiplications is ",
      MatrixChainOrder(arr, 1, N-1))
