// paging.c

// furthest in the future paging in O(n logk): n - number of page requests
//                                             k - cache size

// input:
// (any int > 0) - gives the # of instances which follow
// for each instance:
//      line 1. (any int > 0) - the size of the cache
//      line 2. (any int > 0) - # of page requests
//      line 3. space delimited positive integers which will be the request
//          sequence. 

// i.e.

// 3 (# of instances)
// 2
// 7
// 1 2 3 2 3 1 2
// 4
// 12
// 12 3 33 14 12 20 12 3 14 33 12 20
// 3
// 20
// 1 2 3 4 5 1 2 3 4 5 1 2 3 4 5 1 2 3 4 5

// the sample input has 3 instances. The first has a cache holding 2 pages.
// It then has a request sequence of 7 pages. The second has a cache which
// holds 4 pages and a request sequence of 12 pages. The third has a cache
// which holds 3 pages and a request sequence of 20 pages.

// for each instance, the program should output the # of page faults achieved
// by furthest in the future paging assuming the cache is initially empty at
// the start of processing the page request sequence. One output should be
// given per line. The correct output for the sample instance is:

// 4
// 6
// 12

#include <stdio.h>
#include <stdlib.h>

int findReplaceIndex(int* cache, int cache_size, int* requests, int num_requests, int current_index) {
    int furthest = -1, index = -1;
    for (int i = 0; i < cache_size; ++i) {
        int j = current_index;
        for (; j < num_requests; ++j) {
            if (cache[i] == requests[j]) break;
        }
        // If this page is never used again, return immediately.
        if (j == num_requests) return i;
        if (j > furthest) {
            furthest = j;
            index = i;
        }
    }
    return index; // Index of the page to be replaced.
}

int main() {
    int num_instances;
    scanf("%d", &num_instances);

    while (num_instances--) {
        int cache_size, num_requests;
        scanf("%d %d", &cache_size, &num_requests);

        int* requests = (int*)malloc(num_requests * sizeof(int));
        for (int i = 0; i < num_requests; ++i) {
            scanf("%d", &requests[i]);
        }

        int* cache = (int*)malloc(cache_size * sizeof(int));
        for (int i = 0; i < cache_size; ++i) {
            cache[i] = -1; // Initialize cache
        }

        int page_faults = 0;
        for (int i = 0; i < num_requests; ++i) {
            int page = requests[i];
            int found = 0;
            for (int j = 0; j < cache_size; ++j) {
                if (cache[j] == page) {
                    found = 1;
                    break;
                }
            }
            if (!found) {
                page_faults++;
                found = 0;
                for (int j = 0; j < cache_size; ++j) {
                    if (cache[j] == -1) {
                        cache[j] = page;
                        found = 1;
                        break;
                    }
                }
                if (!found) {
                    int replaceIndex = findReplaceIndex(cache, cache_size, requests, num_requests, i + 1);
                    cache[replaceIndex] = page;
                }
            }
        }

        printf("%d\n", page_faults);
        free(requests);
        free(cache);
    }
    return 0;
}

