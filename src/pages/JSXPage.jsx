import React from 'react'

// 컴포넌트 = js + xml(html) 문법 = jsx
// jsx 문법은 html과 js를 조합한 문법

// 1. 반드시 부모 태그가 있어야 함
// Virtual DOM(리액트가 가지고 있는 document 구조)에서 컴포넌트 변화를 감지할 때
// 효율적으로 비교할 수 있도록 컴포넌트 내부는 하나의 DOM 트리 구조로 이루어져야 한다.


// 2. 변수 사용 시 {} 표현식 문법 사용 (= 식이 값으로 평가될 수 있는 문법)
//(<div style={{color:color}}>{name}</div>)

// 3. 조건문(if) 사용 시 삼항 연산자(==) 사용 (리턴문에선 조건식 사용 불가)

// 4. class 대신 className

// 5. React DOM은 HTML 어트리뷰트 이름 대신 camelCase 프로퍼티 명명 규칙을 사용


// Fragment 태그는 빈 태그와 같은 기능 (껍데기 기능)

const JSXPage = () => {

  const name = '리액트'
  const color = 'red'
  const isLogin = true

  const style = {
    backgroundColor : 'green',
    fontSize: '32px'
  }
  // return (<> { isLogin? ( <div>로그인 되었습니다.</div> ) : ( <div>로그인이 필요합니다.</div> ) } </>)

  return (
    <>
      <div className="d-flex" style = {style}>안녕하세요</div>
    </>
  )
}

export default JSXPage
