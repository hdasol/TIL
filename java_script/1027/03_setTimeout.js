// 03. 동기, 비동기, 실행 컨텍스트 종합

// 시간 지연 함수 

function sleep(sec) {
  const delayUntil = Date.now() + sec
  while (Date.now() < delayUntil) { }
}

setTimeout(function () {
  console.log('5초 뒤 실행!')
}, 5000)

for (let i = 1; i <= 10; i++) {
  console.log(`${i}번째 반복`)
  sleep(1000)
}


// 이러면 10번째 반복 후 바로 5초 뒤 실행! 왜냐면 아직 이벤트 루프에 전역 함수가
// 돌고 있기 때문에 그걸 기다린 후 바로 실행한다.
