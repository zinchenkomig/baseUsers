import {useContext} from 'react';
import AuthContext from "../context/auth";
import {Outlet, Navigate, useLocation} from "react-router-dom";


const RequireAuth = () => {
    const {userInfo} = useContext(AuthContext);
    const location = useLocation();

    console.log('user info:', userInfo);
    return (
    userInfo?.username
        ? <Outlet/>
        : <Navigate to="/login" state={{from: location}} replace/>
    );
};

export default RequireAuth;