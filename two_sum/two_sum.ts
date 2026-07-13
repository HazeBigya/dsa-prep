export {};

function twoSum(numbers: number[], target: number): number[] {
  const numMap = new Map<number, number>();
  for (let i = 0; i < numbers.length; i++) {
    const diff = target - numbers[i];
    if (numMap.has(diff)) {
      return [numMap.get(diff)!, i];
    }
    numMap.set(numbers[i], i);
  }
  throw new Error("No two sum solution found");
}

const numbers: number[] = [2, 7, 11, 15];
const target: number = 9;
const result: number[] = twoSum(numbers, target);
console.log(`Indices of the two numbers that add up to ${target}:`, result);
