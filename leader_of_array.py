def leaders(arr):
    n = len(arr)
    leaders = []
    if n == 0:
        return leaders

    max_from_right = float('-inf') # Initialize with negative infinity

    for i in range(n - 1, -1, -1):
        if arr[i] > max_from_right:
            leaders.append(arr[i])
            max_from_right = arr[i]

    return leaders[::-1] # Reverse the list to get leaders in original order

# Example usage:
arr = [16, 17, 4, 3, 5, 2]
res = leaders(arr)
print(res)
