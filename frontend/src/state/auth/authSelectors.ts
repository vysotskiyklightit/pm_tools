import { RootState } from '../store';

export const selectIsLoggedIn = ({ auth }: RootState) => auth.isLoggedIn;

export const selectIsUserFetching = ({ auth }: RootState) => auth.isFetching;

export const selectUsername = ({ auth }: RootState) => auth.user.username;
