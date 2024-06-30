import axios from 'axios';

const apiClient = axios.create({ 
    baseURL: 'http://127.0.0.1:8000/',
    // baseURL: 'http://192.168.1.10:8000/',
})


export default apiClient;