const body = document.querySelector('body')

function logThis() {
  console.log(this)
}


const obj = {
  logThis: function () {
    console.log(this)
  },
  setTime: function () {
    setTimeout(this.logThis, 2000)
  },
  addEvent: function () {
    body.addEventListener('click', this.logThis)
  }
}
// setTimeout과 addEventListener에 적용되는 룰이 다르다.
// this가 가르키는 것이 다르다는 것. 함수안에 콜백함수 안에 this는 window로 날아간다.
obj.logThis()
obj.setTime()
obj.addEvent()


// forEach  같은 경우?
const obj2 = {
  method: function () {
    [1, 2, 3].forEach(function () {
      console.log(this)
    }, this)
    // 두 번째 인자로 this를 넣어주는 경우 method f를 가리키게 됨!
    // 만약 이거 없으면 window로 날아감.
  }
}