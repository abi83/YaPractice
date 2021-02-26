/*
Return true if the given string is a palindrome. Otherwise, return false.
A palindrome is a word or sentence that's spelled the same way both forward
and backward, ignoring punctuation, case, and spacing.
 */

function palindrome(str) {
  let newstr = str.replace(/(\W)|(\_)/g, '').toLowerCase();
  for (let i in newstr) {
    if (newstr[i] != newstr[newstr.length - 1- i]) {
      return false
      }
  }
  return true;
}



console.log(palindrome("e -ye"));