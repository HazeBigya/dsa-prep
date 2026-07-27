export {};

function gcd_lcm(a: number, b: number) {
  const product: number = a * b;
  while (b !== 0) [a, b] = [b, a % b];
  const GCD = a;
  const LCM = product / GCD;
  console.log("GCD: ", GCD, "LCM: ", LCM);
}

gcd_lcm(48, 18);
