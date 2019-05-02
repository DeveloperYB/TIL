# 에러, 그리고 처리

## Error

```js
const email = 'devwabi@gmail.com';

function validateEmail(email){
    return email.match(/@/) ?
        email :
        new Error('invalid email : ${email}')
}

const validatedEmail = validateEmail(email);
if(validatedEmail instanceof Error){
    console.error(`Error : ${validatedEmail.message}`);
}else{
    console.log(`Valid email : ${validatedEmail}`);
}
```

---

## try / catch


```js
function validateEmail(email){
    return email.match(/@/) ?
        email :
        new Error('invalid email : ${email}')
}

const email = null;
try{
    const validatedEmail = validateEmail(email);
    if(validatedEmail instanceof Error){
        console.error(`Error : ${validatedEmail.message}`);
    }else{
        console.log(`Valid email : ${validatedEmail}`);
    }
}catch(err){
    console.error(`Error : ${err.message}`);
}
```

---

## try / catch + finally

```js
try{
    console.log('this line is executed');
    throw new Error('boom')
    console.log('this line is not');
}catch(err){
    console.log('there was an error')
}finally{
    console.log('always executed');
    console.log('perform cleanup here');
}
```

> 에러 발생, 미발생 동리하게 반드시 호출하는 finally

---

> 예상할 수 없는 상황에 대비한 마지노선으로 생각하고 위 예외처리를 쓸것,\
예상할 수 있는 에러는 조건문으로 처리하는 것이 최선!