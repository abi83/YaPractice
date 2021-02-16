function findElement(arr, func) {
  return arr.find(func);
}

x = findElement([1, 2, 3, 4], num => num % 2 === 0);

console.log(x);