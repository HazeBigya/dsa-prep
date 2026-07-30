export {};

function minWindowSubstring(s: string, t: string): string {
  if (t.length === 0 || s.length === 0) return "";

  const need = new Map<string, number>();
  for (const c of t) need.set(c, (need.get(c) ?? 0) + 1);
  const needCount = need.size;

  const window = new Map<string, number>();
  let have = 0;
  let res = "";
  let resLen = Infinity;
  let L = 0;

  for (let R = 0; R < s.length; R++) {
    const c = s[R];
    window.set(c, (window.get(c) ?? 0) + 1);
    if (need.has(c) && window.get(c) === need.get(c)) have++;
    while (have === needCount) {
      if (R - L + 1 < resLen) {
        resLen = R - L + 1;
        res = s.slice(L, R + 1);
      }
      const leftC = s[L];
      window.set(leftC, (window.get(leftC) ?? 0) - 1);
      if (need.has(leftC) && (window.get(leftC) ?? 0) < (need.get(leftC) ?? 0)) have--;
      L++;
    }
  }

  return res;
}

let s = "ADOBECODEBANC";
let t = "ABC";
console.log("The shortest substring is: ", minWindowSubstring(s, t));
