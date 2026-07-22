export {};

function containerWithTheMostWater(height: number[]): number {
  let max_area = 0;
  let L = 0;
  let R = height.length - 1;

  while (L < R) {
    const area = (R - L) * Math.min(height[L], height[R]);
    max_area = Math.max(max_area, area);
    if (height[L] < height[R]) L++;
    else R--;
  }
  return max_area;
}

const height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
console.log("The max area the wall can hold the water is", containerWithTheMostWater(height))
