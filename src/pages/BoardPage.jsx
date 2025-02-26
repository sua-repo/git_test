import React from 'react'
import { useParams } from 'react-router-dom'

const BoardPage = () => {
  const params = useParams()

  console.log(params)

  return <h1 className='text-center mt-5'>게시판 입니다.{params.id}번 글입니다.</h1>
}

export default BoardPage