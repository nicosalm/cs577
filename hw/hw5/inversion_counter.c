// inversion_counter.c

#include <stdio.h>
#include <stdlib.h>

int merge(int *a, int *aux, int lo, int mid, int hi) {
    int i = lo, j = mid + 1, k;
    long long count = 0;
    for (k = lo; k <= hi; k++) {
        aux[k] = a[k];
    }

    for (k = lo; k <= hi; k++) {
        if (i > mid) a[k] = aux[j++];
        else if (j > hi) a[k] = aux[i++];
        else if (aux[j] < aux[i]) {
            a[k] = aux[j++];
            count += (mid - i + 1); // count each inversion
        } else {
            a[k] = aux[i++];
        }
    }
    return count;
}

long long mergeSort(int *a, int *aux, int lo, int hi) {
    int mid;
    long long count = 0;
    if (hi <= lo) return 0;
    mid = lo + (hi - lo) / 2;
    count += mergeSort(a, aux, lo, mid);
    count += mergeSort(a, aux, mid + 1, hi);
    count += merge(a, aux, lo, mid, hi);
    return count;
}

long long inversionCounter(int *a, int n) {
    int *aux = (int *)malloc(n * sizeof(int));
    long long count = mergeSort(a, aux, 0, n - 1);
    free(aux);
    return count;
}

int main() {
    int k, n, i, j;
    scanf("%d", &k);
    for (i = 0; i < k; i++) {
        scanf("%d", &n);
        int *a = (int *)malloc(n * sizeof(int));
        for (j = 0; j < n; j++) {
            scanf("%d", &a[j]);
        }
        printf("%lld\n", inversionCounter(a, n));
        free(a);
    }
    return 0;
}

