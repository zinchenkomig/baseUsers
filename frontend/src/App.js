import {createBrowserRouter, Link, Outlet, RouterProvider} from "react-router-dom";
import ErrorPage from "./error_page";
import Login from "./login/login";
import SignUp from "./signup/signup";
import useAuth from "./hooks/auth";


const router = createBrowserRouter([
    {
        path: "/",
        element: <Root/>,
        errorElement: <ErrorPage/>,
        children: [
            {
                path: "products",
                element: <ProductsContent/>,
            },
            {
                path: "profile",
                element: <Profile/>,
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

// const nav_active = ({ isActive, isPending }) =>
//     isActive
//         ? "nav-link active"
//         : isPending
//             ? "nav-link pending"
//             : "nav-link"


export default function App(){
    return (
        <RouterProvider router={router}/>
    )
}

function Root() {
  return (
      <div className="container-fluid">
      <nav className="navbar navbar-expand-lg bg-light">
          <div className="container">
              <Link className="navbar-brand" to={`/`}>
                  Home
              </Link>
              <div className="d-flex">
                  <Link to={`profile`}>
                      <svg xmlns="http://www.w3.org/2000/svg" width="2em" height="2em" fill="currentColor"
                           className="bi bi-person-circle" viewBox="0 0 16 16">
                          <path d="M11 6a3 3 0 1 1-6 0 3 3 0 0 1 6 0z"/>
                          <path fillRule="evenodd"
                                d="M0 8a8 8 0 1 1 16 0A8 8 0 0 1 0 8zm8-7a7 7 0 0 0-5.468 11.37C3.242 11.226 4.805 10 8 10s4.757 1.225 5.468 2.37A7 7 0 0 0 8 1z"/>
                      </svg>
                  </Link>
              </div>
          </div>
      </nav>
      <Outlet/>
      </div>

  );
}

function ProductsContent(){
    return (
        <div className="container text-center">
        </div>
    )
}


function Profile(){
    const userInfo = useAuth();

    return(
        <div>
            Profile info: {userInfo?.username}
        </div>
    )
}

