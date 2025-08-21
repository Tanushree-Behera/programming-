def trap_rain_water(h):
    n = len(h)
    res = 0
    for i in range(n):
        l = 0
        r = 0
        for j in range(i + 1):
            l = max(l, h[j])
        for j in range(i, n):
            r = max(r, h[j])
        res += max(0, min(l, r) - h[i])
    return res

h = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(trap_rain_water(h))
