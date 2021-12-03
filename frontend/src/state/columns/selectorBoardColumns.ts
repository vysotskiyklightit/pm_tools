import { RootState } from '../store';

export const selectColumns = ({ columns }: RootState) => columns.data;
