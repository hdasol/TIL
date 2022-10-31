// 02. 동기와 비동기

// 동기
console.log('첫 번째')
console.log('두 번째')
console.log('세 번째')

// 비동기
console.log('첫 번째')
setTimeout(() => console.log('두 번째'), 2000)
console.log('세 번째')

// 두 번째가 2초 뒤에 프린트 되는데 이걸 가능하게 하는 것은 웹브라우저이다.
// 웹 브라우저의 (web api, task queue, event loop)가 가능하게 한다.
// 자바스크립트가 아니라.
