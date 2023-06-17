import axios from "axios"

// const dev = 'http://localhost:8000/'
const dev = 'http://10.100.102.11:8000/'

const API = axios.create({
  baseURL: dev 
})

export default API
