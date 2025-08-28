def count_exactly_k_naive(s: str, k: int) -> int:
    n = len(s)
    count = 0

    for i in range(n):
        distinct_chars = set()
        for j in range(i, n):
            distinct_chars.add(s[j])
            if len(distinct_chars) == k:
                count += 1
            elif len(distinct_chars) > k:
                break
    return count

s = "pqpqs"
k = 2
result = count_exactly_k_naive(s, k)
print(f"The number of substrings with exactly {k} distinct characters in '{s}' is: {result}")
