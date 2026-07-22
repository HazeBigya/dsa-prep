export {};

function twoSumSorted(nums: number[], target: number): number[] {
  let L: number = 0;
  let R: number = nums.length - 1;
  while (L < R) {
    const sum: number = nums[L] + nums[R];
    if (sum === target) return [L + 1, R + 1];
    else if (sum < target) L++;
    else R--;
  }
  return [];
}

const nums = [2, 7, 9, 11, 15, 20, 31];
const target = 35;
console.log(`The sum of array for target ${target} using sorting method:`, twoSumSorted(nums, target));
