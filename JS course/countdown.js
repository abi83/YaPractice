/*
The function should use recursion to return an array containing the integers n through 1
based on the n parameter. If the function is called with a number less than 1, the function
should return an empty array. For example, calling this function with n = 5 should
return the array [5, 4, 3, 2, 1]. Your function must use recursion by calling itself
and must not use loops of any kind.
*/

function countdown(n){
  if (n < 1) {
    return [];
  } else {
    const countArray = countdown(n - 1);
    countArray.unshift(n);
    return countArray;
  }}


function rangeOfNumbers(startNum, endNum) {
  if (endNum - startNum == 0) {return [endNum];
  } else {
    const output = rangeOfNumbers(startNum+1, endNum);
    output.unshift(startNum);
    return output;
  }
};

console.log(rangeOfNumbers(1,5));
console.log(rangeOfNumbers(6,9));
console.log(rangeOfNumbers(4,4));
