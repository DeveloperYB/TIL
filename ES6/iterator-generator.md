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

