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

