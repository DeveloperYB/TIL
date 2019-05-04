# 비동기적 프로그래밍

Javascript 는 단일 스레드에서 동작하기 때문에 한 번에 한 가지 일만 할 수 있다. 싱글 스레드 만의 장점으로 멀티스레드 프로그래밍에서 겪어야 하는 골치 아픈 문제들을 신경 안써도 된다는 점이 있지만 사용자 입력이나, 웹 통신 같은 비동기적 관점으로 프로그래밍 하는게 어렵게 느껴지는 점을 단점으로 꼽을 수 있다.

### 비동기적 테크닉 사용 3 가지

- Ajax 호출, 네트워크 통신
- 파일 일고, 쓰기 같은 파일시스템 작업
- 시간을 지연해야하는 기능
---

## 콜백, 프로미스 비유 예시

A형 간염 때문에 사람들이 많이 아프자, 많은 사람들이 예방접종을 하루 빨리 맞기 위해서 보건소에 몰려들었다.

"콜백 보건소" 에서는 사람들이 줄서고 기다리지 않도록, 사람들의 전화번호를 받았다가 차례가 돌아오면 전화를 해준다. (= 콜백 방식)

"프로미스 보건소" 에서는 차례가 되면 진동이 울리는 호출기를 사람들에게 전해준다. (= 프로미스 방식)


### 비유 예시 요약

- 콜백 방식은 차례가 되면 알 수 있도록 수단을 `당사자가 일처리하는 곳에` 넘겨준다.
- 프로미스 방식은 차례가 되면 알 수 있도록 수단을 `일처리하는 곳에서 당사자에게` 넘겨준다.

---

## 자바스크립트 비동기적 프로그래밍 4 가지 패러다임

1. Callback
2. Promise
3. Generator
4. async/await

제너레이터 자체로는 비동기적 프로그래밍을 지원하지 않기 때문에 프로미스나 콜백과 함께 사용해야 한다. 마찬가지로 프로미스도 콜백과 함께 사용해야한다.

---

## 패러다임 1. Callback

### 예시 1)
```js
console.log(`Before setTimeout 5 seconds : HI`);
setTimeout(function(){
    console.log(`After setTimeout 5 seconds : BYE`);
}, 5000); // 5 seconds
console.log("test 1");
console.log("test 2");
```
#### 콘솔로그 결과
```
Before setTimeout 5 seconds : HI
test 1
test 2
After setTimeout 5 seconds : BYE
```
### 예시 2)
```js
let start = 10;
let i = 0;
console.log(`0 : ${start} Sec`);
const intervalId = setInterval(function(){
    let now = --start;
    if(now !== start || ++i > 10){
        return clearInterval(intervalId);
    }
    console.log(`${i} : ${now} Sec`);
},3000);
```
#### 콘솔로그 결과
```
0 : 10 Sec
(3초 뒤)
1 : 9 Sec
(3초 뒤)
2 : 8 Sec
(3초 뒤)
3 : 7 Sec
(3초 뒤)
4 : 6 Sec
(3초 뒤)
5 : 5 Sec
(3초 뒤)
6 : 4 Sec
(3초 뒤)
7 : 3 Sec
(3초 뒤)
8 : 2 Sec
(3초 뒤)
9 : 1 Sec
(3초 뒤)
10 : 0 Sec
```

> 참고 사항.\
setTimeout, setInterval, clearInterval은 모두 전역 객체 (브라우저에서는 window, 노드에서는 global)에 정의되어 있다.

### 오류 우선 콜백 패턴 : Error first callback

콜백을 사용하다보면 예외처리가 어려워질 때가 있다. 그래서 표준을 잡은 방법으로 오류를 우선적으로 처리하는 방법이 오류 우선 콜백 패턴이다. (첫 번째 매개변수에 에러 객체를 쓰는 것)

### 예시 3) Node.js

```js
const fs = require('fs');

const fname = 'wabi_report.txt';
fs.readFile(fname, function(err, data){
    if(err) return console.error(`파일을 읽을 수 없습니다. : ${fname} : ${err.message}`);

    console.log(`${fname} 내용 : ${data}`);
});
```

> 참고 사항.\
위 'Error first callback' 패턴은 프로미스를 사용하지 않을 경우 노드 개발에서는 표준이나 다름없다.

### 예시 4) 콜백의 단점 : 콜백 지옥, Node.js

