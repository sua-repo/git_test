import { BrowserRouter, Outlet, Route, Routes, useNavigate } from 'react-router-dom'
import 'bootstrap/dist/css/bootstrap.min.css'
//import HomePage from './pages/HomePage'
//import HelloPage from './pages/HelloPage'
//import ProfilePage from './pages/ProfilePage'
//import BoardPage from './pages/BoardPage'

/*
function App2() {
  return (
    <>
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<HomePage />}></Route>
          <Route path="/hello" element={<HelloPage />}></Route>
          <Route path="/profile" element={<ProfilePage />}></Route>
          <Route path="/board" element={<BoardPage />}></Route>
        </Routes>
      </BrowserRouter>
    </>
  )
}
*/


function About() {
  const navigate = useNavigate()

  return (
    <div>
      <button
        onClick={() => {
          navigate('/profile')
        }}
      >
        어바웃 페이지로 이동하기
      </button>

      <button
        onClick={() => {
          navigate(-1)
        }}
      >
        이전 페이지로 이동하기
      </button>

      <h2>여기는 About 페이지입니다.</h2>
      <p>대충 쇼핑몰 페이지라는 뜻</p>

      <Outlet /> {/* 중첩 라우트가 렌더링될 위치 */} {/* 서브페이지가 보여질 위치를 Outlet으로 지정해준다. */}
      <Routes>
        <Route path="/location" element={<Location />}></Route>
      </Routes>
    </div>
  )
}

function Location() {
  return <h1>로케이션 컴포넌트</h1>
}

// 2. 중첩 라우팅
//  /about/location
// 서브 페이지의 path는 /를 생략하고 작성하면 된다.
// Outlet 없이 
function App2() {
  return (
    <>
      <BrowserRouter>
        <Routes>
          <Route path='/about/*' element={<About />} >
            <Route path="location" element={<Location />}></Route>
          </Route>
        </Routes>
      </BrowserRouter>
    </>
  )
}


//
export default App2