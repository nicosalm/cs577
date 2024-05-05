
# knapsack dp

'''
Knapsack:
    List of items 0 ... i ... n
        - each has size si -> Int
        - each has value vi -> Int

    Knapsack of total size S:
        1. Want to maxmimize the sum of the values for a subset of items
        1. Need subset of items whose total size ≤ S
    
    (2) Guessing:
        Is item i in the subset or not? (2 choices)
            1. Yes
            2. No

    (1) Subproblem => suffix i: of items & remaining capacity
        # subproblems = theta n * S

    (3) Recurrence
        DP(i, X) = max { DP(i+1, X), DP(i+1, X-si) + vi } 

    (5) DP(n, S)
        time = theta n * S -> not polynomial time; pseudopolynomial
'''

def knapsack(items, S):
    n = len(items)
    dp = [[0 for _ in range(S + 1)] for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        size, value = items[i-1]
        for x in range(S + 1):
            # option 1: don't take an item
            dp[i][x] = dp[i-1][x]

            # option 2: take the item if it fits
            if x >= size:
                dp[i][x] = max(dp[i][x], dp[i-1][x - size] + value)

    return dp[n][S]

items = [(10, 60), (20, 100), (30, 120)]  # Each item is a tuple (size, value)
capacity = 50
print("Maximum value in knapsack:", knapsack(items, capacity))
