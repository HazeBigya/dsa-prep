from collections import defaultdict


def grouped_anagrams(strs):
    anagram_map = {}
    for s in strs:
        sorted_str = "".join(sorted(s))
        if sorted_str in anagram_map:
            anagram_map[sorted_str].append(s)
        else:
            anagram_map[sorted_str] = [s]
    return list(anagram_map.values())


def grouped_anagrams_defaultdict(strs):
    anagram_map = defaultdict(list)
    for s in strs:
        sorted_str = "".join(sorted(s))
        anagram_map[sorted_str].append(s)
    return list(anagram_map.values())


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(
    "The Grouped Anagrams are :",
    grouped_anagrams(strs),
    grouped_anagrams_defaultdict(strs),
)
