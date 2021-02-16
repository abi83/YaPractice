function findLongestWordLength(str) {
  let arrFromStr = str.split(' ');
  let n = 0;
  for (let i = 0; i<=arrFromStr.length-1;i++){
    if (n<arrFromStr[i].length) {n=arrFromStr[i].length}
  }
  return n;
}

console.log(findLongestWordLength("What if we try a super-long word such as otorhinolaryngology"));