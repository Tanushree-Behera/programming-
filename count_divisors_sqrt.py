import math
def count_divisors_sqrt(n):
    if n <= 0:
        return 0
    
    count = 0
    limit = int(math.sqrt(n))

    for i in range(1, limit + 1):
        if n % i == 0:
            if i * i == n:
                count += 1
            else:
                count += 2
    return count

N = 12
print(f"The number of divisors for {N} is: {count_divisors_sqrt(N)}")
