import axios from 'axios';

let addr = process.env.VUE_APP_API_ROOT;
console.log(addr)
// fetch('./apiroot.txt').then((resp) => resp.text().then(string => addr = string))

export default new axios.create({
    'baseURL': addr,
})
