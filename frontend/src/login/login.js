import './style.css'
import axios from "../api/backend";
import { useForm } from "react-hook-form";
import {Link} from "react-router-dom";
import { useNavigate } from "react-router-dom";


export default function Login(){
    const { register, handleSubmit, formState: { errors } } = useForm({mode: "onBlur"});
    const navigate = useNavigate();

    async function onSubmit(data) {
        let dataForm = new FormData()
        dataForm.append('username', data['username'])
        dataForm.append('password', data['password'])

        const response = await axios.post('/auth/token', dataForm)
            .then((response) => {
                return response;
            }).catch((error)=>{console.log(error)});
        if (response.status === 200) {
            navigate('/profile');
        }
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