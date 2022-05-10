'use strict';

const obj1 = {};
const obj2 = new Object();

const ellie = {
    name : 'ellie',
    age : 4
}

function print(person){
    console.log(person.name);
    console.log(person.age);
}

print(ellie);

ellie.hasJob = true;
console.log(ellie.hasJob);

delete ellie.hasJob;
console.log(ellie.hasJob);

console.log(ellie.name);
console.log(ellie['name']);

function printValue(obj, key){
    // console.log(obj.key); // undefined
    console.log(obj[key]);
}

printValue(ellie, 'age');

function Person(name, age){
    this.name = name;
    this.age = age;
}

let wndud = new Person('wndud', 10);
console.log(wndud);

console.log('name' in ellie);
console.log('age' in ellie);
