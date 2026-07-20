export {};

function productOfArray(nums: number[]): number[] {
  const n: number = nums.length;
  const output: number[] = new Array(n);

  let pre: number = 1;
  for (let i: number = 0; i < n; i++) {
    output[i] = pre;
    pre *= nums[i];
  }

  let post: number = 1;
  for (let i: number = n - 1; i >= 0; i--) {
    output[i] = output[i] * post;
    post *= nums[i];
  }
  
  return output;
}

const nums = [5, 10, 1, 2];
const result = productOfArray(nums);
console.log("result:", result);
