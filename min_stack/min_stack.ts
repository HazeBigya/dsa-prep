export {};

class minStack {
  private arr: number[];
  private min_arr: number[];

  constructor() {
    this.arr = [];
    this.min_arr = [];
  }

  push(x: number) {
    this.arr.push(x);
    if (this.min_arr.length > 0) {
      this.min_arr.push(Math.min(x, this.getMin()));
    } else this.min_arr.push(x);
  }

  pop() {
    this.arr.pop();
    this.min_arr.pop();
  }

  top(): number {
    return this.arr.at(-1) as number;
  }

  getMin(): number {
    return this.min_arr.at(-1) as number;
  }

  print() {
    console.log(this.arr);
    console.log(this.min_arr);
  }
}

const stack = new minStack();
stack.push(1);
stack.push(-2);
console.log("Top so far: ", stack.top());
stack.push(0);
stack.push(-5);
stack.push(2);
stack.pop();
console.log("Min so far: ", stack.getMin());
stack.pop();
console.log("Top: ", stack.top());
console.log("Min: ", stack.getMin());
stack.print();
