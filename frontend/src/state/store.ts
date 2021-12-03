import { configureStore, combineReducers } from '@reduxjs/toolkit';
import authReducer from './auth/authReducer'
import boardReducer from "./board/reducerBoard";
import boardColumnReducer from "./columns/reducerBoardColumns";

const rootReducer = combineReducers({
  auth: authReducer,
  boards: boardReducer,
  columns: boardColumnReducer,
});
export type RootState = ReturnType<typeof rootReducer>;

const store = configureStore({
  reducer: rootReducer,
});

export default store;
