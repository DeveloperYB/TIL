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
// Math.round(x);   -   x의 반올림
Math.round(2.2); // 2
Math.round(2.8) // 3
Math.round(-3.2) // -3
Math.round(-3.8) // -4
// Math.min(x1, x2,...);    -   매개변수 중 최소값
Math.min(-1, 2, 4, 5); // -1
Math.min(20, 12, 9, 30); // 9
// Math.max(x1, x2,...);
Math.max(20, 100, 300); // 300
Math.max(1, 2, 3, -9, 20); // 20
```

## 난수 생성

자바스크립트에서는 난수를 생성을 `Math.random()`을 사용한다.\
이 함수는 0 이상 ~ 1 미만의 수를 반환 한다. 다른 범위의 난수를 반환하는 간편 매서드는 없기 때문에 특정 공식을 이용해서 만들게 된다.

```js
// 0 이상 1 미만
Math.random();
// x 이상 y 미만 (실수)
x + (y-x)*Math.random();
// m 이상 n 미만의 정수
m + Math.floor( (n-m)*Math.random() );
// m 이상 n 이하의 정수
m + Math.floor( (n-m+1)*Math.random() );
```