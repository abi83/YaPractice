function factorialize(num) {
  let answer = 1;
  for (let i=1; i<=num; i++){
    // console.log('i': i, 'answer:', answer, answer)
    answer *= i;
  }
  return answer;
}

console.log(factorialize(5));