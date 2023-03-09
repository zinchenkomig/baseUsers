import axios from "axios";

const backend_base = "http://127.0.0.1:8000"


export default axios.create({
    baseURL: backend_base,
    withCredentials: true,
});
