/*
  Operands
  1. unary (단항 연산자)
  2. binary (이항 연산자)
  3. ternary (삼항 연산자)

  1. 산술연산자
  2. 수 비교연산자
  3. 동등/일치 연산자
  4. 논리연산자
*/

let i = 1
// i에 대한 평가가 끝난 후, 1을 더한다.
console.log(i++)
// i에 대한 평가가 끝나기 전, 1을 더한다.
console.log(++i)
// ! => 이건 오른쪽 애를 평가한 다음 불리언 값을 뒤집어버림
console.log(!true) 

console.log(1>2 ? '크다' : '작다')

let a = 2
const even_or_odd = a % 2 ? 'odd' : 'even'
console.log(even_or_odd)
