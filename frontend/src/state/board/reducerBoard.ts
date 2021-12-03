import {createAsyncThunk, createReducer} from "@reduxjs/toolkit";
import { getBoards } from "../../api/apiController";
import {AxiosError} from "axios";
import {BoardsState} from "../../types";


export const getListBoard = createAsyncThunk<any>(
  'listBoard/getRequest',
  async ( any, { rejectWithValue }) => {
    try {
      const { data } = await getBoards();

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

const initialState = {
  isFetching: false,
  data: [],
};

const boardReducer = createReducer<BoardsState>(initialState, {
  [getListBoard.fulfilled.type]: (state, { payload }) => {
    state.data = payload;
    state.isFetching = true;
  },
  [getListBoard.rejected.type]: (state) => {
    state.isFetching = false;
  },

});

export default boardReducer;
