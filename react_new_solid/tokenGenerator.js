import axios from "axios";

async function getCsrfToken() {
    const loginResponse = await axios.get('http://192.168.1.171:8000/user/get-csrf-token/');
    const csrfTokenHeader = loginResponse.headers['set-cookie']
      .find(cookie => cookie.startsWith('csrftoken'));
    if (csrfTokenHeader) {
      const csrfToken = csrfTokenHeader.split('=')[1].split(';')[0];
      return csrfToken;
    }
  }

  export const tokenGenerator = {
    getCsrfToken
  }