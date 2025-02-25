import React from 'react'
import Hello from '../components/Hello'

const PropsPage = () => {
    // 파라미터를 만들어서 넘길 수 있다 -> 함수이기 때문
    const age = 3
    const name = '홍길동'
    
    /*
    const {name, age, color} = {
        name : '홍길동',
        age : '29',
        color : 'red'
    }
    */

    return (
        <div>
        <Hello name = {name} age = {age} color = "red"></Hello>
        <Hello></Hello>
        </div>
    )
}

export default PropsPage
