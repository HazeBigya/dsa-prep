export {};

interface bracketsT {
  [key: string]: string;
}

function validParenthesis(s: string): boolean {
  const stack = [];
  const closed_brackets: bracketsT = {
    ")": "(",
    "}": "{",
    "]": "["
  };
  for (const char of s) {
    if (!(char in closed_brackets)) stack.push(char);
    else {
      if (stack.length === 0 || stack.pop() !== closed_brackets[char]) return false;
    }
  }
  return stack.length === 0;
}

const s = "{][]}";
console.log("The string is a valid parenthesis: ", validParenthesis(s));
