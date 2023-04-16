import {createBrowserRouter, Link, Outlet, RouterProvider} from "react-router-dom";
import ErrorPage from "./error_page";
import Login from "./login/login";
import SignUp from "./signup/signup";
import AuthContext from "./context/auth";
import {useContext} from "react";
import RequireAuth from "./components/RequireAuth";
import axios from "./api/backend";
import { FaUser } from "react-icons/fa"
import "./style.css"


const router = createBrowserRouter([
    {
        path: "/",
        element: <Root/>,
        errorElement: <ErrorPage/>,
        children: [
            {
                element: <RequireAuth/>,
                children: [
                    {
                        path: "profile",
                        element: <Profile/>,
                    },
                ]
            },
            {
                path: "login",
                element: <Login/>
            },
            {
                path: "signup",
                element: <SignUp/>
            }
        ]
    },
])

export default function App(){

    return (
            <RouterProvider router={router}/>
    )
}
function NLink({to, children}) {
    return (
        <Link className="nav-link" to={to}>
            {children}
        </Link>

    )
}

function Root() {
  return (
      <div>
      <nav>
          <NLink to={`/`}>Home</NLink>
          <NLink to={`/profile`}><FaUser/></NLink>
      </nav>
          <div className="main-content">
              <Outlet/>
          </div>
      </div>

  );
}

function Profile(){
    const {userInfo, setUserInfo} = useContext(AuthContext);

    async function onLogoutClick(){
        await axios.post('/auth/logout');
        localStorage.removeItem('username');
        setUserInfo({});
    }

    return(
        <div>
            <div>
                Profile info: {userInfo?.username}
            </div>
            <button onClick={onLogoutClick}>Logout</button>
        </div>
    )
}
