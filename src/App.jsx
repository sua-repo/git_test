import { BrowserRouter, Outlet, Route, Routes } from 'react-router-dom'
import routes from './route/Routes'
import Header from './components/Header'
import 'bootstrap/dist/css/bootstrap.min.css'


function App() {
  return (
    <>
      <div>헤더입니다.</div>
      <Outlet />
      <div>꼬리말</div>
    </>
  )
}

export default App