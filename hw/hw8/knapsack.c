// knapsack problem in c

/**
* @file knapsack.c
* @brief C program for the knapsack problem
*
* This program is a C implementation of the knapsack problem in O(nW)
*
* @see https://en.wikipedia.org/wiki/Knapsack_problem
*
* The input will start with a positive integer, giving the number of instances
* which follow. For each instance, there will be two non-negative integers,
* representing the number of items and the capacity of the knapsack, followed
* by a list describing each item. Each item is described by two non-negative
* integers, the first giving the weight of the item and the second giving the
* value of the item. The output will be the maximum value that can be obtained
* by taking a subset of the items such that the sum of their weights is less
* than or equal to the capacity of the knapsack.
*/

// Sample input:
// 2
// 1 3
// 4 100
// 3 4
// 1 2
// 3 3
// 2 4

/**
 * The sample input has two instances. The first instance has one item and
 * a capacity of 3. The item has a weight of 4 and a value of 100. The second
 * The second instance has three items and a capacity of 4. For each instance,
 * the output will be the maximum value:
*/

// Sample output:
// 0
// 6

#include <stdio.h>
#include <stdlib.h>

int max(int a, int b) {
    return (a > b) ? a : b;
}

int knapsack(int W, int wt[], int val[], int n) {
    int i, w;
    // 2D array to store the maximum value that can be obtained
    int **dp = (int **)malloc((n + 1) * sizeof(int *));
    for (i = 0; i <= n; i++) {
        dp[i] = (int *)malloc((W + 1) * sizeof(int));
    }

    // build table dp[][] in a bottom-up manner
    for (i = 0; i <= n; i++) {
        for (w = 0; w <= W; w++) {
            if (i == 0 || w == 0) {
                dp[i][w] = 0;
            } else if (wt[i - 1] <= w) {
                dp[i][w] = max(val[i - 1] + dp[i - 1][w - wt[i - 1]], dp[i - 1][w]);
            } else {
                dp[i][w] = dp[i - 1][w];
            }
        }
    }

    // store the result
    int result = dp[n][W];
    for (i = 0; i <= n; i++) {
        free(dp[i]);
    }
    free(dp);

    return result;
}

int knapsackOptimized(int W, int wt[], int val[], int n) {
    int w;
    // 1D array to store the maximum value that can be obtained with weight w
    int *dp = (int *)malloc((W + 1) * sizeof(int));
    
    for (w = 0; w <= W; w++) {
        dp[w] = 0;
    }

    // update dp[] for every item. Note that we update dp[] in reverse order.
    for (int i = 0; i < n; i++) {
        for (w = W; wt[i] <= w; w--) {
            dp[w] = max(dp[w], val[i] + dp[w - wt[i]]);
        }
    }

    int result = dp[W];
    free(dp);
    return result;
}

int main() {
    int instances, n, W, i, j;
    scanf("%d", &instances);
    
    while (instances--) {
        scanf("%d %d", &n, &W);
        int *wt = (int *)malloc(n * sizeof(int));
        int *val = (int *)malloc(n * sizeof(int));
        
        for (i = 0; i < n; i++) {
            scanf("%d %d", &wt[i], &val[i]);
        }
        
        printf("%d\n", knapsack(W, wt, val, n));
        
        free(wt);
        free(val);
    }

    return 0;
}
