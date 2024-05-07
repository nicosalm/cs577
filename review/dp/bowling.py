# Bowling

'''
Given n pins 0, 1, ..., n-1

- pin i has value v_i
- hit 1 pin i, get v_i points
- hit 2 pins i, i+1, get v_i * v_i+1 points
- can also never hit a pin
- max score

(1) Subproblem
    - B(i) = max score possible starting with pins {i, n-1}
(5) Original Problem
    - B(0)
(3) Recurrence
    - B(i) = max {  B(i+1),                     -- don't hit
                    B(i+1) + v_i,               -- hit 1 pin
                    B(i+2) + (v_i * v_i+1) }    -- hit 2 pins
    
    - Base case: B(n) = 0

    - Time: O(n) * O(1)     -- num subproblems * time per subproblem 

(4) Topological Ordering
    - Decreasing i order: n, n-1, ..., 0
'''

'''
Bottom up DP
    B(n) = 0                                    -- base case
    for i = n, n-1 ... 0:                       -- topo
    B(i) = max {    B(i+1),                     -- relate
                    B(i+1) + v_i,
                    B(i+2) + (v_i * v_i+1) }

    return B(0)                                 -- original problem

    -- DP is approximately "local brute force"
'''

def bowling(pins): 

    n = len(pins)
    B = [0] * (n+2) # dp array
    
    for i in range(n-1, -1, -1):
        
        no_pin = B[i + 1]
        one_pin = B[i + 1] + pins[i]
        two_pin = B[i + 2] + (pins[i] * pins[i + 1]) if (i + 1 < n) else 0

        B[i] = max(no_pin, one_pin, two_pin)

    return B[0]

pins = [3, 5, 8, 1, 6, -5, -1]
print("Maximum score:", bowling(pins))
