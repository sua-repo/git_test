import React, { useState } from 'react'


// State가 화면 갱신을 위한 데이터 관리

// 화면 갱신 안 됨
// state : 상태
// state란 리액트가 고나리하는 화면 갱신용 변수 
const Counter2 = () => {
  
  const [number, setNumber] = useState(0)

  const onIncrease = () => {
    setNumber(number + 2)
    console.log(number)
  }

  const onDecrease = () => {
    setNumber((number) => number - 2)
    console.log(number)
  }

  return (
    <div>
      <h1>{number}</h1>
      <button onClick = {onIncrease}>+2</button>  
      <button onClick = {onDecrease}>-2</button>
    </div>
  )
}

export default Counter2
