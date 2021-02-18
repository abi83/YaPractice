var readline = require('readline');
var io_interface = readline.createInterface({input: process.stdin});

let output_numbers = [],
    line_number = 0,
    num_lines;
io_interface.on('line', function (line) {
  if (line_number === 0) {
    num_lines = parseInt(line);
  } else if (line_number <= num_lines) {
    let values = line.split(" ");
    let value_1 = parseInt(values[0]),
        value_2 = parseInt(values[1]);
    let result = value_1 + value_2;
    output_numbers.push(result);
  }
  line_number++;
})

io_interface.on('close', function () {
  if (line_number < 1 + num_lines) {
    // последняя строка была пустой и потому не считана
    // здесь мы могли бы обработать эту ситуацию
  }
  process.stdout.write(output_numbers.join('\n'));
})