```js
const fs = require('fs');

fs.readFile('wabi_report_04_27.txt', function(err, dataA){
    if(err) console.error(err);
    fs.readFile('wabi_report_04_28.txt', function(err, dataB){
        if(err) console.error(err);
        fs.readFile('wabi_report_04_29.txt', function(err, dataC){
            if(err) console.error(err);
            fs.readFile('wabi_report_04_30.txt', function(err, dataD){
                if(err) console.error(err);
                setTimeout(function(){
                    fs.writeFile('wabi_report_0427_0430.txt',dataA+dataB+dataC+dataD,function(err){
                        if(err) console.error(err);
                    });
                },60000);
            });
        });
    });
});
```

위 코드는 4/27~30 까지의 리포트.txt 파일을 불러와서 에러가 없을경우
순차적으로 읽은뒤 마지막으로 1분 뒤 파일하나로 합치는 작업을 나타낸다.

---

## 패러다임 2. Promise

위 콜백의 단점인 콜백 지옥을 보완하기 위해서 만들어진 것이 프로미스 이다. 콜백 자체를 대체하는 것은 아니지만 프로미스를 사용함으로써 안전하고 관리하기 쉬운 코드를 만들 수 있다.

### Promise 기본 개념, 

- 프로미스 기반 비동기적 함수 호출하면 Promise 인스턴스를 반환한다.
- 프로미스는 성공 또는 실패 딱 2 가지뿐 이다.
- 성공 또는 실패가 단 한 번만 일어난다.
- 단 한번의 성공 또는 실패로 해당 프로미스는 결정되었다고 한다. (= settled)
- 프로미스는 객체이다. (= 어디든 전달할 수 있다.)
- 성공, 실패의 중간 단계인 10,20,~50% 완료 라는 진행상황 개념이 없다.
- 프로미스는 객체이므로 전달을 통해 처리를 다른 함수에서 하게 할 수 있다.
- 프로미스는 체인으로 연결할 수 있는 장점이 있다.

### 예시 1)

```js
function countdown(seconds){
    return new Promise(function(resolve, reject){
        for(let i = seconds; i >= 0; i--){
            setTimeout(function(){
                if(i > 0) console.log(i + '...');
                else resolve(console.log('The end!'));
            }, (seconds - i)*1000);
        }
    });
}

countdown(5).then(
    function(){
        console.log('success');
    }
);
```
#### 콘솔로그 결과
```
5...
4...
3...
2...
1...
The end!
success
```

### 예시 2) 이벤트 : Node.js

이벤트가 일어나면 이벤트 발생을 담당하는 개체 에서 이벤트가 일어났음을 알린다. 필요한 이벤트는 모두 콜벡을 통해서 주시할 수 있다. 노드에서는 이벤트를 지원하는 모듈 EventEmmitter가 내장되어 있다. (클래스와 함께 하도록 설계되어있으므로, 위 예시 1 코드 countdown 함수를 클래스로 하단 예시코드에서는 바꾼다.)

```js
const EventEmitter = require('events').EventEmitter;

class Countdown extends EventEmitter {
    constructor(seconds, superstitious){
        super();
        this.seconds = seconds;
        this.superstitious = !!superstitious;
    }
    go(){
        const countdown = this;
        const timeoutIds = [];
        return new Promise(function(resolve, reject){
            for(let i = countdown.seconds; i >= 0; i--){
                timeoutIds.push(setTimeout(function(){
                    if(countdown.superstitious && i === 13){
                        // 13 일때는 중지 : 대기중인 타임아웃을 전부 취소.
                        timeoutIds.forEach(clearTimeout);
                        return reject(new Error('WTF ERROR!'));
                    }
                    countdown.emit('tick',i);
                    if(i === 0) resolve();
                }, (countdown.seconds - i)*1000));
            }
        });
    }
}
```

EventEmmitter 를 상속하는 클래스는 이벤트를 발생시킬 수 있다. 카운트다운을 시작하고 프로미스를 반환하는 매서드는 go 부분 내부이다.\
카운트가 13일 경우는 에러를 반환하고, this에 특별한 변수를 넣었기 때문에 해당 this를 통해서 프로미스 내부에서 쓸 수 있다.\
`countdown.emit('tick', i)`는 'tick' 이벤트를 발생시키는 부분이다.

사용은 하단 코드를 참조.

