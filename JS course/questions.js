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
// Вопрос 3. Как работает try...catch на примере с делением нуля
// Вопрос 4. typeof - для объектов и массивов выдает "object".
// Есть ли шанс узнать что у меня - объект или массив
// Вопрос 5. Как дебажить ???
// Вопрос 6. Что такое "use strict";
// Вопрос 7. Кодестайл. на примере:
// https://github.com/abi83/YaPractice/blob/master/JS%20course/Projects/cash_register.js
