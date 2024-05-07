'''
Edit distance:

Given two strings x, y what is the cheapest sequence of character edits*
to turn x -> y 

* insert c, delete c, replace c -> c'

'''

'''
Longest common subsequence:

"HIEROGLYPHOLOGY"
"MICHAELANGELO"

LCS: "HELLO"

Drop any set of letters from x and y s.t. the two strings are equal
- Cost of insert/delete = 1
- Cost of replace c -> c' = { 0 if c = c' 
                              inf otherwise } 
'''

'''
(1) Subproblems
    Solve edit distance problem on two different strings:
    - on x[i:] & y[j:] for all i, j
    - # subproblems: theta |x| * |y| -> quadratic, O(n^2) if same len

(2) Guess
    Want to convert x into y, look at first characters (want to cut them
    off somehow) ... want first char in x to become first char in y.

    One of three possibilities:
        - replace x[i] -> y[j]
        - insert y[j] at beginning
        - delete x[i]

(3) Recurrence
    DP(i, j) = min(
        1. cost(replace(x[i] -> y[j]))
        + DP (i+1, j+1), 

        2. cost(insert(y[j]))
        + DP(i, j+1),

        3. cost(delete(x[i]))
        + DP(i+1, j) 

(4) Topological ordering:
    for i = |x| ... 0:
        for j = |y| ... 0:

    Matrix dimensions: 
    Y-axis: 0 ... i ... |x|
    X-axis: 0 ... j ... |y|

    Computing A[i,j] requires:  DP[i+1,j],  -- cost of deletion
                                DP[i,j+1],  -- cost of insertion
                                DP[i+1,j+1] -- cost of replace

                                (see (3))
(5) DP(0, 0)

Running time:
    O(1) * O(|x| * |y|) -- time/subproblem * # subproblems
'''

def edit_dist(x, y):

    # table to store subproblems
    dp = [[0 for _ in range(len(y) + 1)] for _ in range(len(x) + 1)]

    # initialize last row, column of dp table
    for i in range(len(x) + 1):
        dp[i][len(y)] = len(x) - i
    for j in range(len(y) + 1):
        dp[len(x)][j] = len(y) - j

    # fill dp[][] from bottom up
    for i in range(len(x) - 1, -1, -1):
        for j in range(len(y) -1, -1, -1):
            if x[i] == y[j]:
                dp[i][j] = dp[i+1][j+1]

            else:
                dp[i][j] = 1 + min(dp[i+1][j],
                                   dp[i][j+1],
                                   dp[i+1][j+1])

    return dp[0][0]

def LCS(x, y):
    dp = [[0 for _ in range(len(y) + 1)] for _ in range(len(x) + 1)]

    # build the dp array from bottom up
    for i in range(1, len(x) + 1):
        for j in range(1, len(y) + 1):
            if x[i - 1] == y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1  # characters match
            else:
                # take max of excluding current char from x or y
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # dp[len(x)][len(y)] contains the length of LCS for x[0..n-1], y[0..m-1]
    return dp[len(x)][len(y)]

x = "HIEROGLYPHOLOGY"
y = "MICHAELANGELO"
print("Edit Distance:", edit_dist(x, y))
print("Length of LCS:", LCS(x, y))
