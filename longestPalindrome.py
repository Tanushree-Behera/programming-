class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s

        start = 0
        max_len = 1
        n = len(s)

        
        def expand_from_center(left, right):
            nonlocal start, max_len
            while left >= 0 and right < n and s[left] == s[right]:
                current_len = right - left + 1
                if current_len > max_len:
                    max_len = current_len
                    start = left
                left -= 1
                right += 1

        for i in range(n):
            # Case for odd-length palindromes
            expand_from_center(i, i)
            
            # Case for even-length palindromes
            expand_from_center(i, i + 1)

        return s[start:start + max_len]


solution = Solution()
print(solution.longestPalindrome("babad")) # Output: "bab"

