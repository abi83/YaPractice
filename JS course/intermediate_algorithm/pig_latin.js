/*
Pig Latin is a way of altering English Words. The rules are as follows:

- If a word begins with a consonant, take the first consonant or
consonant cluster, move it to the end of the word, and add "ay" to it.
- If a word begins with a vowel, just add "way" at the end.
 */

function translatePigLatin(str) {
  const consonants = str.match(/^[bcdfghjklmnpqrstvwxyz]+/)
  const vowels  = str.match(/^[aeiou]+/)
  if (consonants) {
    return str.substring(consonants[0].length) + consonants[0] + 'ay'
  } else if (vowels) {
    return str + 'way'
  }
}
console.log(
  translatePigLatin("rhythm")
);