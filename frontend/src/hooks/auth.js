import {useEffect, useState} from "react";
import axios from "../api/backend"
import {useNavigate} from "react-router-dom";


export default function useAuth(){
    const [userInfo, setUserInfo] = useState(null);
    const navigate = useNavigate();

    useEffect( () =>
    {
        async function getCurrentUser(){
            return await axios.get('/current_user')
                .then((response) => {
                    if (response.status === 200){
                        console.log('Success')
                        setUserInfo(response.data)
                    }
                    else{
                        console.log('Fail')
                        setUserInfo(null)
                        navigate('/login');
                    }
                });
        }
        getCurrentUser();
        return () => {console.log('Unmount')}
    }, [navigate])
    return userInfo;
}