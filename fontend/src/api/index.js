import axios from 'axios'

var api = axios.create({
  baseURL: 'http://localhost:8000'
})

export default api
