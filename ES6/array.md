## 배열

[요약 바로가기](./#요약)

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

---

## 배열 검색

#### indexOf, lastIndexOf
```js
const o = {name:'wabi',age:29};
const arr = [1,5,'a',o,true,5,[1,2],'9'];
arr.indexOf(5); // 1
arr.lastIndexOf(5) // 5
arr.indexOf('a') // 2
arr.lastIndexOf('a') // 2
arr.indexOf({name:'wabi',age:29}) // -1
arr.indexOf(o) // 3
arr.indexOf([1,2]) // -1
arr.indexOf('9') //7
arr.indexOf(9) // -1

arr.indexOf('a',5) // -1
arr.indexOf(5,5) // 5
arr.lastIndexOf(5,4) // 1
arr.lastIndexOf(true,3) // -1
```

#### findIndex
```js
const arr = [{id:5,name:'Wabi'},{id:6,name:'Yuna'}];
arr.findIndex( o => o.id === 6); // 1
arr.findIndex( o => o.name === 'Francis'); // -1
arr.findIndex( o => o.name === 'Wabi'); // 0
```

#### find
> 하단코드 예시) index 3 이상, 거듭제곱수 구하기
```js
const arr = [1,17,16,7,4,16,10,3,49];
arr.find((x,i) => i >= 3 && Number.isInteger(Math.sqrt(x))); // 4
```
> Math.sqrt : 제곱근을 반환 \
Number.isInteger : 정수 상황 Boolean

#### find (with this)
```js
class Person {
    constructor(name){
        this.name = name;
        this.id = Person.nextId++;
    }
}
Person.nextId = 0;
const Wabi = new Person('Wabi'),
Yuna = new Person('Yuna'),
Yuri = new Person('Yuri'),
Zinico = new Person('Zinico'),
Suk = new Person('Suk');

const arr = [Wabi,Yuna,Yuri,Zinico,Suk];

// 방법 1 : ID 를 직접 비교하는 방법
arr.find(p => p.id === Wabi.id); // Wabi 객체 반환

// 방법 2 : "this" 매개변수를 이용하는 방법
arr.find(function(p){
    return p.id === this.id
},Yuna); // Yuna 객체 반환
```

#### some, every

```js
const arr = [5,7,29,12,3,19];
arr.some(x => x%2 === 0); // true; 12 는 짝수
arr.some(x => Number.isInteger(Math.sqrt(x)) ); // false; 제곱수가 없습니다.
```

```js
const arr = [4,6,16,36];
arr.every(x => x%2 === 0); // true; 홀수가 없습니다.
arr.every(x => Number.isInteger(Math.sqrt(x)) ); // false;  6은 제곱수가 아닙니다.
```
---
## map, filter

```js
const people = [
    {name : 'Wabi', age : 29, gender : 'male'},
    {name : 'Yuna', age : 30, gender : 'female'}
];
const names = people.map(x => x.name); // ['Wabi','Yuna']
const genders = people.map(x => x.gender); // ['male','female']
const ages = people.map(x => x.age); // [29,30]
const nextAges = people.map(x => x.age + 1); // [30,31]

const newPeople = names.map((x,i)=>({
    name : x,
    age : ages[i],
    nextAge : nextAges[i],
    gender : genders[i]
})); // 이렇게 다시 합치는 용도로 쓸 일은 없지만... ㅎㅎ
```

```js
const cards = [];
for(let suit of ['H','C','D','S']){
    for(let val = 1; val <= 13; val++){
        cards.push({val,suit});
    }
}

//val === 2
cards.filter( c => c.val === 2);
/*
[
    {suit : 'H' , val : 2},
    {suit : 'C' , val : 2},
    {suit : 'D' , val : 2},
    {suit : 'S' , val : 2}
]
*/
```
---
## reduce

```js
const arr = [5,10,5,5];
//초기값 설정
const sum = arr.reduce((a,x) => a += x, 0); // 25
//초기값 미설정시, idx 0 을 참조.
const sum = arr.reduce((a,x) => a += x); // 25
```
> MDN web docs 참조 : https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Array/Reduce

```js
const words = ['Hi','My','name','is','Youbeen Kim','Just call','me','Wabi','Thx'];
const alphabets = words.reduce((a,x)=>{
    let fx = x[0].toUpperCase();
    if(!a[fx]) a[fx] = [];
    a[fx].push(x);
    return a;
},{});
/*
{
    "H":["Hi"],
    "M":["My","me"],
    "N":["name"],
    "I":["is"],
    "Y":["Youbeen Kim"],
    "J":["Just call"],
    "W":["Wabi"],
    "T":["Thx"]
}
*/
```
---
## 문자열 병합 

```js
const attributes = ['Nim','HiYo','Nanun','Wabi'];
const html = `<ul><li>`+attributes.join(`</li><li>`)+`</li></ul>`;
```
---
## 요약

#### 배열 함수의 매개변수(순서대로)
|메서드|설명|
|---|---|
|reduce에만 적용|누적값, 초깃값 또는 마지막 호출에서 반환한 값|
|모든 메서드|요소 (현재 요소의 값)|
|모든 메서드|현재 요소의 인덱스|
|모든 메서드|배열 자체 (그다지 쓸모없음)|

#### 배열 콘텐츠 조작

---
