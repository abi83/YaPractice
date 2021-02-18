// Return the lowest index at which a value (second argument) should be inserted
// into an array (first argument) once it has been sorted. The returned value
// should be a number.
// For example, getIndexToIns([1,2,3,4], 1.5) should return 1 because it is
// greater than 1 (index 0), but less than 2 (index 1).
//
// Likewise, getIndexToIns([20,3,5], 19) should return 2 because once the array
// has been sorted it will look like [3,5,20] and 19 is less than 20 (index 2)
// and greater than 5 (index 1).

arr = [1,2,4,5];
num = 3;
f = function (element, index, arr) {
  return element > num;
}

console.log(arr.findIndex((element, index, arr) => element > num));

//iterate through object


let users = {
  Alan: {
    age: 27,
    online: false
  },
  Jeff: {
    age: 32,
    online: true
  },
  Sarah: {
    age: 48,
    online: false
  },
  Ryan: {
    age: 19,
    online: true
  }
};



function getArrayOfUsers(obj) {
  for (let item in Object.keys(obj))
  {console.log(item)}
}
getArrayOfUsers(users);

//output:
// 0
// 1
// 2
// 3


// this ?
let dog = {
  name: "Spot",
  numLegs: 4,
  sayLegs: () => {return `This dog has ${this.numLegs} legs.`}
};

console.log(dog.sayLegs()); //This dog has undefined legs.
