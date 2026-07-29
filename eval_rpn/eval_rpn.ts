export {};

function evalRpn(tokens: string[]) {
  const operand = new Set(["+", "-", "*", "/"]);
  const stack: number[] = [];
  tokens.forEach((token) => {
    if (operand.has(token)) {
        const a = stack.pop()!;
        const b = stack.pop()!;
      switch (token) {
        case "+":
          stack.push(b + a);
          break;
        case "-":
          stack.push(b - a);
          break;
        case "*":
          stack.push(b * a);
          break;
        case "/":
          stack.push(Math.trunc(b / a));
          break;
        default:
          break;
      }
    } else {
      stack.push(Number(token));
    }
  });

  console.log("Value of the expression =", stack.pop());
}
const token = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"];
evalRpn(token);
