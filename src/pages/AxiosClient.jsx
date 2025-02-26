import axios from 'axios';
import React, { useEffect, useState } from 'react';

const AxiosClient = () => {
  const [contacts, setContacts] = useState(null); // 데이터를 저장할 상태

  useEffect(() => {
    // 버튼 안 눌러도 바로 데이터 받아옴
    handleClick()
  }, [])

  const handleClick = () => {
    axios.get('https://sample.bmaster.kro.kr/contacts?pageno=3&pagesize=10')
      .then((response) => {
        //통신이 성공 했을때
        console.log(response)
        setContacts(response.data.contacts)
      })
      .catch(function (error) {
        //에러가 났을때 실행
        console.log(error)
      })
      .then(() => {
        // try catch finally 에서 finally 부분에 해당
        console.log('에러가 나든 안나든 무조건 실행')
      })
  }

  /*
  const onRemove = (id) => {
    // user.id 가 파라미터로 일치하지 않는 원소만 추출해서 새로운 배열을 만듬
    // = user.id 가 id 인 것을 제거함
    // users.filter((user) => user.id !== id
    setUsers(users.filter((user) => user.id !== id));
   };
  */

  const removeClick = (event) => {
    let no = event.target.name
    console.log(event)
    console.log(no)
    console.log(event.target.value)

    setContacts(contacts.filter((contact) => contact.no != no))
    // 다른 애가 true라 다른 애들만 그림
  }

  return (
    <div className='text-center mt-5'>
      <h2>클라이언트 테이블 받아오기 연습</h2>
      <button onClick={handleClick}>클라이언트 데이터</button>
      <hr />
      <div className='d-flex justify-content-center'>
        <table border="1">
          <tr>
            <td>번호</td>
            <td>이름</td>
            <td>전화번호</td>
            <td>주소</td>
            <td>사진</td>
            <td>삭제</td>
          </tr>
          {
            contacts && contacts.map((contact, index) => (
                <tr key={index}>
                    <td>{contact.no}</td>
                    <td>{contact.name}</td>
                    <td>{contact.tel}</td>
                    <td>{contact.address}</td>
                    <td><img src={contact.photo} alt="" /></td>
                    <td><input type="button" name = {contact.no} onClick={removeClick} value="삭제" /></td>
                </tr>
            )
          )}
        </table>
      </div> 
    </div>
  );
};

export default AxiosClient;
