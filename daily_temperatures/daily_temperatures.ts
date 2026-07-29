export {};

function dailyTemperature(temp: number[]): number[] {
  const n = temp.length;
  const answer: number[] = new Array(n).fill(0);
  const stack: number[] = [];
  for (let i: number = 0; i < n; i++) {
    while (stack.length !== 0 && temp[i] > temp[stack[stack.length - 1]]) {
      const top: number = stack.pop()!;
      answer[top] = i - top;
    }
    stack.push(i);
  }
  return answer;
}

const temp = [73, 74, 75, 71, 69, 72, 76, 73];
console.log("The days before a warmer temperature is: ", dailyTemperature(temp));
