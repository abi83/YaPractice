//Convert the given number into a roman numeral.


function convertToRoman(num) {
let converter = [
    {'base': 1000, 'digits': 0, 'remainder': 0, 'symbol': 'M'},
    {'base': 500, 'digits': 0, 'remainder': 0, 'symbol': 'D'},
    {'base': 100, 'digits': 0, 'remainder': 0, 'symbol': 'C'},
    {'base': 50, 'digits': 0, 'remainder': 0, 'symbol': 'L'},
    {'base': 10, 'digits': 0, 'remainder': 0, 'symbol': 'X'},
    {'base': 5, 'digits': 0, 'remainder': 0, 'symbol': 'V'},
    {'base': 1, 'digits': 0, 'remainder': 0, 'symbol': 'I'},
]
let remainder = num
let answer = ''
for (let item of (converter)){
    //console.log('rank', item.base, 'digits', Math.trunc(remainder / item.base))
    item.digits = Math.trunc(remainder / item.base);
    item.remainder = remainder %item.base;
    remainder= num %item.base;
}
console.log(converter)

for (let index=0; index<converter.length; index++){
    if (converter[index].digits<=3){
    answer += converter[index].symbol.repeat(converter[index].digits);}
    else if (converter[index].digits===4&&converter[index-1].digits===1) {
    answer = answer.slice(0, -1);
    answer += (converter[index].symbol + converter[index-2].symbol);
    }
    else if (converter[index].digits===4&&converter[index-1].digits===0) {
    answer += (converter[index].symbol + converter[index-1].symbol);
    }
    else return 'Smth is wrong'
    //console.log(item.symbol.repeat(item.digits));
}
console.log(answer);


 return answer;
}

convertToRoman(29);