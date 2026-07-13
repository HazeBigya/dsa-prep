export {};

function containsDuplicate(nums: number[]): boolean {
  const seen = new Set<number>();
  for (const num of nums) {
    if (seen.has(num)) {
      return true;
    }
    seen.add(num);
  };
  return false;
}

function containsDuplicateOneLine(nums: number[]): boolean {
  return nums.length !== new Set(nums).size;
}

const nums: number[] = [1, 2, 3, 4, 5, 1];
const result: boolean = containsDuplicate(nums);
console.log(`Does the array contain duplicates? ${result}`); // Output: true

const onelinerResult: boolean = containsDuplicateOneLine(nums);
console.log(`Does the array contain duplicates (one-liner)? ${onelinerResult}`); // Output: true
