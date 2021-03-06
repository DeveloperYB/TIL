# 정규표현식

정규식으로 하는 일은 문자열 속에서 부분 문자열을 찾거나, 찾은 부분을 교체할 때 쓰인다.\
String.prototype 메서드의 검색과 교체 기능에는 어느정도 한계가 있지만, 충분히 쓸만하다. 특히 큰 문자열 안에 원하는 부분의 문자열이 존재하는지만 찾으려 할 때는 충분하다.

## String 메서드

```js
const testTxt = "As i was going to my home";
testTxt.startsWith("As"); // true
testTxt.endsWith("home"); // true
testTxt.startsWith("going", 9); // true : index 9 에서 시작.
testTxt.endsWith("to", 17); // true : index 17을 끝으로 간주
testTxt.includes("was"); // true
testTxt.includes("to", 16); // false
testTxt.indexOf("going"); // 9
testTxt.indexOf("going", 10); // -1 : index 10 에서 시작해서 해당 문자 있는지 검색
testTxt.indexOf("none"); // -1
```
> 위 메서드 모두 대소문자를 구별한다.

```js
testTxt.toLowerCase().startsWith("as"); // true
```

> toLowerCase 는 원래 문자열을 그대로 두고, 새 문자열을 반환한다. 자바스크립트의 문자열은 항상 불변이다.

## 문자열 찾고, 교체 replace

```js
const testTxtInput = "I was gonna take a shower";
const testTxtOutput = testTxtInput.replace("take a shower", "work"); // "I was gonna work"
```

## 정규식 만들기

자바스크립트의 정규식은 RegExp 클래스 이다. 또는 간편한 리터럴 문법을 사용할 수 도 있다. (= 슬래시로 감싼 형태도 가능)

```js
const re1 = /going/; // 단어 "going"을 찾을 수 있는 정규식
const re2 = new RegExp("going"); // 생성자를 사용했지만 결과가 위 와 동일.
```

### 정규식 검색

```js
const txt = "I was playing a game with my wife";
const re = /\w{3,}/ig;

txt.match(re); // ["was", "playing", "game", "with", "wife"]
txt.search(re); // 2 : 세글자 이상으로 이루어진 단어의 첫 시작은 인덱스 2 이다.

re.exec(txt); // ["was"]
re.exec(txt); // ["playing"] : exec 는 이전 반환값의 위치를 기억한다.
re.exec(txt); // ["game"]
re.exec(txt); // ["with"]
re.exec(txt); // ["wife"]
re.exec(txt); // null : 일치하는 것이 더이상 없다.
re.exec(txt); // ["was"] : 다시 재반복
re.test(txt); // true (txt 에는 세글자 이상으로 이루어진 단어가 한 개 이상 있다.)

// 위 예제 코드 모두 정규식 리터럴 그대로 써도 된다.
txt.search(/\w{3,}/ig);
/\w{3,}/ig.test(txt);
```

### 정규식을 사용한 문자열 교체
```js
const txtInput = "I'm studying now on my bed, and my wife is watching tv beside me"
const txtOutput = txtInput.replace(/\w{5,}/ig, '@@@@@');
// "I'm @@@@@ now on my bed, and my wife is @@@@@ tv @@@@@ me"
```

> 정규식을 오로지 큰 문자열에서 부분 문자열을 찾는 방법으로만 국한되어 생각하면, 정규식의 근본적인 성격을 이해하지 못하게 된다. 더군다나 할 수 있는 일도 제한을 두고 생각해게 된다. 좀 더 나은 개념으로는 정규식이 입력 문자열을 소비하는 패턴이라고 생각 하면 된다.

### 정규식의 간단한 알고리즘 정리

1. 문자열 왼쪽에서 오른쪽으로 진행한다.
2. 일단 소비한 글자에 다시 돌아오는 일은 없다.
3. 한 번에 한 글자씩 움직이며 일치하는 것이 있는지 확인한다.
4. 일치하는 것을 찾으면 해당하는 글자를 한꺼번에 소비한 뒤 다음 글자로 진행한다.

> 물론 위 간단한 알고리즘 외에도 더 세밀한 알고리즘도 존재한다.

### HTML 찾기 및 정규식의 한계

```js
const html = '<br> [!CDATA[<br>]]';
const matches = html.match(/<br>/ig);
```

위 정규식은 2번 일치하지만, 실제 br 태그는 하나 뿐이다. 위 예시 처럼
태그안에 태그가 존재하는 계층적 구조에는 매우 취약하다.

## 문자셋

문자셋은 글자 하나를 다른 것으로 대체하는 방법을 간단하게 줄인 것을 말한다.

```js
const beer99 = "99 bottles of beer on the wall" +
    "take 1 down and pass it around -- "+
    "my phone number is 000-2949-1010";
const matches = beer99.match(/0|1|2|3|4|5|6|7|8|9/g);
// ["9", "9", "1", "0", "0", "0", "2", "9", "4", "9", "1", "0", "1", "0"]
```

위 방법은 좋은 방법은 아니다. 더 간략하게 쓰기 위해서 아래처럼 가능하다.

```js
const matches = beer99.match(/[0123456789]/g);
const matches = beer99.match(/[0-9]/g);
```

범위를 지정하여 위 처럼 쓰거나, 더불어서 범위를 결합하는 것도 가능하다.
```js
const matches = beer99.match(/[\-0-9a-z.]/ig);
```

순서는 중요하지 않다. 위 코드와 ("/[.a-z0-9\-]/ig") 는 같다. 단, 하이픈은 이스케에프를 해주어야지 하지 않을 경우 범위를 표시하는 메타 문자라고 간주를 한다. (대괄호 바로 앞에쓰는 경우에는 제외)

특정 문자를 제외할 경우에는 ^ (캐럿) 을 맨 앞에 쓰면 된다.

```js
const match = beer99.match(/[^\-0-9a-z.]/);
// 위 코드는 공백만 찾게 된다.
```

