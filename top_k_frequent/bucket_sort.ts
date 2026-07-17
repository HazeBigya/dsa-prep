export {};

function bucketSort(nums: number[], k: number): number[] {
  const frequencyMap = new Map<number, number>();
  for (const num of nums) {
    frequencyMap.set(num, (frequencyMap.get(num) || 0) + 1);
  }

  const buckets: number[][] = Array.from({ length: nums.length + 1 }, () => []);
  for (const [num, frequency] of frequencyMap) {
    buckets[frequency].push(num);
  }

  const result: number[] = [];
  for (let i = buckets.length - 1; i > 0; i--) {
    for (const num of buckets[i]) {
      result.push(num);
      if (result.length === k) return result;
    }
  }

  return result;
}

const nums = [1, 1, 1, 2, 2, 3, 5, 5, 5, 5, 6, 6, 7, 8, 8, 8, 8];
const k = 2;
const result = bucketSort(nums, k);
console.log("Result:", result);
