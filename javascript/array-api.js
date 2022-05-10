'user strict'

// Q1. make a string out of an array
  const fruits = ['apple', 'banana', 'orange'];
  fruits.forEach(elem => {
      console.log(elem);
  });
  
  // Q2. make an array out of a string
  const fruits2 = '🍎, 🥝, 🍌, 🍒';
  const fruitBasket = [];
  fruitBasket.push(fruits);
  fruitBasket.forEach(elem => {
      console.log(elem);
  });
  
  // Q3. make this array look like this: [5, 4, 3, 2, 1]
  const array = [1, 2, 3, 4, 5];
  array.reverse();
  console.log(array);
  
  // Q4. make new array without the first two elements
  const array2 = [1, 2, 3, 4, 5];
  const array3 = [];
  array2.splice(0,2);
  array3.push(array2);
  array3.forEach(elem=>{
      console.log(elem);
  });

  class Student {
    constructor(name, age, enrolled, score) {
      this.name = name;
      this.age = age;
      this.enrolled = enrolled;
      this.score = score;
    }
  }
  const students = [
    new Student('A', 29, true, 45),
    new Student('B', 28, false, 80),
    new Student('C', 30, true, 90),
    new Student('D', 40, false, 66),
    new Student('E', 18, true, 88),
  ];
  
  // Q5. find a student with the score 90
  for(let i=0; i<students.length; i++){
    if (students[i].score === 90) {
        console.log(students[i]);
    }
  } 

  // Q6. make an array of enrolled students
  const enrolledStudents = [];

  for(let i=0; i<students.length; i++){
      if(students[i].enrolled === true){
          enrolledStudents.push(students[i]);
      }
  }

  console.log(enrolledStudents);

  // Q7. make an array containing only the students' scores
  // result should be: [45, 80, 90, 66, 88]
  const scores = [];
  for(let student of students){
    scores.push(student.score);
  }
  console.log(scores);

  // Q8. check if there is a student with the score lower than 50
  const result = students.filter(students => students.score < 50);
  console.log(result);
  
  // Q9. compute students' average score
  let sum = 0;

  for (let student of students){
    sum += student.score;
  }
  const avg = sum / students.length;
  console.log(avg); 
  
  // Q10. make a string containing all the scores
  // result should be: '45, 80, 90, 66, 88'
  const result2 = scores.toString();
  console.log(result2);

  // Bonus! do Q10 sorted in ascending order
  // result should be: '45, 66, 80, 88, 90'
  const result3 = scores.sort();
  const result4 = result3.toString();
  console.log(result4);