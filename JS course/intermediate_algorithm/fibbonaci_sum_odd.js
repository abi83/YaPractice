function sumFibs(num){
  let smaller = 1, bigger = 1;
  let temp = 0;
  let out = [1,1];
  
  while (smaller + bigger <= num) {
    out.push(smaller + bigger);
    temp = bigger;
    bigger = smaller + bigger
    smaller = temp;
  }
  console.log(out);
  return out.reduce(
      (acc, cu) => {if (cu % 2 === 1) {acc = acc + cu} return acc},0
  )
}

console.log(sumFibs(75025));