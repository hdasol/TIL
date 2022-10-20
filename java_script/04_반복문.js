// while 문
// const i = 0
let i = 0
while (i < 5) {
  console.log('하이')
  i++
}

// 전통적인 for
const numbers = [1, 2, 3, 4, 5]
// for (변수할당; 종료조건; 증가) {로직}
for (let j=0; j < numbers.length; j++) {console.log(numbers[j])}

// Array용 for => 요소를 꺼내는 for 이며, of 문을 쓴다
for (const number of numbers) {
  console.log(number, typeof(number))
}

// object용 for 이며, key를 꺼내는 for이다. in 문을 쓴다.
const person = {myName:'dasol', 'address':'seoul'}
for (const key in person) {console.log(key, person[key])}

// 그런데 이거 배열을 돌리면