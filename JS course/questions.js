//  Вопрос четыертый. Вот эти методы.... В первую очередь map и reduce.
//  Что за методы, как работают разобрать 1-2 примера.
//
// Some commonly used functions are
// - map
// - filter
// - reduce
// - find
// - findIndex


// Вопрос. Что такое прототип (как отвечать на собеседовании).
// И что тут происходит? наследование...
function Animal() { }

Animal.prototype = {
  constructor: Animal,
  eat: function() {
    console.log("nom nom nom");
  }
};

function Dog() { }

Dog.prototype = Object.create(Animal.prototype);
let beagle = new Dog();// И что такое промисы.
