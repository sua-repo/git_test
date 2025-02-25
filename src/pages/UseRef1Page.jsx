import React, { useRef, useState } from 'react'

//첫번째 사용하는 경우
//useRef 변화는 감지해야 되지만, 렌더링은 하고 싶지 않을때.
//중요한 사실 화면 갱신이 일어 난다는 말은
// => 해당 컴포넌트를 실행한다.

const UseRef1Page = () => {

    const [count, setCount] = useState(0)
    const countRef = useRef(0) //{current: 1}
    console.log(countRef)
    console.log('호출되고 있음')
  
    const increaseCountState = () => {
      setCount(count + 1)
    }
  
    const increaseCountRef = () => {
      countRef.current = countRef.current + 1
      console.log('핳하하')
    }
  
    //let tag = document.querySelector("#AAA")
  
    //prettier-ignore
    return (
      <div className='text-center mt-5'>
          <p>State :{count}</p>
          <p>Ref :{countRef.current}</p>
          <button id="AAA"  onClick={increaseCountState}>State 값 올리라</button>
          <button onClick={increaseCountRef}>Ref 값 올리라</button>      
      </div>
    )
  }
  
  export default UseRef1Page