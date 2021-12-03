import React, {useEffect} from 'react';
import {useDispatch, useSelector} from "react-redux";
import makeStyles from "@material-ui/core/styles/makeStyles";
import {createStyles} from "@material-ui/core";
import {getListBoardColumns} from "../../state/columns/reducerBoardColumns";
import {selectColumns} from "../../state/columns/selectorBoardColumns";
import Container from '@material-ui/core/Container';
import Paper from '@material-ui/core/Paper';
import Typography from "@material-ui/core/Typography";

type Props = {
    boardId: number;
};

const useStyles = makeStyles((theme) =>
  createStyles({
    root: {
      padding: 25,
      flex: 1,
      flexDirection: 'column',
      display: 'flex',
      justifyContent: 'center',
    },
  }),
);

const BoardColumns: React.FC<Props> = ({ boardId }) => {
    const classes = useStyles();
    const dispatch = useDispatch();
    const columns = useSelector(selectColumns);

    useEffect(() => {
      dispatch(getListBoardColumns(boardId));
    }, [boardId, dispatch]);
    return (
<Container className={classes.root}>
    {columns.map( (column, id) =>
        (

  <Paper elevation={3} >
      <Typography variant="h5" component="div">{column.name}</Typography>
  </Paper>
        )
    )}

</Container>

)};

export default BoardColumns;
