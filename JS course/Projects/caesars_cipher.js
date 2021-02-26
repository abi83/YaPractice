/*
One of the simplest and most widely known ciphers is a Caesar cipher, also
known as a shift cipher. In a shift cipher the meanings of the letters are
shifted by some set amount.

A common modern use is the ROT13 cipher, where the values of the letters are
shifted by 13 places. Thus 'A' ↔ 'N', 'B' ↔ 'O' and so on.

Write a function which takes a ROT13 encoded string as input and returns a
decoded string.
 */
function rot13(str) {
const input = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz';
const output = 'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm';
let answer = ''

for (let symbol of str){
  let index = input.indexOf(symbol);
  if (index >= 0){
    answer += output[index];
  }
  else {
    answer += symbol
  }
  
}
  return answer;
}

rot13("GUR DHVPX OEBJA SBK WHZCF BIRE GUR YNML QBT.");