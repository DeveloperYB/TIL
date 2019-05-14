# Webpack, Tree Shaking

- [웹팩 공식 가이드](https://webpack.js.org/guides/tree-shaking/)

## Tree Shaking 이란?

웹팩이 JS모듈을 번들링할 때 사용하지 않는 코드는 제거를 하는 최적화 과정이다.

### 예시 )

#### project
```
webpack-test-tree-shaking
|- package.json
|- webpack.config.js
|- /dist
  |- bundle.js
  |- index.html
|- /src
  |- index.js
+ |- test.js
|- /node_modules
```

#### src/test.js
```js
export function whatIsYourName (name) { console.log(`My name is ${name}`) }
export function whatIsYourAge (age) { console.log(`I am ${age} years old`) }
export function wabi () { console.log("Wabi"); }
export function one () { console.log("One"); }
export function hidekuma () { console.log("Hidekuma"); }
```
