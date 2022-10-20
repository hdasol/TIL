// 1. dash-case(kebab-case)
// => html, css 사용

// 2. snake_case
// 3. camelCase === lowerCamelCase(Js 주로사용)
// 4. Pascalcase === UpperCanelCase(JS class명)
// 5. UPPER_SNAKE_CASE => 절대 변하면 안될 것 같은 상수들

let x = 1
x = 2
console.log(x)

// let x = 'hi'
// let은 재할당은 가능하지만 재선언은 안돼, const는 재할당, 재선언 둘 다 안돼
// var => ES5, 제선언 및 재할당 모두 가능!

// 위에는 가능하지만, 밑에는 불가능하다. bar는 정의하지 않았다는 에러를 뜨게 한다. var는 선언을 먼저 하지 않아도, console.log를 쓸 수 있다. 
// 상대적으로 자유도 개념에서 보면 var > let > const 정도로 볼 수 있지 않나?
console.log(foo);
var foo;

// console.log(bar);
// let bar;

// 데이터 종류(자료형) -> JS는 데이터 기준으로 사고,

/*
  Primitive Types
  1. Number
  2. String
  3. Empty
  4. Boolean
*/

// 스트링
let myName = 'alex'
let greeting = `Hello, my name is ${myName}`
console.log(greeting)

console.log('안녕' + '하세요')
console.log('안녕' + 3 + '살 아가야') // 형변환


// Number
console.log(
  'Number Types: ',
  Infinity, -Infinity, NaN
)

// Empty Values
console.log(undefined, null)

// Boolean Types
console.log(true, false)

