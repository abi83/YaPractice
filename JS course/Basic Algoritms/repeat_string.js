// Repeat a given string str (first argument) for num times (second argument).
// Return an empty string if num is not a positive number. For the purpose of
// this challenge, do not use the built-in .repeat() method.


function repeatStringNumTimes(str, num) {
  if (num>0) {
    return str + repeatStringNumTimes(str, num-1)
  }
  return '';
}

x = repeatStringNumTimes("abc", 10);
console.log(x);