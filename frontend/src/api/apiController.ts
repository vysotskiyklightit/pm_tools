import axios from 'axios';
import { ENDPOINTS } from '../constants';
import {LoginFormData, RefreshToken, TokenResponse, UserState} from "../types";

const port = process.env.REACT_APP_PORT;

const api = axios.create({
  baseURL:
    process.env.NODE_ENV === 'production'
      ? // eslint-disable-next-line no-restricted-globals
        `${location.protocol}//${location.hostname}:${port}`
      : 'http://localhost:8001',
  headers: {
    'Content-Type': 'application/json',
  },
});
api.interceptors.response.use(
    (response) => {
      return response
    },
    async (error) => {
        const response = error.response
      if (response && response.status === 401){
          console.log(response.body.detail)
      }
    }
);

export const getToken = (formData: LoginFormData) => api.post<TokenResponse>(ENDPOINTS.authToken, formData);
export const refreshToken = (formData: RefreshToken) => api.post<TokenResponse>(ENDPOINTS.refreshToken, formData);
export const userMe = () => api.get<UserState>(ENDPOINTS.user_me);

export default api;
