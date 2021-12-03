
export type LoginFormData = {
  username: string;
  password: string;
};

export type LoginError = {
  message: string;
};

export type RefreshToken = {
  refresh: string;
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
