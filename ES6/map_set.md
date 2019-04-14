## Map & Set

ES6 이전 키와 값을 연결하는데 객체 사용시, 생기는 여러가지 단점.

- 프로토타입 체인 때문에 의도하지 않은 연결이 생길 수 있습니다.
- 객체 안에 연결된 키와 값이 몇 개나 되는지 쉽게 알아낼 수 있는 방법이 없습니다.
- 키는 반드시 문자열이나 심볼이어야 하므로 객체를 키로 써서 값과 연결할 수 없습니다.
- 객체는 프로퍼티 순서를 전혀 보장하지 않습니다.

> 맵은 키와 값을 연결한다는 점에서 객체와 비슷하고, 셋은 중복을 허용하지 않는다는 점을 제외 하면 배열과 비슷합니다.

```js
const u1 = {name : 'Wabi'};
const u2 = {name : 'Yuna'};
const u3 = {name : 'Zinico'};
const u4 = {name : 'Yuri'};

const userRoles = new Map();
```

```js
userRoles.set(u1, 'User');
userRoles.set(u2, 'User');
userRoles.set(u3, 'Admin');
```

```js
userRoles
    .set(u1, 'User')
    .set(u2, 'User')
    .set(u3, 'Admin');
```

> 메서드를 체인으로 연결할 수 있다.

```js
const userRoles = new Map([
    [u1,'User'],
    [u2,'User'],
    [u3,'Admin']
]);

userRoles.get(u2); // User

userRoles.has(u1); // true
userRoles.get(u1); // "User"
userRoles.has(u4); // false
userRoles.get(u4); // undefined

userRoles.get(u1); // 'User'
userRoles.set(u1, 'Admin');
userRoles.get(u1); // 'Admin'

userRoles.size; // 3
```

> 요소를 지울때는 delete() \
모두 지울 때는 clear()