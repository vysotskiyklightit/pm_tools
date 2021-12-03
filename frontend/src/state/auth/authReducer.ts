import { createReducer, createAsyncThunk } from '@reduxjs/toolkit';
import { AxiosError } from 'axios';
import api, {getToken, refreshToken, userMe} from '../../api/apiController';
import {AuthState, LoginError, LoginFormData, RefreshToken, TokenResponse, UserState} from '../../types';

export const loginRequest = createAsyncThunk<TokenResponse, LoginFormData,
  {
    rejectValue: LoginError;
  }
>('login/getToken', async (formData, { rejectWithValue }) => {
  try {
    const { data } = await getToken(formData);

    api.defaults.headers.common.Authorization = `Bearer ${data.access}`;

    await localStorage.setItem('access', data.access);
    await localStorage.setItem('refresh', data.refresh);

    return data;
  } catch (e) {
    const error: AxiosError = e;

    if (!e.response) {
      throw e;
    }

    return rejectWithValue(error.response?.data);
  }
});

export const refreshTokenThunk = createAsyncThunk<TokenResponse, RefreshToken
    >('login/refreshToken', async (formData, { rejectWithValue }) => {
  try {

    const { data } = await refreshToken(formData);

    api.defaults.headers.common.Authorization = `Bearer ${data.access}`;

    await localStorage.setItem('access', data.access);

    return data;
  } catch (e) {
    const error: AxiosError = e;

    if (!e.response) {
      throw e;
    }

    return rejectWithValue(error.response?.data);
  }
});

export const autologin = createAsyncThunk<UserState, string>(
  'autologin',
  async (token, { rejectWithValue }) => {
    try {
      api.defaults.headers.common.Authorization = `Bearer ${token}`;

      const { data } = await userMe();

      return data;
    } catch (e) {
      const error: AxiosError = e;

      if (!e.response) {
        throw e;
      }

      return rejectWithValue(error.response?.data);
    }
  },
);

export const logout = createAsyncThunk('logout', async () => {
  delete api.defaults.headers.common.Authorization;

  localStorage.removeItem('access');
  localStorage.removeItem('refresh');
});

const initialState = {
  isLoggedIn: false,
  isFetching: false,
  user: {
    id: 0,
    username: '',
    email: '',
    groups: [],
  },
};

const authReducer = createReducer<AuthState>(initialState, {
  [loginRequest.fulfilled.type]: (state) => {
    state.isLoggedIn = true;
  },
  [loginRequest.rejected.type]: (state) => {
    state.isLoggedIn = false;
  },

  [logout.fulfilled.type]: () => initialState,

  [autologin.pending.type]: (state) => {
    state.isFetching = true;
  },
  [autologin.fulfilled.type]: (state, { payload }) => {
    state.isFetching = false;
    state.isLoggedIn = true;
    state.user = payload;
  },
  [autologin.rejected.type]: (state) => {
    state.isFetching = false;
    state.isLoggedIn = false;
  },
});

export default authReducer;
