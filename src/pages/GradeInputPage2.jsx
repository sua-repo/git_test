import React, { useState } from 'react'

// 다중입력
const GradeInputPage2 = () => {

  /*
    const [kor, setKor] = useState(0);
    const [eng, setEng] = useState(0);
    const [math, setMath] = useState(0);
    const [name, setName] = useState('');
  */

    const [grade, setGrade] = useState({
      name : '',
      kor : 0,
      eng : 0,
      math : 0
    })

    const onChange = (event) => {
        const {name, value} = event.target

        setGrade({
          ...grade,   // 복사본 => 주소 기준으로 변화를 감지하기 때문에 번지수를 바꾸기 위해 복사본을 만듦
          [name] : value
        })
    }

  return (
    <div>
      이름 : <input name="name" onChange={onChange} value={grade.name} /><br></br>
      국어 : <input name="kor" onChange={onChange} value={grade.kor} /><br></br>
      영어 : <input name="eng" onChange={onChange} value={grade.eng} /><br></br>
      수학 : <input name="math" onChange={onChange} value={grade.math} /><br></br>
      <div>
        <div>총점 : {Number(grade.kor) + Number(grade.eng) + Number(grade.math)}</div>
        <div>평균 : {(Number(grade.kor) + Number(grade.eng) + Number(grade.math)) / 3.0}</div>
      </div>
    </div>
  )
}

export default GradeInputPage2
