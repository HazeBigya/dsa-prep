export {};

function bestTimeStock(prices: number[]): number {
  if (prices.length == 0) return 0;
  let min_price = prices[0];
  let max_profit = 0;
  for (let i = 1; i < prices.length; i++) {
    if (prices[i] < min_price) min_price = prices[i];
    else {
      const profit = prices[i] - min_price;
      if (profit > max_profit) max_profit = profit;
    }
  }
  return max_profit;
}

const prices = [7, 1, 5, 3, 6, 4];
console.log("The Max price is : ", bestTimeStock(prices));
