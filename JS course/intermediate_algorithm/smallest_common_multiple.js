/*
Find the smallest common multiple of the provided parameters that can be
evenly divided by both, as well as by all sequential numbers in the range
between these parameters.

The range will be an array of two numbers that will not necessarily be in
numerical order.

For example, if given 1 and 3, find the smallest common multiple of both
1 and 3 that is also evenly divisible by all numbers between 1 and 3.
The answer here would be 6.
 */

function smallestCommons(arr) {
  let end = Math.max(...arr)
  let start = Math.min(...arr)
  let primes = [2]
  for (let number = 3; number <= end; number++) {
    let numberIsPrime = true
    for (let prime of primes) {
      if (number % prime === 0) {
        numberIsPrime = false
        break
      }
    }
    if (numberIsPrime && !primes.includes(number)) {
      primes.push(number)
    }
  }
  // console.log(primes)
  let range = Array(end - start + 1).fill().map((_, idx) => start + idx)
  let primesPower = [];
  for (let prime of primes) {
    primesPower.push(
      range
      .map(function(element) {
            let power = Math.log(element)/Math.log(prime)
            // console.log('element', element, 'prime', prime, 'power',power)
            if (Math.abs(power - Math.floor(power)) < 0.001) {
              return {prime: prime, element: element, power: Math.floor(power)}
            // } else {
            //   return {prime: prime, element: element, power: 1}
            }
          })
      .filter((element)=> element)
      .find(function( element, index, array) {
        let arrayOfPower = array.map((element) => element.power);
        return element.power === Math.max(...arrayOfPower)
      })
    )
    }
  console.log(primesPower)
  return primesPower
    .filter((element) => element)
    .reduce(
        function (accum, element) {return accum * Math.pow(element.prime, element.power)},
        1
    )
}

console.log(
  smallestCommons([18,23])
);