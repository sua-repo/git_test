import React from 'react'

const ConditionalPage = () => {

  const isLogin = true
  /*
  // 조건부 랜더링 : if문 사용
  if (isLogin) {
    return (
      <>
        <h2>조건부 렌더링 예시 1번입니다.</h2>
        <div>
          <button style={{ margin: 10 }}>Logout</button>
        </div>
      </>
    )
  } 
  else {
    return (
      <>
        <h2>조건부 렌더링 예시 1번입니다.</h2>
        <div>
          <button style={{ margin: 10 }}>Login</button>
        </div>
      </>
    )
  }
  */

  /*
  // 조건부 랜더링 : switch문 사용
  switch (isLogin) {
    case true:
      return (
        <>
          <h2>조건부 렌더링 예시 2번입니다.</h2>
          <div>
            <button style={{ margin: 10 }}>Logout</button>
          </div>
        </>
      )
    case false:
      return (
        <>
          <h2>조건부 렌더링 예시 2번입니다.</h2>
          <div>
            <button style={{ margin: 10 }}>Login</button>
          </div>
        </>
      )
    default:
      return null
  }
  */

  /*
  // 조건부 랜더링 : 삼항 연산자
  return (
    <>
      <h2>조건부 렌더링 예시 3번입니다.</h2>
      {isLogin ? (
        <div>
          <button style={{ margin: 10 }}>Logout</button>
        </div>
      ) : (
        <div>
          <button style={{ margin: 10 }}>Login</button>
        </div>
      )}
    </>
  )
  */

  // 조건부 랜더링 : && 연산자 사용
  /*
  let a = true
  let b = a && '바나나'
  console.log(b)    // 바나나
  */
  return (
    <>
      <h2>조건부 렌더링 예시 4번입니다.</h2>
      {isLogin && (
        <div>
          <button style={{ margin: 10 }}>Logout</button>
        </div>
      )}
    </>
  )
}

export default ConditionalPage
