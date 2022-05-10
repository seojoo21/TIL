'use strict'

// async & await
// clear style of using promise :)

// 0. promise 
// function fetchUser(){
//     return new Promise((resolve, reject)=>{
//         // do network request in 10secs....
//         resolve('ellie');
//     })
// }

// 1. async (from promise to async)
async function fetchUser(){
    // do network request in 10secs....
    return 'ellie';
}

const user = fetchUser();
user.then(console.log)
console.log(user);


// 2. await
function delay(ms) {
    return new Promise(resolve => setTimeout(resolve,ms));
}

async function getApple(){
    await delay(1000);
    return '🍎';
}

async function getBanana(){
    await delay(1000);
    return '🍌';
}
// async function getBanana()와 동일한 작업을 함 
// function getBanana(){
//     return delay(3000).then(()=>'🍌')
// }

// Promise를 사용했지만 콜백 지옥 같은 현상이 발생  
// function pickFruits(){
//     return getApple().then(apple=> {
//         return getBanana().then(banana => `${apple} + ${banana}`);})
// }

async function pickFruits(){
    const apple = await getApple();
    const banana = await getBanana();
    return `${apple} + ${banana}`;
}
pickFruits().then(console.log);

// 위의 코드의 경우 getApple() 1초 후 getBanana()가 실행되어 총 2초가 걸린다. 
// getApple과 getBanana의 경우 서로 관련이 없기 때문에 굳이 기다려줄 필요가 없음 
// 따라서 아래와 같이 Promise를 이용해 getBanana가 getApple을 기다릴 필요 없이 
// 즉 병렬적으로 바로 실행될 수 있도록 코드를 개선해볼 수 있다. 

async function pickFruits2(){
    // 프로미스륾 만드는 순간 프로미스 안에 들어있는 코드 블럭이 실행된다. 
    const applePromise = getApple(); 
    const bananaPromise = getBanana();

    // 동기화 시작 -> 1초만에 병렬적으로 실행 
    const apple = await applePromise; 
    const banana = await bananaPromise;
    return `${apple} + ${banana}`;
}
pickFruits2().then(console.log);

// 그러나 실제로 병렬적으로 기능을 수해할 때 위와 같이 코드를 작성하지 않고 아래와 같이 Promise API를 사용한다.

// 3. useful Promise APIs : Promise.all()
function pickAllFruits(){
    return Promise.all([getApple(), getBanana()])
    .then(fruits => fruits.join(' + '));
}

pickAllFruits().then(console.log);

// 3. usefult Promise APIs : Promise.race() -> 가장 먼저 값을 return하는 아이만 값이 전달이 되어진다.  
async function getOrange(){
    await delay(2000);
    return '🍊';
}

async function getPeach(){
    await delay(1000);
    return '🍑';
}

function pickOnlyOne(){
    return Promise.race([getOrange(), getPeach()]);
    // 가장 먼저 값을 return하는 아이만 (getPeach()) 값이 전달이 되어진다. 
}

pickOnlyOne().then(console.log);