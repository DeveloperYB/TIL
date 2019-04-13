# OOP : ES6 Class

> 버미노트님 블로그 참고 : https://beomy.tistory.com/15

## class 선언 2 방식

```js
// unnamed
var haveLunch = class {
    constructor(mainDish, subDish) {
        this.mainDish = mainDish;
        this.subDish = subDish;
    }
};
 
// named
var haveLunch = class haveLunch {
    constructor(mainDish, subDish) {
        this.mainDish = mainDish;
        this.subDish = subDish;
    }
};
```

## Class ? 호이스팅 ?

```js
var hL = new haveLunch(); // ReferenceError
class haveLunch {}
```

> 클레스 선언은 함수 선언과 다르게 호이스팅이 되지 않는다.

## 정적 메서드

> 정적 메서드에서 this는 인스턴스가 아니라 클래스 자체에 묶인다.\
하지만 일반적으로 정적 메서드에는 this 대신 클래스 이름을 사용하는 것이 좋은 습관

```js
class Car {
    static getNextVin(){
        return Car.nextVin++;
    }
    static areSimilar(car1,car2){
        return car1.make === car2.make && car1.model === car2.model;
    }
    static areSame(car1,car2){
        return car1.vin === car2.vin;
    }
    constructor(make,model){
        this.make = make;
        this.model = model;
        this.vin = Car.getNextVin();
    }
}
Car.nextVin = 0;

const car1 = new Car('Sonata','S');
const car2 = new Car('Matiz','A');
const car3 = new Car('Matiz','A');

car1.vin; //0
car2.vin; //1
car3.vin; //2

Car.areSimilar(car1,car2); // false
Car.areSimilar(car2,car3); // true
Car.areSame(car2,car3); // false
Car.areSame(car2,car2); // true
```
---
## 상속

```js
class Vehicle{
    constructor(){
        this.passengers = [];
        console.log('Vehicle created');
    }
    addPassenger(p){
        this.passengers.push(p);
    }
}
class Car extends Vehicle{
    constructor(){
        super();
        console.log('Car created');
    }
    deployAirbags(){
        console.log('Boom!');
    }
}

const v = new Vehicle();
v.addPassenger("Wabi");
v.addPassenger("Yuna");
v.passengers;   // ['Wabi','Yuna'];
const c = new Car();
c.addPassenger("Yuri");
c.addPassenger("Zinico");
c.passengers;   // ['Yuri','Zinico'];
v.deployAirbags(); // error
c.deployAirbags(); // 'Boom!'
```

> 상속은 단방향! \
Car를 Vehicle의 서브클래스로 만듬.

## 객체 프로퍼티 나열

```js
class Super{
    constructor(){
        this.name = 'Super';
        this.isSuper = true;
    }
}
//유효하지만, 쓰지않는 방식 (테스트용으로 씀)
Super.prototype.sneaky = 'Not recommended!';

class Sub extends Super {
    constructor(){
        super();
        this.name = 'Sub';
        this.isSub = true;
    }
}

const obj = new Sub();

for(let p in obj){
    console.log(`${p}: ${obj[p]}` + (obj.hasOwnProperty(p)?'':' (ingerited)'));
}
/* 콘솔로그 결과
name: Sub
isSuper: true
isSub: true
sneaky: Not recommended! (ingerited)
*/
```

---

> 객체지향 프로그래밍은 널리 쓰이는 패러다임이고, 그럴만한 이유가 있다. 객체 지향 프로그래밍을 사용하다 보면 자연스레 관리하고, 디버그하고 수정하기 쉬운 정리되고 캡슐화된 코드를 작성하게 된다.