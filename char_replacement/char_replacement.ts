export {};

function charReplacement(s: string, k: number): number {
  const count = new Map<string, number>();
  let L = 0;
  let maxFreq = 0;
  let maxLen = 0;
  for (let R = 0; R < s.length; R++) {
    count.set(s[R], (count.get(s[R]) || 0) + 1);
    maxFreq = Math.max(maxFreq, count.get(s[R])!);
    while (R - L + 1 - maxFreq > k) {
      count.set(s[L], count.get(s[L])! - 1);
      L++;
    }
    maxLen = Math.max(maxLen, R - L + 1);
  }
  return maxLen;
}

const s = "AAABABABA";
const k = 2;
console.log("The Max length of the longest repeating charecter with replacement is: ", charReplacement(s, k));
