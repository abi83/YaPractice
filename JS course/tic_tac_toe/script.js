////const one = document.querySelector("one");
//let two = document.getElementsByClassName("two");
////const three = document.getElementById("three");
////
////console.log('querySelector', one);
//console.log('getElementsByClassName', two);
////console.log('getElementById',three);
//
//
////const masterEl = document.getElementById('master')
////console.log(masterEl)

function howMany(...args) {
  return "You have passed " + args.length + " arguments.";
}
console.log(howMany(0, 1, 2)); // You have passed 3 arguments.
console.log(howMany("string", null, [1, 2, 3], { })); // You have passed 4 arguments.