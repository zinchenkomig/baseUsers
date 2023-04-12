import './style.css'
import axios from "../api/backend";
import { useForm } from "react-hook-form";



export default function SignUp(){
    const { register, watch, handleSubmit, setError, formState: { errors } } = useForm({mode: "onBlur"});

    async function validate_username(username){
        const is_exists = await axios.get('/check/username', {params: {username: username}})
            .then((response)=>{return response.data;}
            )
            .catch((reason)=>{console.log(reason)})
        return !is_exists || `Username ${username} already exists`
    }

    function onSubmit(data) {
        axios.post('/auth/register', data)
            .then(function (response) {
                console.log(response);
            })
            .catch(function (error) {
                if (error.response.status===409){
                    setError("username", {type: "focus", message: "Username already exists"})
                }
            });
    }

    return (
        <div className="row justify-content-center">
            <div className="col-lg-3 col-sm-6">
            <h3>Sign Up Form</h3>
                <form method="post" onSubmit={handleSubmit(onSubmit)}>
                <input
                    placeholder="Username"
                    className="form-control"
                    {...register("username", {
                        required: "This field is required",
                        minLength: {
                            value: 4,
                            message: "Minimum length is 4"
                        },
                        validate: validate_username
                    })}
                />
                    {errors.username && <p className="warning">{errors.username.message}</p>}
                <input
                    placeholder="E-Mail"
                    className="form-control"
                    type="email"
                    {...register("email", {
                        pattern: {
                            value: /^[\w-.]+@([\w-]+\.)+[\w-]{2,4}$/g,
                            message: 'Invalid email format'
                    }
                    })}
                />
                    {errors.email && <p className="warning">{errors.email.message}</p>}

                    <input
                    placeholder="Password"
                    type="password"
                    className="form-control"
                    {...register("password", {
                        required: "This field is required",
                        minLength: {
                            value: 6,
                            message: "Minimum password length is 6"
                        }
                    })}
                />
                    {errors.password && <p className="warning">{errors.password.message}</p>}
                    <input
                        placeholder="Repeat password"
                        type="password"
                        className="form-control"
                        {...register("repeat_password", {
                            validate: (value) => {
                                if (watch('password') !== value) {
                                    return "Your passwords do not match";
                                }
                            }
                        })}
                    />
                    {errors.repeat_password && <p className="warning">{errors.repeat_password.message}</p>}
                <button className="btn btn-primary" type="submit">Submit</button>
                </form>
        </div>
        </div>
    )
}