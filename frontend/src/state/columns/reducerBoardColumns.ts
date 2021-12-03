import {createAsyncThunk, createReducer} from "@reduxjs/toolkit";
import { getBoardsColumns } from "../../api/apiController";
import {AxiosError} from "axios";
import {ColumnsState} from "../../types";


export const getListBoardColumns = createAsyncThunk(
  'listBoard/getRequest',
  async ( boardId: number, { rejectWithValue }) => {
    try {
      const { data } = await getBoardsColumns(boardId);

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

const boardColumnReducer = createReducer<ColumnsState>(initialState, {
  [getListBoardColumns.fulfilled.type]: (state, { payload }) => {
    state.data = payload.results;
    state.isFetching = true;
  },
  [getListBoardColumns.rejected.type]: (state) => {
    state.isFetching = false;
  },

});

export default boardColumnReducer;
