## IIFE (즉시 호출 함수표현)

> ES6에서 블록 스코프 변수를 도입하면서 아래 같은 코드가 필요한 경우가 많이 줄었다.

```js
const f = (function(){
    let count = 0;
    return function(){
        return `I have been called ${++count} time(s).`
    }
})();

f();        // "I have been called 1 time(s)."
f();        // "I have been called 2 time(s)."
```
---
## 함수 호이스팅

```js
f();            // 'f'
function(){
    console.log('f');
}
```

```js
f();            // ReferrenceError: f 는 정의되지 않았습니다.
let f = function(){
    console.log('f');
}
```
---
## Temporal dead zone (사각지대)

> ES5, 아래 하단 코드 사용 가능.
```js
if(typeof wabi === undefined){
    console.log(false);
}else{
    console.log(true);
}
```

>ES6, let으로 변수 선언하였으므로, 에러 발생
```js
if(typeof wabi === undefined){
    console.log(false);
}else{
    console.log(true);
}
let wabi = 'dev';
```
---
## 클로저

```js
// 1
let globalFunc;
{
    let blockVar = 'a';
    globalFunc = function(){
        console.log(blockVar);
    }
}
globalFunc();           // "a"

// 2
let f;
{
    let o = {note : 'Safe'};
    f = function(){
        return o;
    }
}
let oRef = f();
oRef.note = "Not so safe after all!";
```

> 자신의 스코프에 없는 것들을 접근할 방법 생성.
