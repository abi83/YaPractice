function mutation(arr) {
  for (let symbol of arr[1]) {
    if (!arr[0].toLowerCase().includes(symbol.toLowerCase())){
      return false
    }
  }
  return true
}

console.log(mutation(["Hello", "helloa"]));