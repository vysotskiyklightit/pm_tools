import React from "react";
import CssBaseline from '@material-ui/core/CssBaseline';
import clsx from 'clsx';
import { makeStyles, Theme, createStyles } from '@material-ui/core/styles';
import Toolbar from '@material-ui/core/Toolbar';
import AppBar from '@material-ui/core/AppBar';
import NavBar from './NavBar';

const drawerWidth = 240;

const useStyles = makeStyles((theme: Theme) =>
  createStyles({
    root: {
      display: 'flex',
    },
    appBar: {
      display: 'flex',
      flexDirection: 'row',
      transition: theme.transitions.create(['margin', 'width'], {
        easing: theme.transitions.easing.sharp,
        duration: theme.transitions.duration.leavingScreen,
      }),
    },
    appBarShift: {
      width: `calc(100% - ${drawerWidth}px)`,
      marginLeft: drawerWidth,
      transition: theme.transitions.create(['margin', 'width'], {
        easing: theme.transitions.easing.easeOut,
        duration: theme.transitions.duration.enteringScreen,
      }),
    },
    menuButton: {
      marginLeft: theme.spacing(1),
    },
    drawer: {
      width: drawerWidth,
      flexShrink: 0,
    },
    drawerPaper: {
      backgroundColor: theme.palette.primary.main,
      color: theme.palette.secondary.main,
      width: drawerWidth,
    },
    drawerHeader: {
      display: 'flex',
      alignItems: 'center',
      padding: theme.spacing(0, 1),
      // necessary for content to be below app bar
      height: theme.spacing(6),
      justifyContent: 'flex-end',
    },
    content: {
      '& .fas, & .far': {
        marginRight: theme.spacing(1),
      },
      backgroundColor: theme.palette.background.default,
      flexGrow: 1,
      padding: theme.spacing(3),
      transition: theme.transitions.create('margin', {
        easing: theme.transitions.easing.sharp,
        duration: theme.transitions.duration.leavingScreen,
      }),
      marginLeft: -drawerWidth,
    },
    drawerContainer: {
      overflow: 'auto',
    },
    contentShift: {
      transition: theme.transitions.create('margin', {
        easing: theme.transitions.easing.easeOut,
        duration: theme.transitions.duration.enteringScreen,
      }),
      marginLeft: 0,
    },
  }),
);

const Layout: React.FC = ({ children }) => {
  const classes = useStyles();
  const [open, setOpen] = React.useState(false);

    return (
    <div className={classes.root}>
      <CssBaseline />

        <AppBar
        position="fixed"
        className={clsx(classes.appBar, {
          [classes.appBarShift]: open,
        })}
      >
<NavBar />
      </AppBar>
         <main
        className={clsx(classes.content, {
          [classes.contentShift]: open,
        })}
      >
        <Toolbar variant="dense" />
        {children}
      </main>
</div>
    );
};

export default Layout;
