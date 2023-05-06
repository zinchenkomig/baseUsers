import {useContext} from "react";
import AuthContext from "../context/auth";
import axios from "../api/backend";

export default function Profile(){
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