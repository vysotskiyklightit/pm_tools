import React from 'react';
import { useDispatch } from 'react-redux';
import Toolbar from '@material-ui/core/Toolbar';
import Typography from '@material-ui/core/Typography';
import makeStyles from '@material-ui/core/styles/makeStyles';
import { createStyles } from '@material-ui/core';
import Button from '@material-ui/core/Button';
import clsx from 'clsx';
import {logout} from "../../state/auth/authReducer";


const useStyles = makeStyles((theme) =>
  createStyles({
    root: {
      padding: 0,
      flex: 1,
      display: 'flex',
    },
    subheader: {
      padding: theme.spacing(0, 2),
      flexGrow: 1,
    },
    controls: {
      display: 'flex',
      flexDirection: 'row',
      padding: theme.spacing(0, 5),
    },
    hoverableButton: {
      '&:hover': {
        color: theme.palette.primary.main,
        backgroundColor: theme.palette.secondary.main,
      },
    },
    logoutButton: {
      textTransform: 'capitalize',
      '& i.fas, & i.far': {
        marginRight: theme.spacing(1),
      },
    },
    link: {
      textDecoration: 'none',
    },
  }),
);
const NavBar: React.FC = () => {
    const classes = useStyles();
    const dispatch = useDispatch();
    const handleLogoutClick = () => {
      dispatch(logout)
    };
    return (
 <Toolbar className={classes.root} variant="dense">
      <Typography variant="h6" noWrap className={classes.subheader}>
        Board
      </Typography>

      <div className={classes.controls}>
        <Button
          onClick={handleLogoutClick}
          color="secondary"
          className={clsx(classes.logoutButton, classes.hoverableButton)}
        >
          <i className="far fa-user" />
          {/* eslint-disable-next-line */}
          Admin |<i>&nbsp;Logout</i>
        </Button>
      </div>
    </Toolbar>
    );
};

export default NavBar;
