from typing import List

def longest_common_prefix(strs: List[str]) -> str:
    if not strs:
        return ""

    for i in range(len(strs[0])):
        char = strs[0][i]
        for j in range(1, len(strs)):
            if i >= len(strs[j]) or strs[j][i] != char:
                return strs[0][:i]

    return strs[0]
    
strs1 = ["flower", "flow", "flight"]
print(f"The longest common prefix for {strs1} is: '{longest_common_prefix(str
