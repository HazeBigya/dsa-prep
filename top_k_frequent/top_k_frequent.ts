export {};

function topKFrequent(nums: number[], k: number): number[] {
  const frequencyMap = new Map<number, number>();
  for (const num of nums) {
    frequencyMap.set(num, (frequencyMap.get(num) || 0) + 1);
  }
  const sortedEntries = [...frequencyMap.entries()].sort((a, b) => b[1] - a[1]);
  console.log('Frequency Map:', frequencyMap);
  console.log('Sorted Entries:', sortedEntries);
  return sortedEntries.slice(0, k).map(entry => entry[0]);
}

const nums = [1, 1, 1, 2, 2, 3, 5, 5, 5, 5, 6, 6, 7, 8, 8, 8, 8];
const k = 2;

const result = topKFrequent(nums, k);
console.log(`Top ${k} frequent elements: `, result);