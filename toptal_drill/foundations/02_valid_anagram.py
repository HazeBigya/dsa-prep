from collections import Counter


def valid_anagram(s, t):
    if len(s) != len(t):
        return False

    count_s = {}
    count_t = {}

    for char in s:
        count_s[char] = count_s.get(char, 0) + 1
    for char in t:
        count_t[char] = count_t.get(char, 0) + 1

    return count_s == count_t


def valid_anagram_counter(s, t):
    return Counter(s) == Counter(t)


s = "anagram"
t = "nagaram"

print("Is Anagram: ", valid_anagram(s, t), valid_anagram_counter(s, t))
