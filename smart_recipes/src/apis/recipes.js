import axios from 'axios';


export default axios.create({
  baseURL:'http://findrecipe.herokuapp.com/api'
})