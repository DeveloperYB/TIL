## 배열 Array

> 자바스크립트는 루비 같은 언어와 다르게 (str.downcase, str.downcase!) 함수이름만 봐서는 대상 자체를 수정하는지, 아니면 새로운 것을 반환 하는지 모른다... 그러니 외우자....
---

## 처음 || 끝, 요소 하나 추가 || 제거
push, unshift 새 요소를 추가한 늘어난 길이 반환 \
pop, shift 제거된 요소를 반환

```js
const arr = ['w','a','b','i'];
arr.push('zzang'); // 5
//arr = ['w','a','b','i','zzang']

arr.pop(); // 'zzang'
//arr = ['w','a','b','i']

arr.unshift('Mr'); // 5
//arr = ['Mr','w','a','b','i']

arr.shift(); // 'Mr'
//arr = ['w','a','b','i']
```

---

## 배열의 끝에 여러 요소 추가
> concat 매서드 적용 이후 사본을 반환

```js
const arr = [1,2,3];
arr.concat(4,5,6); //[1,2,3,4,5,6] arr은 안바뀐다.
arr.concat([4,5,6]); //[1,2,3,4,5,6] arr은 안바뀐다.
arr.concat(4,[5,6]); //[1,2,3,4,5,6] arr은 안바뀐다.
arr.concat([4,5],6); //[1,2,3,4,5,6] arr은 안바뀐다.
arr.concat([4,[5,6]]); //[1,2,3,4,[5,6]] arr은 안바뀐다.
```
> concat은 제공받은 배열을 단 한번만 분해 한다.

---

## 배열 일부 가져오기

```js
const arr = [1,2,3,4,5];
arr.slice(3); // [4,5] arr은 안바뀐다.
arr.slice(2,4); // [3,4] arr은 안바뀐다.
arr.slice(-2); // [4,5] arr은 안바뀐다.
arr.slice(1,-2); // [2,3] arr은 안바뀐다.
arr.slice(-2,-1); // [4] arr은 안바뀐다.
```

---

## 임의의 위치에 요소 추가 || 제거

```js
const arr = [1,5,7];
arr.splice(1,0,2,3,4); // arr은 이제 [1,2,3,4,5,7]
arr.splice(5,0,6); // arr은 이제 [1,2,3,4,5,6,7]
arr.splice(1,2); // arr은 이제 [1,4,5,6,7]
arr.splice(2,1,'a','b'); // arr은 이제 [1,4,'a','b',6,7]
```

---

## 배열 안 요소 교체

> ES6 에서 도입한 새로운 메서드

```js
const arr = [1,2,3,4];
arr.copyWithin(1,2); // arr은 이제 [1,3,4,4]
arr.copyWithin(2,0,2); // arr은 이제 [1,3,1,3]
arr.copyWithin(0,-3,-1); // arr은 이제 [3,1,1,3]
```

---

## 특정 값으로 배열 채우기

> ES6 에서 도입한 새로운 메서드

```js
const arr = new Array(5).fill(1); // arr이 [1,1,1,1,1] 로 초기화
arr.fill('a'); // arr은 이제 ['a','a','a','a','a']
arr.fill('b',1); // arr은 이제 ['a','b','b','b','b']
arr.fill('c',2,4); // arr은 이제 ['a','b','c','c','b']
arr.fill(5.5,-4); // arr은 이제 ['a',5.5,5.5,5.5,5.5]
arr.fill(0,-3,-1); // arr은 이제 ['a',5.5,0,0,5.5]
```

---

## 배열 정렬과 역순 정렬

```js
const arr1 = [1,2,3,4,5];
arr1.reverse(); // arr은 이제 [5,4,3,2,1]

const arr2 = [5,3,2,4,1];
arr2.sort(); // arr은 이제 [1,2,3,4,5];

const arr3 = [
    {name : 'Suzanne'},
    {name : 'Jim'},
    {name : 'Trevor'},
    {name : 'Amanda'},
];

arr3.sort(); // 값 무변동
arr3.sort((a,b)=>a.name > b.name); // arr은 name 프로퍼티의 알파벳 순으로 정렬
arr3.sort((a,b)=>a.name[1] < b.name[1]); // arr은 name 프로퍼티의 두 번째 글자의 알파벳 역순으로 정렬
```