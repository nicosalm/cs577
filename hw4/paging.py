def find_replace_index(cache, requests, current_index):
    furthest = -1
    index = -1
    for i in range(len(cache)):
        j = current_index
        for j in range(current_index, len(requests)):
            if cache[i] == requests[j]:
                break
        if j == len(requests):
            return i
        if j > furthest:
            furthest = j
            index = i
    return index


def main():
    num_instances = int(input())

    for _ in range(num_instances):
        cache_size = int(input())
        num_requests = int(input())
        requests = list(map(int, input().split()))

        cache = [-1] * cache_size
        page_faults = 0

        for i in range(num_requests):
            page = requests[i]
            if page not in cache:
                page_faults += 1
                if -1 in cache:
                    cache[cache.index(-1)] = page
                else:
                    replace_index = find_replace_index(cache, requests, i + 1)
                    cache[replace_index] = page

        print(page_faults)


if __name__ == "__main__":
    main()
