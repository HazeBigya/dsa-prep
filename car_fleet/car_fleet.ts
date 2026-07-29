export {};

function carFleet(position: number[], speed: number[], target: number): number {
  const stack: number[] = [];
  const cars = position.map((p, i) => [p, speed[i]] as [number, number]).sort((a, b) => b[0] - a[0]);
  cars.forEach(([pos, spd]) => {
    const time: number = (target - pos) / spd;
    if (stack.length === 0 || time > stack[stack.length - 1]) {
      stack.push(time);
    }
  });
  return stack.length;
}

const target = 12
const position = [10, 8, 0, 5, 3]
const speed  = [ 2, 4, 1, 1, 3]

console.log("The number of fleet are: ", carFleet(position, speed, target))