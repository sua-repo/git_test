import React, { Fragment } from 'react'
import Hello from '../components/Hello'
// 컴포넌트 = js + xml(html) 문법 = jsx
// jsx 문법은 html과 js를 조합한 문법
const HelloPage = () => {
  return (
    <Fragment>
      <Hello></Hello>
      <Hello></Hello>
      <Hello></Hello>
      <Hello></Hello>
      <Hello></Hello>
    </Fragment>
  )
}

export default HelloPage