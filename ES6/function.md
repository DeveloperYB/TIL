#함수와 추상적 사고

## 서브루틴

서브루틴은 오래된 개념이고 복잡한 코드를 `간단하게 만드는 기초적인 수단이다.`

> 서브루틴은 procedure, routine, subprogram, macro 등 다양한 이름으로 불려지고, 자바스크립트에서는 함수 또는 메서드라고 불러진다.

### 서브루틴 === 알고리즘 ?

```js
const hour = new Date().getHours();
const eat = {
    breakfast : false,
    lunch : false,
    dinner : false
};
if(8<=hour && hour <= 9) eat.breakfast = true;
else if(12<=hour && hour <= 13) eat.lunch = true;
else if(18<=hour && hour <= 19) eat.dinner = true;
else{
    eat.breakfast = false;
    eat.lunch = false;
    eat.dinner = false;
}
```

> 위 코드를 서브루틴('이하 함수 : Javascript')로 표현하면, (하단코드)

```js
function mealTime(){
    const hour = new Date().getHours();
    const eat = {
        breakfast : false,
        lunch : false,
        dinner : false
    };
    if(8<=hour && hour <= 9) eat.breakfast = true;
    else if(12<=hour && hour <= 13) eat.lunch = true;
    else if(18<=hour && hour <= 19) eat.dinner = true;
    else{
        eat.breakfast = false;
        eat.lunch = false;
        eat.dinner = false;
    }
    return eat;
}
```

> 함수는 10번,100번 재사용될 반복성코드를 하나로 나타낸다.\
함수의 이름은 `최대한 다른 사람이 함수이름만 봐도 이해할 수 있도록 핵심요소`를 나타낸 이름 이어야 한다.

## 이터레이터 사용하기 (with 클로저)

```js
const colors = ['red','orange','yellow','green','blue','indigo','violet'];
let colorIdx = -1;
function getNextRainbowColor(){
    if(++colorIdx >= colors.length) colorIdx = 0;
    return colors[colorIdx];
}
```

> 위 함수의 결과가 항상 다른점, `colorIdx`가 `getNextRainbowColor` 함수에 속하지 않는데도 함수를 호출하면 변수가 바뀌는 부수적인 효과가 일어나는점, 이 2가지가 `순수한 함수`라는 정의를 어긴다. (같은 변수에는 같은 결과값)

#### 1. 클로저 이용해서 함수안에 변수를 넣기

```js
const getNextRainbowColor = (function(){
    const colors = ['red','orange','yellow','green','blue','indigo','violet'];
    let colorIdx = -1;
    return function(){
        if(++colorIdx >= colors.length) colorIdx = 0;
        return colors[colorIdx];
    };
})();
```

> 하지만 입력이 같아도 결과가 다르기 때문에 순수 함수라고 볼 수 없다.\
만약 위 함수 `getNextRainbowColor`를 다른곳에서도 사용한다고하면, 결과값에 영향을 끼치게 되므로 부수적인 효과가 아직도 일어난다.

#### 2. 이터레이터 이용하기

```js
function getNextRainbowColor(){
    const colors = ['red','orange','yellow','green','blue','indigo','violet'];
    let colorIdx = -1;
    return {
        next(){
            if(++colorIdx >= colors.length) colorIdx = 0;
            return {val : colors[colorIdx], done : false}
        }
    };
}
```

> 위 코드의 `getNextRainbowColor`함수는 순수한 함수이다.\
항상 같은 것을 반환 하기 때문에 안전하다. 결국에는 next() 메서드도 매번 다른 값을 반환하기 때문에 순수한 함수가 아니다? 라고 할 수도 있지만, 반환 자체가 메서드라는 점, 자신이 속한 객체 안에서 동작하기 때문에 `getNextRainbowColor` 함수를 다른곳에 또 호출하더라도 독립적인 이터레이터가 생성된다. (= 다른 이터레이터를 침범하지 않는다.)

---

## DRY ('Don't repeat yourself')

코드를 하나로 묶어서 반복을 피한다는 개념이 중요하다.\
순수한 함수를 쓰면 코드를 테스트하기 쉽고, 이해하기도 쉽고, 재사용하기도 더 쉽다.