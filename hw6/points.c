// points.c

/*
* Suppose you are given two sets of n points, one set {p1, p2, . . . , pn} on the line y = 0 and the other set {q1, q2, . . . , qn} on the line y = 1.
* Create a set of n line segements by connecting each point pi to qi. Write a program to determine the number of pairs of line segments that intersect.
*
* Input (read from stdin): 2n points, each point is represented by a pair of real numbers.
* Outpt (to stdout): The number of intersecting pairs of line segments.
*
* This is done with a divide and conquer algorithm with a time complexity of O(nlogn) using merge sort.
*
* The first line of the input is the number of instances. For each instance, the first line will contain the number of pairs of points (n).
* The next n lines of the instance each contain the location x of a point qi on the top line. Followed by the final n lines of the instance each contain the location x of a point pi on the bottom line.
*
* Example:
* Input:
* 2
* 4
* 1
* 10
* 8
* 6
* 6
* 2
* 5
* 1
* 5
* 9
* 21
* 1
* 5
* 18
* 2
* 4
* 6
* 10
* 1
*
* Output:
* 4
* 7
*/

#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int x;                  // x-coordinate
    int original_index;     // original index in the input
} point;

// comparator for sorting points by x-coordinate
int compare_points(const void *a, const void *b) {
    point *point_a = (point *)a;
    point *point_b = (point *)b;
    return point_a->x - point_b->x;
}

// function to merge two halves of an array and count inversions
long long merge_and_count(int *array, int left, int middle, int right) {
    int i, j, k;
    long long inversions = 0;
    int n1 = middle - left + 1;
    int n2 = right - middle;
    int L[n1], R[n2];

    // copy data to temporary subarrays l[] and r[]
    for (i = 0; i < n1; i++)
        L[i] = array[left + i];
    for (j = 0; j < n2; j++)
        R[j] = array[middle + 1 + j];

    // merge the temp arrays back into array[left..right]
    i = 0; j = 0; k = left;
    while (i < n1 && j < n2) {
        if (L[i] <= R[j]) {
            array[k] = L[i++];
        } else {
            array[k] = R[j++];
            inversions += (n1 - i);
        }
        k++;
    }

    // copy the remaining elements of l[], if there are any
    while (i < n1) {
        array[k++] = L[i++];
    }

    // copy the remaining elements of r[], if there are any
    while (j < n2) {
        array[k++] = R[j++];
    }

    return inversions;
}

// function to sort an array using merge sort and count inversions
long long merge_sort_and_count(int *array, int left, int right) {
    long long inversions = 0;
    if (left < right) {
        // same as (left+right)/2, but avoids overflow for large left and right
        int middle = left + (right - left) / 2;

        // sort first and second halves
        inversions += merge_sort_and_count(array, left, middle);
        inversions += merge_sort_and_count(array, middle + 1, right);

        // merge the sorted halves
        inversions += merge_and_count(array, left, middle, right);
    }
    return inversions;
}

int main() {
    int instances, n;
    scanf("%d", &instances);

    while (instances--) {
        scanf("%d", &n);
        point points_top[n], points_bottom[n];
        int sequence[n];  // this will hold the mapping to count inversions

        for (int i = 0; i < n; i++) {
            scanf("%d", &points_top[i].x);
            points_top[i].original_index = i;
        }
        for (int i = 0; i < n; i++) {
            scanf("%d", &points_bottom[i].x);
            points_bottom[i].original_index = i;
        }

        // sort points on one line, say y=1 (top line)
        qsort(points_top, n, sizeof(point), compare_points);

        // for each point in the sorted top line, find the position of its connected point in the bottom line
        for (int i = 0; i < n; i++) {
            sequence[i] = points_bottom[points_top[i].original_index].x;
        }

        // count inversions in the bottom line sequence
        long long intersections = merge_sort_and_count(sequence, 0, n - 1);

        printf("%lld\n", intersections);
    }

    return 0;
}
