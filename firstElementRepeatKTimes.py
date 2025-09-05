def firstElementRepeatKTimes(arr, k):
    count_map = {}
    for num in arr:
        count_map[num] = count_map.get(num, 0) + 1

    for num in arr:
        if count_map[num] == k:
            return num

    return -1

arr = [3, 1, 4, 4, 5, 2, 6, 1, 4]
k = 2
result = firstElementRepeatKTimes(arr, k)
print(result)
