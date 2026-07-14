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

const start1 = performance.now();
const result1 = groupAnagrams(strs);
const end1 = performance.now();
console.log("Grouped Anagrams: ", result1);
console.log(`Time taken: ${(end1 - start1).toFixed(4)} ms`);

const start2 = performance.now();
const result2 = groupAnagramsOptimized(strs);
const end2 = performance.now();
console.log("Grouped Anagrams (Optimized): ", result2);
console.log(`Time taken (Optimized): ${(end2 - start2).toFixed(4)} ms`);