```js
const countFn = new Countdown(5);

countFn.on('tick', function(i){
    if(i > 0) console.log(i + '...');
});
countFn.go().then(function(){
    console.log('The end!');
}).catch(function(err){
    console.error(err.message);
});
```

### 예시 3) 프로미스 체인

```js
function runToGoal(){
    return new Promise(function(resolve, reject){
        console.log('5초 동안 스퍼트!!, 달린다');
        setTimeout(function(){
            resolve('도착!!!');
        }, 5000);
    });
}
function timeLog(time){
    console.log(`${time}...`);
}
function countdown(seconds){
    const timeoutIds = [];
    return new Promise(function(resolve, reject){
        for(let i = seconds; i >= 0; i--){
            timeoutIds.push(setTimeout(function(){
                if(i === 13){
                    timeoutIds.forEach(clearTimeout);
                    //clearTimeout 으로 모든 setTimeout 대기를 막지 않으면 13 이후 12 아래로 다 콘솔로그가 프린트된다.
                    return reject('카운트 다운 실패');
                }
                if(i > 0) timeLog(i);
                else resolve('카운트 다운 종료');
            }, (seconds - i)*1000));
        }
    });
}
```

위 예시 코드를 하단에 성공과 실패로 나뉘어서 실행예시를 들어온다.

#### 성공
```js
var test = countdown(5);
test.then(msg => console.log(msg))
.then(runToGoal)
.then(msg => console.log(msg))
.catch(err => console.error(err));
```
#### 콘솔로그 결과
```
5...
4...
3...
2...
1...
카운트 다운 종료

(runToGoal 함수 시작)
5초 동안 스퍼트!!, 달린다

(5초뒤)

도착!!!
```

#### 실패
```js
var test = countdown(15);
test.then(msg => console.log(msg))
.then(runToGoal)
.then(msg => console.log(msg))
.catch(err => console.error(err));
```
#### 콘솔로그 결과
```
15...
14...
카운트 다운 실패
```

위 예시 코드로 알 수 있듯이 프로미스 체인을 이용하면 모든 단계의 에러를 한번에 캐치할 수 있다. 체인 중 어느 한곳의 에러만으로도 catch 핸들러가 동작한다.

### 예시 4) 결정되지 않는 프로미스 방지

프로미스를 웹 통신에 사용하거나, 특정 함수에 사용을 하는데 해당 프로미스가 만약 너무 오래걸리는 통신이나, 오래걸리는 알고리즘이거나, 또는 promise resolve reject 호출하는 것을 잊어서 프로미스가 성공이나 실패로 결정나지 않는다면 프로미스는 자체적으로 결정되지 않았다고 해결하지 못한다.

위 문제를 프로미스에 타임아웃을 걸어서 걸어둔 시간 이후로도 응답이 없다면 reject를 시키는 코드를 만들 수 있다.

```js
function halfFail(){
    return new Promise(function(resolve, reject){
        if(Math.random() < 0.5) return; //아래 resolve 도달 불가
        console.log('2초 뒤 완료.');
        setTimeout(function(){
            resolve('완료!!');
        },2000)
    });
}
```

위 코드는 50% 확률로 프로미스의 resolve를 반환 안한다.

```js
halfFail().then(msg => console.log(msg));
```
#### 콘솔로그 결과
```
2초 뒤 완료.
(2초뒤)
완료
```
#### 또는
```
log 노출 없음 (= 결정이 안된 프로미스)
```

위 예시처럼 코드를 잘못 만들지는 않지만, 같은 결과로 프로미스가 반환되지 않는 경우 또는 개발자가 프로미스 반환시간에 제한을 걸어야 하는 경우가 생길 수도 있다.

```js
function addTimeout(fn, timeout = 1000){
    return function(...args){
        return new Promise(function(resolve, reject){
            const tid = setTimeout(reject, timeout, new Error('프로미스 타임아웃'));
            fn(...args).then(function(...args){
                clearTimeout(tid);
                resolve(...args);
            }).catch(function(...args){
                clearTimeout(tid);
                reject(...args);
            });
        });
    }
}
```

#### 위 코드 사용 예시

