//test data
bracketTests = {
  '{}()[]': true,
  '{}}': false,
  ')(': false,
  '([)]': false,
}

const bracketTest = function(sequence) {
  const pairs_to_close = {
    '}': '{',
    ')': '(',
    ']': '[',
  };
  let unclosed_brackets = '';
  for (let symbol of sequence) {
    if ('([{'.includes(symbol) || unclosed_brackets === '') {
      unclosed_brackets += symbol
    }
    if (
      ')]}'.includes(symbol)
      && unclosed_brackets[unclosed_brackets.length - 1] === pairs_to_close[symbol]) {
        unclosed_brackets = unclosed_brackets.slice(0, -1)
    }
  };

  return unclosed_brackets === ''
}

//running tests
for (let testCase in bracketTests){
  console.log(
      bracketTest(testCase) === bracketTests[testCase]? 'Test passed': 'Test failed'
  )
}