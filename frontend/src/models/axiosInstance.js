import axios from 'axios';
import useToken from '../components/useToken';


export const axiosInstance = axios.create({
  baseURL: 'http://127.0.0.1:8000/api/',
  headers: {'Authorization': 'Bearer ' + sessionStorage.getItem('access')}
});
