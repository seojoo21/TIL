'use strict'

class UserStorage {

    //setTimeout 재사용 
    delay(ms){
        return new Promise((resolve, reject)=>{setTimeout(resolve,ms)});
    }

    async loginUser(id, password) {
        await this.delay(2000);
        if(
            (id === 'ellie' && password == 'dream') || 
            (id === 'coder' && password === 'academy')
           ){
               return id;
           } else {
               throw (new Error('not found'));
           }
        }

    async getRoles(user){
        await this.delay(2000);
        if(user === 'ellie') {
            return({name:'ellie', role:'admin'});
        } else {
            throw(new Error('no access'));
        }
    }
}

const userStorage = new UserStorage();
const id = prompt('enter your id');
const password = prompt('enter your password');


userStorage
.loginUser(id,password)
.then(user => userStorage.getRoles(user))
.then(user => alert(`Hello ${user.name}, you have a ${user.role} role`))
.catch(console.log);

