/*
 * Weighted Interval Scheduling in O(n^2) time, where n is the number of jobs
 * 
 * The input will start with a positive integer, giving the number of instances
 * which follow. For each instance, there will be a positive integer, giving the
 * number of jobs. For each job, there will be a trio of integers, i, j, k,
 * where i < j, i is the start time, j is the finish time, and k is the weight.
 */

// Sample input:

// 2
// 1
// 1 4 5
// 3
// 1 2 1
// 3 4 2
// 2 6 4

/*
 * The sample input has two instances. The first instance has one job to
 * schedule with the start time of 1, the finish time of 4, and the weight of 5.
 * The objective of the problem is to determine a schedule of non-overlapping
 * intervals with maximum weight and return the weight of the schedule.
 *
 * For each instance, the program should output the total weight of the
 * intervals scheduled on a separate line. Each output line should be termianted
 * by exactly one newline character.
 */

// Sample output:

// 5
// 5

#include <stdio.h>
#include <stdlib.h>

#define MAX_JOBS 10000

struct Job {
  long start, finish, weight;
};

// function to compare two jobs based on their finish time
int compare(const void *a, const void *b) {
  struct Job *jobA = (struct Job *)a;
  struct Job *jobB = (struct Job *)b;
  return (jobA->finish > jobB->finish) - (jobA->finish < jobB->finish);
}

// function to find the latest job (in sorted array) that doesn't conflict with the job[i] using binary search
int latestNonConflict(struct Job jobs[], int i) {
  int low = 0, high = i - 1;
  while (low <= high) {
    int mid = (low + high) / 2;
    if (jobs[mid].finish <= jobs[i].start) {
      if (mid + 1 <= high && jobs[mid + 1].finish <= jobs[i].start)
        low = mid + 1;
      else
        return mid;
    } else {
      high = mid - 1;
    }
  }
  return -1;
}

// function to find the maximum weight of non-overlapping intervals
long findMaxWeight(struct Job jobs[], int n) {
  // sort jobs based on finish time
  qsort(jobs, n, sizeof(jobs[0]), compare);

  // static array to store the maximum weight of non-overlapping intervals
  long maxWeight[MAX_JOBS];
  maxWeight[0] = jobs[0].weight;

  for (int i = 1; i < n; i++) {
    int l = latestNonConflict(jobs, i);
    long weight = jobs[i].weight + (l != -1 ? maxWeight[l] : 0);
    maxWeight[i] = (weight > maxWeight[i - 1]) ? weight : maxWeight[i - 1];
  }

  return maxWeight[n - 1];
}

int main() {
  int t;
  scanf("%d", &t);
  while (t--) {
    int n;
    scanf("%d", &n);
    struct Job jobs[n];
    for (int i = 0; i < n; i++) {
      scanf("%ld %ld %ld", &jobs[i].start, &jobs[i].finish, &jobs[i].weight);
    }
    printf("%ld\n", findMaxWeight(jobs, n));
  }
  return 0;
}


