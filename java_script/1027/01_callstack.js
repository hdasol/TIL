// 01. 콜스택과 실행 컨텍스트
// 자바 스크립트는 하나의 싱글 스레드임. 몸이 하나라는 말임
// console.log()는 함수이다.

const foo = function () {
  console.log("foo")
}

const bar = function () {
  console.log("bar")
}

foo()
bar()