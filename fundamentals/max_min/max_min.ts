export {};

function MaxMin(nums: number[]) {
  let max = nums[0];
  let min = nums[0];

  for (let i = 1; i < nums.length; i++) {
    if (nums[i] > max) max = nums[i];
    if (nums[i] < min) min = nums[i];
  }

  console.log(`The Max number is ${max} and the min number is ${min}`);
}

const nums = [4, 6, -2, 9, -7, 6];
MaxMin(nums);
