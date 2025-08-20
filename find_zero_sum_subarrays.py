def find_zero_sum_subarrays(arr):
    res = []
    c_s = 0  #c_s = current sum
    s_m = {0: [-1]}  #s_m = sum map

    for i in range(len(arr)):
        c_s += arr[i]

        if c_s in s_m:
            for s_i in s_m[c_s]:
                res.append((s_i + 1, i))
            s_m[c_s].append(i)
        else:
            s_m[c_s] = [i]

    return res

a = [6, 3, -1, -3, 4, -2, 2, 4, 6, -12, -7]
print(f"{find_zero_sum_subarrays(a)}")
