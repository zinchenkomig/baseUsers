import { useState, createContext } from "react";


const AuthContext = createContext({});

export const AuthProvider = ({children}) => {
    const [userInfo, setUserInfo] = useState({username: localStorage.getItem('username')});

    return (
        <AuthContext.Provider value={{userInfo, setUserInfo}}>
            {children}
        </AuthContext.Provider>
    );
};

export default AuthContext;