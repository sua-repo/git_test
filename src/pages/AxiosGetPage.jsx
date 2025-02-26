import axios from 'axios'
import React, { useEffect, useState } from 'react'
import userService from '../services/UserService'
const AxiosGetPage = () => {

  const [data, setData] = useState(null)

  useEffect(() => {
    userService.getUsers().then((data) => {
        setData(data);
    });
  }, [])

  

  const postClick = () => {
    axios.get('https://jsonplaceholder.typicode.com/posts', {
        userId : 12345,
        id : 101,
        body : '테스트 홍길동',
        title : 'test title 홍길동'
    })
        .then((response) => {
            // 통신이 성공했을 때
            console.log(response);
            setData(response.data)  // 화면 갱신을 위함
        })
        .catch(function (error) { 
            // 통신에서 에러가 났을 때
            console.log(error);

        })
        .then (() => {
            //try - catch - finally에서 finally 부분에 해당
            console.log('에러가 나든 안 나든 무조건 실행');
        })
  }

  return (
  <>
    <div className='text-center mt-5'>
        <h2>엑시오스 Get 연습</h2>
        <button onClick={postClick}>Post 방식 연습</button>
        <hr />
        {
            data&& data.map((post, index) => (
                // data가 0이나 null 이면 빠져나감
                <div key = {index}>
                    <h3>타이틀 : {post.title}</h3>
                    <h3>유저아이디:{post.userId} , 아이디:{post.id}</h3>
                    <h3>바디 : {post.body}</h3>
                </div>
            ))
        }
    </div>  
  </>
  )
}

export default AxiosGetPage
