from collections import defaultdict

def group_anagrams(strs):
    anagram_map = {}
    for str in strs:
        sorted_str = ''.join(sorted(str))
        if(sorted_str in anagram_map):
            anagram_map[sorted_str].append(str)
        else:
            anagram_map[sorted_str] = [str]
    return list(anagram_map.values())

def group_anagrams_using_defaultdict(strs):
    anagram_map = defaultdict(list)
    for str in strs:
        sorted_str = ''.join(sorted(str))
        anagram_map[sorted_str].append(str)
    return list(anagram_map.values())

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
result = group_anagrams(strs)
print("Grouped anagrams:", result)  # Output: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]