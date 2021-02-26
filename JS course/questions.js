// Вопрос 1. Что такое прототип (как отвечать на собеседовании).
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
let beagle = new Dog();


// Вопрос 2. Что такое промисы, пример надо какой-то, может самый простой.
// Вопрос 3. Как дебажить ???
// Вопрос 4. Что такое "use strict";
// Вопрос 5. Кодестайл. на примере:
// https://github.com/abi83/YaPractice/blob/master/JS%20course/Projects/cash_register.js
