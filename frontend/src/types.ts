import BoardColumns from "./components/Board/boardColumns";

export type LoginFormData = {
  username: string;
  password: string;
};

export type LoginError = {
  message: string;
};

export type RefreshToken = {
  refresh: string | null;
};

export type TokenResponse = {
  access: string;
  refresh: string;
};

export type AuthState = {
  isLoggedIn: boolean;
  isFetching: boolean;
  user: UserState;
};

export type UserState = {
  id: number;
  username: string;
  email: string;
  groups: string[];
};

export type BoardList = {
  data: Board[];
};

export type Board = {
  id: number;
  name: string;
  preference: string;
  owner: number;
  contributors: number[];
};

export type BoardsState = {
  isFetching: boolean;
  data: Board[];
};

export type ColumnsState = {
  isFetching: boolean;
  data: BoardColumn[];
};

export type BoardColumnsResponse = {
  count: number;
  next: string | null;
  previous: string | null;
  results: BoardColumn[];
};

export type BoardColumn = {
  id: number;
  name: string;
};
