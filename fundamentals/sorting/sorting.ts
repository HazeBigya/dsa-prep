export {};

function sortArr(arr: number[]): void {
  // Legacy
  //   const asc = [...arr].sort((a, b) => a - b);
  //   const desc = [...arr].sort((a, b) => b - a);

  // New ES 2023 method
  const asc = arr.toSorted((a, b) => a - b);
  const desc = arr.toSorted((a, b) => b - a);

  console.log(`Ascending Order :`, asc);
  console.log(`Decending Order: `, desc);
}

function sortString(str: string): void {
  const asc = str.toLocaleLowerCase().split("").sort().join("");
  const desc = str.toLocaleLowerCase().split("").sort().reverse().join("");
  console.log(`Ascending Order :`, asc);
  console.log(`Decending Order: `, desc);
}

function bubbleSort(arr: number[]): number[] {
  const n = arr.length;

  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n - i - 1; j++) {
      if (arr[j] > arr[j + 1]) {
        [arr[j], arr[j + 1]] = [arr[j + 1], arr[j]];
      }
    }
  }
  return arr;
}

const arr = [10, 2, 1, 20];
const str = "Banana";
sortArr(arr);
sortString(str);

const array = [5, 3, 8, 4, 2];
console.log(`The bubble sort Algo: `, bubbleSort(array));
