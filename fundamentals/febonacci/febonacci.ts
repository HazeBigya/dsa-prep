export {};

function febonacciSeries(num: number): number[] {
  if (num <= 0) return [];
  if (num === 1) return [0];

  const result = [0, 1];
  for (let i = 2; i < num; i++) {
    result.push(result[i - 1] + result[i - 2]);
  }
  return result;
}

function febonacci(num: number): number {
  if (num == 0) return 0;
  if (num == 1) return 1;

  let prev2 = 0;
  let prev1 = 1;
  let current = 0;

  for (let i = 2; i <= num; i++) {
    current = prev1 + prev2;
    prev2 = prev1;
    prev1 = current;
  }
  return current;
}

function febonacciSeriesWithArray(numArray: number[]): number[] {
  if (numArray.length === 0) return [];
  if (numArray.length === 1) return [0];
  if (numArray.length === 2) return [0, 1];

  for (let i = 2; i < numArray.length; i++) {
    numArray[i] = numArray[i - 1] + numArray[i - 2];
  }
  return numArray;
}

const num = 10;
console.log(febonacciSeries(num));

const feb = 5;
console.log(febonacci(feb));

const numArray = [0, 1, 2, 3, 4, 5];
console.log(febonacciSeriesWithArray(numArray));
