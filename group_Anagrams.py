from collections import defaultdict

def group_Anagrams(strs):
    anagrams = defaultdict(list)
    
    for word in strs:
        sorted_word = "".join(sorted(word))
        anagrams[sorted_word].append(word)
        
    return list(anagrams.values())

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
output = group_Anagrams(strs)
print(output)
