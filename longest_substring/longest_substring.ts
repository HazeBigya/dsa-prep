export {};

function longestSubString(s: string): number {
  let seen = new Set();
  let L = 0;
  let maxLength = 0;
  for (let R = 0; R < s.length; R++) {
    while (seen.has(s[R])) {
      seen.delete(s[L]);
      L++;
    }
    seen.add(s[R]);
    maxLength = Math.max(maxLength, R - L + 1);
  }
  return maxLength;
}

const s = "abcabcbb";
console.log("The longest substring length is :", longestSubString(s));
