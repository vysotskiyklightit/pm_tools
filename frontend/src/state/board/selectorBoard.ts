import { RootState } from '../store';

export const selectBoards = ({ boards }: RootState) => boards.data;
