import {createBrowserRouter, Link, Outlet, RouterProvider} from "react-router-dom";
import ErrorPage from "./pages/ErrorPage";
import Login from "./pages/Login";
import SignUp from "./pages/SignUp";
import RequireAuth from "./components/RequireAuth";
import { FaUser } from "react-icons/fa"
import "./assets/style.css"
import Profile from "./pages/Profile";
import RequireSuperuser from "./components/RequireSuperuser";
import UserManagement from "./pages/UsersManagement";
import {useContext} from "react";
import AuthContext from "./context/auth";


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
                element: <RequireSuperuser/>,
                children: [
                    {
                        path: "manage/users",
                        element: <UserManagement/>,
                    }
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


function Root() {
    const { userInfo } = useContext(AuthContext);

  return (
      <div>
      <nav>
          <Link className="nav-link" to={`/`}>Home</Link>
          {userInfo?.scope === 'superuser'
              ? <Link className="nav-link" to={`/manage/users`}>Manage</Link>
              : <></>
          }
          <Link className="nav-link" to={`/profile`}><FaUser/></Link>
      </nav>
          <div className="main-content">
              <Outlet/>
          </div>
      </div>

  );
}

