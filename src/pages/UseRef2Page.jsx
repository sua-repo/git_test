import React, {useRef} from 'react'

//Dom 객체를 받아 올때
//useRef 로 특정 DOM 선택하기
//getElementById, querySelector 같은 DOM Selector 함수를 사용해서 DOM 을 선택합니다.
//프로젝트에서도 가끔씩 DOM 을 직접 선택해야 하는 상황이 발생
//예를 들어서 특정 엘리먼트의 크기를 가져와야 한다던지,
//스크롤바 위치를 가져오거나 설정해야된다던지,
//또는 포커스를 설정해줘야된다던지 등 정말 다양한 상황이 있겠죠.
//추가적으로 Video.js, JWPlayer 같은 HTML5 Video 관련 라이브러리,
//또는 D3, chart.js 같은 그래프 관련 라이브러리 등의 외부 라이브러리를 사용해야 할
//때에도 특정 DOM 에다 적용하기 때문에 DOM 객체를 useRef() 로 가져옴

const UseRef2Page = () => {

  const nameRef = useRef()
  // {current : null} <- 리액트가 관리

  // let nameRef ={
  //   current : windows.documnet.querySelector("input")
  // }

  const handleClick = () => {
    console.log(nameRef.current);
    console.log(nameRef.current.name);
    console.log(nameRef.current.value);

    if (nameRef.current.value.length < 1) {
      nameRef.current.focus();  
      // 아무것도 입력하지 않고 버튼을 누르면 focus 깜빡깜빡
    }
  }

  return (
    <div className='text-center mt-5' style={{ padding: 20 }}>
      <input ref={nameRef} name="name" placeholder="이름을 입력하세요" />
      <button onClick={handleClick}>입력</button>
    </div>
  )
}

export default UseRef2Page
UseRef2Page