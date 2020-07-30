import axios from 'axios';


export default axios.create({
  baseURL:'https://findrecipe.herokuapp.com/api'
})