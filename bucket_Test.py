def bucketsort(arr):
    max_value = max(arr)
    min_value = min(arr)

    range_of_values = max_value - min_value
    num_buckets = len(arr)
    buckets = [[] for _ in range(num_buckets)]

    for num in arr:
        index = int((num - min_value) / (range_of_values / (num_buckets)))
        buckets[index].append(num)

    for i in range(num_buckets):
        buckets[i].sort()

    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(bucket)

    return sorted_arr

arr = [3, 6, 8, 10, 1, 2, 1]
sorted_arr = bucketsort(arr)
print("Sorted array:", sorted_arr)
