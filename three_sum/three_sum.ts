export {};

function three_sum(nums: number[]): number[][] {
  nums.sort((a, b) => a - b);

  const n = nums.length;
  let output: number[][] = [];

  for (let i = 0; i < n-2; i++) {
    if (i > 0 && nums[i] === nums[i - 1]) continue;
    let target = -nums[i];
    let L = i + 1;
    let R = n - 1;

    while (L < R) {
      let sum = nums[L] + nums[R];
      if (sum === target) {
        output.push([nums[i], nums[L], nums[R]]);
        L++;
        R--;
        while (L < R && nums[L] === nums[L - 1]) L++;
      } else if (sum < target) {
        L++;
      } else {
        R--;
      }
    }
  }

  return output;
}

const nums = [-1, 0, 1, 2, -1, -4];
console.log("The Three sum of the array is: ", three_sum(nums));
