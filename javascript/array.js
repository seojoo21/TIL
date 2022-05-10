'user strict'

const arr1 = new Array();
const arr2 = [1,2];

const fruits = ['apple','banana']
fruits.push()
console.log(fruits);

fruits.splice(1,1,'watermelon','grape');
console.log(fruits);

const fruits2 = ['pear', 'cacao'];
const newFruits = fruits.concat(fruits2);
console.log(newFruits);

console.clear();
console.log(fruits.includes('apple'));