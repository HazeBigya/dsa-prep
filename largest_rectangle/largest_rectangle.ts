export {};

function largestRectangle(heights: number[]): number {
  const stack: number[] = [];
  let maxArea: number = 0;
  const n = heights.length;

  for (let i = 0; i < n; i++) {
    while (stack.length !== 0 && heights[i] < heights[stack[stack.length - 1]]) {
      const h = heights[stack.pop()!];
      const width = stack.length === 0 ? i : i - stack[stack.length - 1] - 1;
      maxArea = Math.max(maxArea, width * h);
    }
    stack.push(i);
  }

  while (stack.length !== 0) {
    const h = heights[stack.pop()!];
    const width = stack.length === 0 ? n : n - stack[stack.length - 1] - 1;
    maxArea = Math.max(maxArea, h * width);
  }

  return maxArea;
}

const heights = [2, 1, 5, 6, 2, 3];
console.log("The max area of the rectangle is: ", largestRectangle(heights));
