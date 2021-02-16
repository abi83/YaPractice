// Return the provided string with the first letter of each word capitalized.
//     Make sure the rest of the word is in lower case.
//
// For the purpose of this exercise, you should also capitalize connecting
// words like "the" and "of".

function titleCase(str) {
  let answer = [];
  for (let word of str.split(' ')){
    answer.push(word[0].toUpperCase()+word.substring(1).toLowerCase());
  }
  return answer.join(' ');
}

a = titleCase("I'm a little tea pot");
console.log(a);
