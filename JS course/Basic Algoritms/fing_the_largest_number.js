function largestOfFour(arr) {
  let largestArr = [];
  for (let smallAr of arr){
      largestArr.push(Math.max(...smallAr));
      console.log(largestArr);
      // largestArr = array;
  }
  return largestArr;
}

x = largestOfFour([ [13, 27, 18, 26], [4, 5, 1, 3], [32, 35, 37, 39], [1000, 1001, 857, 1]]);
console.log(x);