from collections import deque

def maxSlidingWindow(arr, k):
    if not arr or k == 0:
        return []

    n = len(arr)
    if k > n:
        return [max(arr)]

    result = []
    dq = deque()
    for i in range(k):
        while dq and arr[i] >= arr[dq[-1]]:
            dq.pop()
        dq.append(i)
    result.append(arr[dq[0]])
    for i in range(k, n):
        if dq and dq[0] == i - k:
            dq.popleft()
        while dq and arr[i] >= arr[dq[-1]]:
            dq.pop()
        dq.append(i)
        result.append(arr[dq[0]])

    return result

arr = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
print(maxSlidingWindow(arr, k))
