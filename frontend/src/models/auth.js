import axios from 'axios';


async function loginUser(data) {
  return axios.post("http://127.0.0.1:8000/api/token/", {username: data.username, password: data.password})
    .then(res => res);
};

export default loginUser;
