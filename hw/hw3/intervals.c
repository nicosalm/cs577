// implement an optimal algorithm for interval scheduling (Greedy algorithm) in O(nlogn) time, where n is the number of jobs.
// The input will start with an positive integer, k, giving the number of instances that follow. For each instance, there will
// be a positive integer, n, giving the number of jobs. For each job, there will be a pair of positive integers i and j, where
// i ≤ j, and i is the start time, and j is the end time.

// a sample input:

// 2
// 1
// 1 4
// 3
// 1 2
// 3 4
// 2 6

// The sample input has two instances. The first instance has one job to schedule with a start time of 1
// and an end time of 4. The second instance has 3 jobs.

// For each instance, your program should output the number of intervals scheduled on a separate line.
// Each output line should be terminated by a newline. The correct output to the sample input would be:

// 1
// 2

#include <stdio.h>
#include <stdlib.h>

typedef struct job {
    int start, end;
} Job;

int compare(const void *a, const void *b) {
    return ((Job *)a)->end - ((Job *)b)->end;
}

// we need some way to schedule jobs
int schedule_jobs(Job jobs[], int n) {

    qsort(jobs, n, sizeof(Job), compare);
    int count = 1;
    int end_mark = jobs[0].end;

    for (int i = 1; i < n; i++) {
        if (jobs[i].start >= end_mark) {
            count++;
            end_mark = jobs[i].end;
        }
    }
    return count;
}

int main() {
   int k, n;
    scanf("%d", &k); // read the number of instances
    while (k--) {
        scanf("%d", &n);

        Job *jobs = (Job *)malloc(n * sizeof(Job));

        for (int i = 0; i < n; i++) {
            scanf("%d %d", &jobs[i].start, &jobs[i].end);
        }

        printf("%d\n", schedule_jobs(jobs, n));
        free(jobs);
    }
}
