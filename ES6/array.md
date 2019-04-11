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
