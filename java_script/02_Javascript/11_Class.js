class Car {
  // __init__():
  constructor(options) {
    this.title = options.title
  }
  // method
  drive() { 
    return `${this.title}은 부릉부릉 달린다!`
  }
}


class Mercedes extends Car {
  constructor(options) {
    super(options)
    this.color = options.color
  }

  honk() {
    return '빵빵'
  }
}

const options = {title: '세단', color: 'blue'}

// 특정 클래스에 새로운 인스턴스 생성할 때 new를 사용한다.
const eclass = new Mercedes(options)


