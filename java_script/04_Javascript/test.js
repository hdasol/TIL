// console.log(typeof undefined, typeof null)

// const alex = {
//   lastName: '권',
//   firstName: '이혁',
//   greeting: function () {
//     return `안녕하세요 ${this.lastName + this.firstName}입니다.`
//   }
// }

// object 안의 
// key: function 구조 안이 function 안의 this는 그 key를 소유하고 있는
// object에 들러붙는다(bind)?

const pine = {
  lastName: '황',
  firstName: '다솔',
  greeting: function() {
    return `안녕하세요 ${this.lastName + this.firstName}입니다`
  }
}

// console.log(pine.greeting())

// 원본은 훼손하지 않으면서, forEach는 돌면서 하나씩 뽑아줌
const arr = [1, 2, 3]

arr.forEach(function (num) {
  console.log(num)
})
console.log(arr)

const arr2 = arr.map(function (num) {
  return num*2
})
console.log(arr2)

const arr3 = arr.map(num => num*2)
console.log(arr3)


// const articles = [
//   {pk: 1, title: 'hi'},
//   {pk: 2, title: 'hello'},
//   {pk: 3, title: 'im fine'},
// ]

const movies = [
  {title: 'matrix', isAdult: false},
  {title: 'kingsman', isAdult: true},
  {title: 'deadpool', isAdult: true},
]
const adultMovies = movies.filter(movie => movie.isAdult)
console.log(adultMovies)


arr.reduce(function (acc, num) {
  console.log(num, acc)
}, 0)

arr.reduce(function (acc, num) {
  return acc + num
}, 0)

/* Spread Operator */

function withoutSpreadOpr() {
  const odds = [1, 3, 5, 7]
  const evens = [2, 4, 6, 8]
  const nums = odds.concat(evens)
  console.log(nums)
}

withoutSpreadOpr()