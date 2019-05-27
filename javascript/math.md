# Map & Set

## 고정 소수점
소주점 뒤 자릿수를 지정하는 형식을 원할 경우 (반올림)
```js
const x = 29.9898;
x.toFixed(3); // 29.990
x.toFixed(2); // 29.99
x.toFixed(1); // 30.0
x.toFixed(0); // 30
```

## 절댓값, 부호, 배열의 최소 값/최대 값 등 숫자 관련 기타 함수
```js
// Math.abs(x);     -   x의 절대값
Math.abs(-5.5); // 5.5
Math.abs(5.5); // 5.5
// Math.sign(x);    -   x 의 부호. x가 음수면 -1, 양수면 1, 0이면 0
Math.sign(-12.42); // -1
Math.sign(1232); // 1
Math.sign(0); // 0
// Math.ceil(x);    -   x의 올림
Math.ceil(3.24); // 4
Math.ceil(-4.98); // -4
// Math.floor(x);   -   x의 내림
Math.floor(12.8); // 12
Math.floor(-9.2); // -10
// Math.trunc(x);   -   x의 소수점 버림
Math.trunc(29.2123123); // 29
Math.trunc(-3.3333); // -3
```