# 이터레이터 & 제너레이터

> ES6 에서 이터레이터 & 제너레이터를 도입되었다.\
제너레이터는 이터레이터에 의존하는 개념이다.

## Iterables ?

> 객체는 값이 for..of 구조 내에서 반복되는 것 같은 그 반복 동작을 정의하는 경우 반복이 가능(iterable)하다.\
Array 또는 Map과 같은 일부 내장 형은 기본 반복 동작이 있지만 다른 형(가령 Object)은 없다.

> `내장 iterable`\
String, Array, TypedArray, Map 및 Set은 모두 내장 반복가능 객체, 이 객체들은 프로토타입 객체가 모두 Symbol.iterator 메서드가 있기 때문이다.


```js
const num = [
    1,2,3,4,5
];
const it = num.values();

it.next(); //{value: 1, done: false}
it.next(); //{value: 2, done: false}
it.next(); //{value: 3, done: false}
it.next(); //{value: 4, done: false}
it.next(); //{value: 5, done: false}
it.next(); //{value: undefined, done: true}
```

> 이터레이터 프로토콜은 모든 객체를 이터러블 객체로 바꿀 수 있다.

```js
class Fibonacci{
    [Symbol.iterator](){
        let a = 0, b = 1;
        return {
            next(){
                let rval = {value : b, done :false}
                b += a;
                a = rval.value;
                return rval;
            }
        }
    }
}

const fib = new Fibonacci();
let i = 0;
for(let n of fib){
    console.log(n);
    if(++1 > 9) break;
}
```

## 제너레이터

> 이터레이터를 사용해 자신의 실행을 제어할 수 있는 함수.\
두 가지 새로운 개념을 도입

- 제너레이터는 언제든 호출자에게 제어권을 넘길 수 없다.
- 제너레이터는 호출한 즉시 실행되지는 않는다. 대신 이터레이터를 반환하고 이터레이터의 next 메서드를 호출함으로 실행이 된다.

```js
function* Num(){
    yield 1;
    yield 2;
    yield 3;
    yield 4;
    yield 5;
    yield 6;
}

const it = Num();
it.next(); // {value: , 1 : false}
it.next(); // {value: , 2 : false}
it.next(); // {value: , 3 : false}
it.next(); // {value: , 4 : false}
it.next(); // {value: , 5 : false}
it.next(); // {value: , 6 : false}
it.next(); // {undefined: , 6 : true}
```

> 제너레이터란? 요약\
Generator는 Iterator를 반환하는 함수이다. Generator 함수는 function 다음에 " * "가 추가되고 내부 새로운 키워드인 yield를 사용한다. 별표가 function 바로 앞에 있는지 또는 *와 function 사이에 공백이 있는지는 중요하지 않다.

---

### yield 표현식과 양방향 통신

```js
function *interrogate(){
    const name = yield 'What is your name?';
    const color = yield 'What is your favorite color?'
    return `${name}'s favorite color is ${color}.`;
}

const it = interrogate();
it.next(); // {value:'What is your name?', done:false}
it.next('Wabi'); // {value:'What is your favorite color?', done:false}
it.next('red'); // {value:'Wabi's favorite color is red.', done:true}
```

1. 제너레이터는 화살표 함수로 만들수 없고 반드시 function *을 써야합니다.
2. 제너레이터에서 중요한 값을 절대 return으로 반환하려고 하면 안됩니다. (이유는 하단 코드 참고)

```js
function* abc(){
    yield 'a';
    yield 'b';
    return 'c';
}

const it = abc();
it.next(); // {value : 'a', done : false}
it.next(); // {value : 'b', done : false}
it.next(); // {value : 'c', done : true}

//이렇게 value값이 c 까지 반환은 하지만 done이 true로 반환 될 시, for ... of 루프에서 c는 출력되지 않는다. 이유는 done 이 true 이면 value 프로퍼티에 주의를 기울이지 않기 때문이다.

for(let l of abc()){
    console.log(l);
}
// 'a' 와 'b'는 출력되지만 'c'는 출력되지 않는다.
```
