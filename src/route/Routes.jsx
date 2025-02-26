import AxiosClient from "../pages/AxiosClient"
import AxiosGetPage from "../pages/AxiosGetPage"
import BoardPage from "../pages/BoardPage"
import BootStrapPage from "../pages/BootStrapPage"
import ConditionalPage from "../pages/ConditionalPage"
import CounterPage from "../pages/CounterPage"
import HelloPage from "../pages/HelloPage"
import HomePage from "../pages/HomePage"
import JSXPage from "../pages/JSXPage"
import ProfilePage from "../pages/ProfilePage"
import PropsPage from "../pages/PropsPage"
import UseEffectPage from "../pages/UseEffectPage"
import UseRef1Page from "../pages/UseRef1Page"
import UseRef2Page from "../pages/UseRef2Page"

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

      {
        path: '/jsx',
        element: <JSXPage/>,
        title : 'jsx문법',
      },

      {
        path: '/conditional',
        element: <ConditionalPage/>,
        title : '조건부랜더링',
      },

      {
        path: '/bootstrap',
        element: <BootStrapPage/>,
        title : '부트스트랩적용',
      },

      {
        path: '/Props',
        element: <PropsPage/>,
        title : '프롭스',
      },

      {
        path: '/usestate',
        element: <CounterPage/>,
        title : 'useState-연습',
      },

      {
        path: '/useeffect',
        element: <UseEffectPage/>,
        title: 'useEffect-연습',
      },

      {
        path: '/useref',
        element: <UseRef1Page/>,
        title: 'useRef-1',
      },

      {
        path: '/useref2',
        element: <UseRef2Page/>,
        title: 'useRef-2',
      },

      {
        path: '/axiosget',
        element: <AxiosGetPage/>,
        title: 'axios-get',
      },

      {
        path: '/axiosclient',
        element: <AxiosClient/>,
        title: 'axios-client',
      },
]
export default routes
  