export {};

function factorial(n: number): number {
  if (n === 0) return 1;
  return n * factorial(n - 1);
}

function factorialIteration(n: number): number {
  let product = 1;
  for (let i = 2; i<= n; i++) {
    product *= i;
  }
  return product;
}

const num: number = 5;
console.log(`The Factorial of ${num} is: `, factorial(num));
console.log(`The Factorial using iteration for ${num} is: `, factorialIteration(num));
