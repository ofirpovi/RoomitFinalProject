import axios from "axios"

// const dev = 'http://localhost:8000/'
const dev = 'http://192.168.1.119:8000/'

const API = axios.create({
  baseURL: dev 
})

export default API
