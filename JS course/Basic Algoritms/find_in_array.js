function getIndexToIns(arr, num) {
  const f = (element, indexm, arr) => {
    return element >= num
  }
  let a = arr.sort(function(a,b){return a-b  }).findIndex(f)
  return  a >= 0 ? a: arr.length;
}

console.log(getIndexToIns([3, 10, 5], 3));