import React, { useEffect } from "react";
import { useHistory } from 'react-router-dom';
import { useDispatch, useSelector } from 'react-redux';
import Box from '@material-ui/core/Box';
import Card from '@material-ui/core/Card';
import CardActions from '@material-ui/core/CardActions';
import CardContent from '@material-ui/core/CardContent';
import Button from '@material-ui/core/Button';
import Typography from '@material-ui/core/Typography';
import {getListBoard} from "../../state/board/reducerBoard";
import {selectBoards} from "../../state/board/selectorBoard";
import makeStyles from "@material-ui/core/styles/makeStyles";
import {createStyles} from "@material-ui/core";

const useStyles = makeStyles((theme) =>
  createStyles({
    root: {
      padding: 25,
      flex: 1,
      flexDirection: 'column',
      display: 'flex',
      justifyContent: 'center',
    },
      content:{
        flexGrow: 1,
        flexDirection: 'row',
      justifyContent: 'center',
      },
      card: {
        flexGrow: 3,
        margin: 5,
        border: "solid #5B6DCD 10px",
      },
  }),
);


const BoardsCards = () => {
    const classes = useStyles();
    const dispatch = useDispatch();
    const history = useHistory();

    const boards = useSelector(selectBoards);
    const handleClick = (boardId: number) => {
       history.push(`/board/${boardId}`)
    };

    useEffect(() => {
      dispatch(getListBoard());
    }, [dispatch]);


    return (
        <div className={classes.root}>
               <Typography variant="h2">Boards</Typography>
           <Box className={classes.content}>
               {boards.map( (board, id) =>  (
           <Card className={classes.card} variant="outlined" key={id}>
             <CardContent>
                  <Typography variant="h5" component="div">{board.name}</Typography>
                  <Typography> {board.preference} </Typography>
            </CardContent>
            <CardActions>
                  <Button onClick={() => handleClick(board.id)} size="small"> Open</Button>
            </CardActions>
           </Card>
                   ))}
            </Box>
        </div>
    );
};

export default BoardsCards;
