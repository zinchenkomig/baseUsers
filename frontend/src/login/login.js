import './style.css'
import axios from "../api/backend";
import { useForm } from "react-hook-form";
import {Link} from "react-router-dom";
import { useNavigate } from "react-router-dom";
import AuthContext from "../context/auth";
import {useContext} from "react";
import {flushSync} from "react-dom";


export default function Login(){
    const { register, handleSubmit, setError, formState: { errors } } = useForm({mode: "onBlur"});
    const navigate = useNavigate();
    const { setUserInfo } = useContext(AuthContext);

    const onSubmit = async (data) => {
        let dataForm = new FormData();
        dataForm.append('username', data['username']);
        dataForm.append('password', data['password']);
        await axios.post('/auth/token', dataForm)
            .then((response) => {
                console.log(response);
                if (response.status === 200) {
                    localStorage.setItem('username', response.data.username);
                    console.log('Localstorage check: ', localStorage.getItem('username'));
                    flushSync(() => {
                        setUserInfo({username: response.data.username})
                    });
                    navigate('/profile');
                }
            }).catch((error)=>{
                if (error.response.status === 401){
                    setError("password", {type: "focus", message: "Invalid credentials"})
                }
                if (error.response.status === 500){
                    setError("password", {type: "custom", message: "Server is not responding. " +
                            "Try again later"})
                }
            }
            );
    }


    return (
        <div className="row justify-content-center">
            <div className="col-lg-3 col-sm-6">
            <h3>Login</h3>
                <form method="post" onSubmit={handleSubmit(onSubmit)}>
                <input
                    placeholder="Username"
                    className="form-control"
                    {...register("username", {
                        required: "This field is required"
                    })}
                />
                    {errors.username && <p className="warning">{errors.username.message}</p>}

                    <input
                    placeholder="Password"
                    type="password"
                    className="form-control"
                    {...register("password", {
                        required: "This field is required"
                    })}
                />
                    {errors.password && <p className="warning">{errors.password.message}</p>}
                    <button className="btn btn-primary" type="submit">Login</button>
                </form>
                <Link to={`/signup`}>Sign Up</Link>
        </div>
        </div>
    )
}