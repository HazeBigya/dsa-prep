export {};

function reverseString(str: string): string {
  const len = str.length;

  const S = str.split("");

  let L = 0;
  let R = len - 1;

  while (L < R) {
    [S[L], S[R]] = [S[R], S[L]];
    L++;
    R--;
  }

  return S.join("");
}

function reverseArray(arr: number[]): number[] {
  const nums = [...arr];

  let L = 0;
  let R = arr.length - 1;

  while (L < R) {
    [nums[L], nums[R]] = [nums[R], nums[L]];
    L++;
    R--;
  }

  return nums;
}

const str = "hello";
const arr = [1, 2, 3, 4, 5];
console.log("The reverse of String ", str, " is ", reverseString(str));
console.log("The reverse of Array ", arr, " is ", reverseArray(arr));
