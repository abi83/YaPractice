var Person = function(firstAndLast) {
  let [first, last] = firstAndLast.split(' ')
  this.getFirstName = function(){
    return first
  }
  this.getLastName = function(){
    return last
  }
  this.getFullName = function() {
    return first + ' ' + last
  };
  this.setFirstName = function(name){
    first = name
  }
  this.setLastName = function(name){
    last = name
  }
  this.setFullName = function(name){
    [first, last] = name.split(' ')
  }

  // return firstAndLast;
};

var bob = new Person('Bob Ross');
console.log(
  bob.getFullName()
);
console.log(Object.keys(bob))