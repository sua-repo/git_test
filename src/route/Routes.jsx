import BoardPage from "../pages/BoardPage"
import HelloPage from "../pages/HelloPage"
import HomePage from "../pages/HomePage"
import ProfilePage from "../pages/ProfilePage"

//React Routes, Route 사용시 배열로 관리하기
const routes = [
    {
      path: '/',
      element: <HomePage/>,
      title : 'Home',
    },

    {
        path: '/profile',
        element: <ProfilePage/>,
        title : 'profile',
      },

      {
        path: '/board',
        element: <BoardPage/>,
        title : 'board',
      },

      {
        path: '/hello',
        element: <HelloPage/>,
        title : 'hello',
      },
]
export default routes
  