
function smallestCommons(arr) {
  let end = Math.max(...arr)
  let start = Math.min(...arr)
  let range = Array(end - start + 1).fill().map((_, index) => end - index)
  let found = false
  let multiplier = 1
  let candidate = end * multiplier

  while (!found) {
    candidate = end * multiplier
    found = range.every(
        (element, index, arr)=>Math.floor(candidate/element) === candidate/element
    )
    multiplier++
  }
  
  return candidate
  
}

console.log(
  smallestCommons([23,18])
);