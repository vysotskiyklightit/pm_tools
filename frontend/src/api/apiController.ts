import axios from 'axios';
import { ENDPOINTS } from '../constants';
import {Board, BoardColumnsResponse, LoginFormData, RefreshToken, TokenResponse, UserState} from "../types";

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
      console.log(response.data)
      return response
    },
    async (error) => {
      const response = error.response
      const originalConfig = error.config;
      if (response && response.status === 401){
           try{
          const autotoken = await localStorage.getItem('refresh');
          const { data } = await refreshToken({refresh: autotoken});
          await localStorage.setItem('access', data.access)
          originalConfig.headers.Authorization = `Bearer ${data.access}`;
          return api(originalConfig);
           } catch (_error){
              // throw _error
             return Promise.reject(_error);
           }
      }
    }
);

export const getToken = (formData: LoginFormData) => api.post<TokenResponse>(ENDPOINTS.authToken, formData);
export const refreshToken = (formData: RefreshToken) => api.post<TokenResponse>(ENDPOINTS.refreshToken, formData);
export const userMe = () => api.get<UserState>(ENDPOINTS.user_me);
export const getBoards = () => api.get<Board[]>(ENDPOINTS.boardList);
export const getBoardsColumns = (boardId: number) => api.get<BoardColumnsResponse>(
     `${ENDPOINTS.boardList}${boardId}${ENDPOINTS.columnPart}`
);

export default api;
