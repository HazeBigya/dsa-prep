function groupAnagrams(strs: string[]): string[][] {
  const anagramMap = new Map<string, string[]>();
  for (const str of strs) {
    const sortedKey = str.split("").sort().join("");
    if (!anagramMap.has(sortedKey)) {
      anagramMap.set(sortedKey, []);
    }
    anagramMap.get(sortedKey)!.push(str);
  }
  return Array.from(anagramMap.values());
}

function groupAnagramsOptimized(strs: string[]): string[][] {
  const anagramMap = new Map<string, string[]>();
  for (const str of strs) {
    const count = new Array(26).fill(0);
    for (const char of str) {
      count[char.charCodeAt(0) - 'a'.charCodeAt(0)]++;
    }
    const key = count.join('#');
    if (!anagramMap.has(key)) {
      anagramMap.set(key, []);
    }
    anagramMap.get(key)!.push(str);
  }
  return Array.from(anagramMap.values());
}

const strs = ["eat", "tea", "tan", "ate", "nat", "bat"];

const result1 = groupAnagrams(strs);
console.log("Grouped Anagrams: ", result1);

const result2 = groupAnagramsOptimized(strs);
console.log("Grouped Anagrams (Optimized): ", result2);