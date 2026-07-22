export {};

function sumOfDigits(n: number): number {
  let sum = 0;
  while (n > 0) {
    sum += n % 10;
    n = Math.floor(n / 10);
  }
  return sum;
}

function countOfDigits(n: number): number {
  let count = 0;
  if (n === 0) return 1;
  while (n > 0) {
    count += 1;
    n = Math.floor(n / 10);
  }
  return count;
}

const n = 1234;
console.log("The sum of numbers: ", sumOfDigits(n));
console.log("The count of numbers: ", countOfDigits(n));
