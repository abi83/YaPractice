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

function countOnline(usersObj) {
  let result = 0;
  for (let user in usersObj) {
    if (usersObj[user].online === true) {
      result++;
    }
  }
  return result;
}
console.log(countOnline(users))


function getArrayOfUsers(obj) {
  for (let item in Object.keys(obj))
  {console.log(item)}
}

console.log(getArrayOfUsers(users));


let dog = {
  name: "Spot",
  numLegs: 4,
  sayLegs: () => {return `This dog has ${this.numLegs} legs.`},
  sayLegs2: function() {return "This dog has " + this.numLegs + " legs.";},

};

console.log(dog.sayLegs()); //This dog has undefined legs.
console.log(dog.sayLegs2());//This dog has 4 legs.