```js
function addTimeout(fn, timeout = 1000){
    return function(...args){
        return new Promise(function(resolve, reject){
            const tid = setTimeout(reject, timeout, '프로미스 타임아웃');
            fn(...args).then(function(...args){
                clearTimeout(tid);
                resolve(...args);
            }).catch(function(...args){
                clearTimeout(tid);
                reject(...args);
            });
        });
    }
}
function countdown(seconds){
    return new Promise(function(resolve, reject){
        for(let i = seconds; i >= 0; i--){
            setTimeout(function(){
                if(i > 0) timeLog(i);
                else resolve('카운트 다운 종료');
            }, (seconds - i)*1000);
        }
    });
}
function halfFail(){
    return new Promise(function(resolve, reject){
        if(Math.random() < 0.5) return; //아래 resolve 도달 불가
        console.log('2초 뒤 완료.');
        setTimeout(function(){
            resolve('완료!!');
        },2000)
    });
}

countdown(2)
.then(msg => console.log(msg))
.then(addTimeout(halfFail, 3000))
.then(msg => console.log(msg))
.catch(err => console.error(err));
```

#### 콘솔로그 결과

```
2...
1...
카운트 다운 종료
2초 뒤 완료.
완료!!
```
#### 또는
```
2...
1...
카운트 다운 종료
프로미스 타임아웃
```

---

## 패러다임 3. Generator

제너레이터는 함수와 호출자 사이의 양방향 통신이 가능하다. 제너레이터는 동기적 성격을 가지고 있지만 프로미스와 같이 사용을 하면 훨씬 더 관리하기 효율적인 비동기 코드를 만들 수 있다.

### Generator 기초 예시 ) 데이터 이동 : yield -> next()
```js
function* getHidikiMembers() {
  yield 'Wabi';
  yield 'Teak';
  yield 'Tesilio';
  yield 'One';
  yield 'Hidekuma';
}

const hidikiMembers = getHidikiMembers();
console.log(hidikiMembers.next()); // {value: "Wabi", done: false}
console.log(hidikiMembers.next()); // {value: "Teak", done: false}
console.log(hidikiMembers.next()); // {value: "Tesilio", done: false}
console.log(hidikiMembers.next()); // {value: "One", done: false}
console.log(hidikiMembers.next()); // {value: "Hidekuma", done: false}
console.log(hidikiMembers.next()); // {value: undefined, done: true}
```

### Generator 기초 예시 ) 데이터 이동 : next() -> yield
```js
function *askFavoriteColor(){
    const name = yield 'What is your name?';
    const color = yield 'What is your favorite color?'
    return `${name}'s favorite color is ${color}.`;
}

const wfc = askFavoriteColor();
wfc.next(); // {value:'What is your name?', done:false}
wfc.next('Wabi'); // {value:'What is your favorite color?', done:false}
wfc.next('red'); // {value:'Wabi's favorite color is red.', done:true}
```

- 함수 내부 `yield` 마다 반환&제어되고 `next()` 를 통해 순환 흐름이 생성된다.
- 제너레이터 함수의 `next()` 와 함수 내부 `yield` 가 서로 데이터를 주고받을 수 있다는 점을 예시에서 확인할 수 있다.

1. 제너레이터는 화살표 함수로 만들수 없고 반드시 function *을 써야한다.
2. 제너레이터에서 중요한 값을 절대 return으로 반환하려고 하면 안된다. (이유는 하단 코드 참고)

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

### 예시 )

```js
const users = ['Wabi','Teak','Tesilio','Hidekuma','One'];

const getRandomIdx = obj => new Promise(resolve => {
  setTimeout(() => resolve({
      ...obj,
      idx : Math.floor(Math.random() * users.length)
  }), 1000);
});

const getUserByIdx = obj => new Promise(resolve => {
  setTimeout(() => resolve({
      ...obj,
      name : users[obj.idx]
  }), 1000);
});

// 프로미스 활용할 경우
Promise.resolve({})
.then(getRandomIdx)
.then(getUserByIdx)
.then(obj => console.log(`배열 ${obj.idx+1} 번째 ${obj.name}가 있습니다.`))
```

제너레이터를 사용하기 위한 실행 라이브러리 & 제너레이터 사용 라이브러리
- [co : 제너레이터 실행기](https://github.com/tj/co)
- [Koa](https://koajs.com/),
- [Redux-saga](https://github.com/redux-saga/redux-saga)

제너레이터를 사용하기위해서 직접 실행 함수를 만들기보다는 위 3가지 라이브러리 등 프로젝트에 알맞게 이미 만들어진 실행기를 쓰는 것이 시간 절약하기에 좋다.

---

## 패러다임 4. async/await

[async/await 는 generator를 기반으로 만들어졌다.](https://tc39.github.io/ecmascript-asyncawait/)
