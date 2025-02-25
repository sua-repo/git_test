import React, { useState } from 'react'


// State가 화면 갱신을 위한 데이터 관리

// 화면 갱신 안 됨
// state : 상태
// state란 리액트가 고나리하는 화면 갱신용 변수 
const Counter = () => {
  
  //let number = 0
  const [number, setNumber] = useState(0)

  const onIncrease = () => {
    //number = number + 1
    setNumber(number + 1)
    console.log(number)
  }

  const onDecrease = () => {
    setNumber((number) => number - 1)
    console.log(number)
  }

  // 함수명 옆에 괄호가 있으면 함수 호출되기 때문에 괄호 빼야 함
  return (
    <div>
      <h1>{number}</h1>
      <button onClick = {onIncrease}>+1</button>  
      <button onClick = {onDecrease}>-1</button>
    </div>
  )
}

export default Counter
