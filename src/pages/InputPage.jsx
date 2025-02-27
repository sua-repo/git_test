import React, { useState } from 'react'

const InputPage = () => {

    const [text, setText] = useState('')

    const onChange = (event) => {
        setText(event.target.value)
        console.log(event.target.value)
    }

    const onReset = () => {
        setText('')
    }

  return (
    <div>
      <input onChange={onChange} value={text} />
      <button onClick={onReset}>초기화</button>
      <div>
        <b>값 : {text}</b>
      </div>
    </div>
  )
}

export default InputPage
