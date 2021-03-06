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
    return '๐';
}

async function getBanana(){
    await delay(1000);
    return '๐';
}
// async function getBanana()์ ๋์ผํ ์์์ ํจ 
// function getBanana(){
//     return delay(3000).then(()=>'๐')
// }

// Promise๋ฅผ ์ฌ์ฉํ์ง๋ง ์ฝ๋ฐฑ ์ง์ฅ ๊ฐ์ ํ์์ด ๋ฐ์  
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

// ์์ ์ฝ๋์ ๊ฒฝ์ฐ getApple() 1์ด ํ getBanana()๊ฐ ์คํ๋์ด ์ด 2์ด๊ฐ ๊ฑธ๋ฆฐ๋ค. 
// getApple๊ณผ getBanana์ ๊ฒฝ์ฐ ์๋ก ๊ด๋ จ์ด ์๊ธฐ ๋๋ฌธ์ ๊ตณ์ด ๊ธฐ๋ค๋ ค์ค ํ์๊ฐ ์์ 
// ๋ฐ๋ผ์ ์๋์ ๊ฐ์ด Promise๋ฅผ ์ด์ฉํด getBanana๊ฐ getApple์ ๊ธฐ๋ค๋ฆด ํ์ ์์ด 
// ์ฆ ๋ณ๋ ฌ์ ์ผ๋ก ๋ฐ๋ก ์คํ๋  ์ ์๋๋ก ์ฝ๋๋ฅผ ๊ฐ์ ํด๋ณผ ์ ์๋ค. 

async function pickFruits2(){
    // ํ๋ก๋ฏธ์ค๋ฅพ ๋ง๋๋ ์๊ฐ ํ๋ก๋ฏธ์ค ์์ ๋ค์ด์๋ ์ฝ๋ ๋ธ๋ญ์ด ์คํ๋๋ค. 
    const applePromise = getApple(); 
    const bananaPromise = getBanana();

    // ๋๊ธฐํ ์์ -> 1์ด๋ง์ ๋ณ๋ ฌ์ ์ผ๋ก ์คํ 
    const apple = await applePromise; 
    const banana = await bananaPromise;
    return `${apple} + ${banana}`;
}
pickFruits2().then(console.log);

// ๊ทธ๋ฌ๋ ์ค์ ๋ก ๋ณ๋ ฌ์ ์ผ๋ก ๊ธฐ๋ฅ์ ์ํดํ  ๋ ์์ ๊ฐ์ด ์ฝ๋๋ฅผ ์์ฑํ์ง ์๊ณ  ์๋์ ๊ฐ์ด Promise API๋ฅผ ์ฌ์ฉํ๋ค.

// 3. useful Promise APIs : Promise.all()
function pickAllFruits(){
    return Promise.all([getApple(), getBanana()])
    .then(fruits => fruits.join(' + '));
}

pickAllFruits().then(console.log);

// 3. usefult Promise APIs : Promise.race() -> ๊ฐ์ฅ ๋จผ์  ๊ฐ์ returnํ๋ ์์ด๋ง ๊ฐ์ด ์ ๋ฌ์ด ๋์ด์ง๋ค.  
async function getOrange(){
    await delay(2000);
    return '๐';
}

async function getPeach(){
    await delay(1000);
    return '๐';
}

function pickOnlyOne(){
    return Promise.race([getOrange(), getPeach()]);
    // ๊ฐ์ฅ ๋จผ์  ๊ฐ์ returnํ๋ ์์ด๋ง (getPeach()) ๊ฐ์ด ์ ๋ฌ์ด ๋์ด์ง๋ค. 
}

pickOnlyOne().then(console.log);