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

Dog.prototype = Animal.prototype;
let beagle = new Dog();
// console.log(beagle.eat())

class Animal1 {
  name = "ANimal";
  eat = function() {
    console.log(`${this.name} nom nom nom`);
  }
}
const dog = {
  name: 'Doggy'
}
class Cat extends Animal1 {
  name = "Cat";
}

var cat = new Cat();
// cat.eat();

// console.log(Object.keys(Cat.prototype));
const catEat = cat.eat.bind(dog).bind(cat);
catEat();

// Вопрос 2. Что такое промисы, пример надо какой-то, может самый простой.
// Вопрос 3. Как дебажить ???
// Вопрос 4. Что такое "use strict";
// Вопрос 5. Кодестайл. на примере:
// https://github.com/abi83/YaPractice/blob/master/JS%20course/Projects/cash_register.js
