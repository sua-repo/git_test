import React from 'react'
import { Link } from 'react-router-dom'

const HomePage = () => {
  return (
    <>
      <h1 className='text-center mt-5'>메인페이지 입니다.</h1>
      <Link to="/profile">프로필 페이지</Link>  
      {/* 
        실제로는 a링크
        but Link는 라우터 돔에서 제공하는 것 바뀌는 부분만 그림
        a태그는 완전 처음부터 다시 그려서 화면 깜빡임 
      */} 
    </> 
  )
}

export default HomePage