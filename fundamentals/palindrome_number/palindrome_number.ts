export {};

function palindroneNumber(n: number): boolean {
  const original = n;
  let reversed = 0;

  if (n === 0) return true;
  else if (n < 0) return false;
  else {
    while (n > 0) {
      const num = n % 10;
      reversed = reversed * 10 + num;
      n = Math.floor(n / 10);
    }
    if (reversed === original) return true;
    else return false;
  }
}

const n = 121;
console.log("Is the number a palindrome: ", palindroneNumber(n));
