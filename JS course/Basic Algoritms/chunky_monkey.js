// Write a function that splits an array (first argument) into groups the length
// of size (second argument) and returns them as a two-dimensional array.


function chunkArrayInGroups(arr, size) {
  let output = [];
  for (let i=0; i < arr.length / size; i++) {
    output.push(Array.from(
        arr.slice(size*i, size*(i+1))
    ))
  }
  return output;
}

x = chunkArrayInGroups([0, 1, 2, 3, 4, 5], 4);
console.log(x);


let myNestedArray = [
  // Only change code below this line
    [
      'unshift',
      [false, 1, 2, 3,],
      'complex',
      'nested'
    ],
    ['loop',
      [
        'shift',
        'deep',
        [
          'deeper',
          6,
          [
            'deepest',
            7,
            1000,
            'method'
          ],
        ],
      ],
    ],
    ['concat', false, true, 'spread', 'array'],
    ['mutate', 1327.98, 'splice', 'slice', 'push'],
    ['iterate', 1.3849, 7, '8.4876', 'arbitrary', 'depth'],
  // Only change code above this line
];