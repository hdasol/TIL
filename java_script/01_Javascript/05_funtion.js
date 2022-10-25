/*


*/

// 1. 선언식 funtion 함수이름 () {} === 기명함수
function add(x,y) {
  return x+y
}

let a = add(3, 4)
console.log(a)

// 2. 표현식 === 익명함수를 어떤 함수 식별자에 할당해서 정의
const sub = function(x,y) {
  return x-y
}

let b = sub(4, 3)
console.log(b)

// 3. arrow funtion

// 원래는 이거였음
let cube = function (n) {return n**3}
// cube = (n) => {return n**3}
cube = n => n**3

console.log(cube(3))

