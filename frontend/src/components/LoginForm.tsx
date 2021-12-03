import React from 'react';
import { Field, Form } from 'react-final-form';
import {
  Button,
  Container,
  createStyles,
  TextField,
  Theme,
  Typography,
} from '@material-ui/core';
import { FORM_ERROR } from 'final-form';
import Divider from '@material-ui/core/Divider';
import { makeStyles } from '@material-ui/core/styles';
import { useDispatch } from "react-redux";
import { LoginFormData } from '../types'
import { loginRequest } from '../state/auth/authReducer'

const useStyles = makeStyles((theme: Theme) =>
  createStyles({
    paper: {
      marginTop: theme.spacing(8),
      display: 'flex',
      flexDirection: 'column',
      alignItems: 'center',
    },
    avatar: {
      margin: theme.spacing(1),
      backgroundColor: theme.palette.primary.light,
    },
    form: {
      width: '100%', // Fix IE 11 issue.
      marginTop: theme.spacing(1),
    },
    submitButton: {
      margin: theme.spacing(3, 0, 2),
    },
    root: {
      height: '100vh',
      display: 'flex',
      alignItems: 'center',
      justifyContent: 'center',
    },
    header: {
      margin: theme.spacing(6),
    },
    subheader: {
      '& > i': {
        color: theme.palette.primary.main,
      },
    },
  }),
);

const LoginForm: React.FC = () => {
  const classes = useStyles();
  const dispatch = useDispatch()
  const onSubmit = async (values: LoginFormData) => {
      const { payload, error }: any = await dispatch(loginRequest(values));
      return typeof payload?.message === 'object'
      ? payload?.message
      : {
          [FORM_ERROR]: payload?.message || error?.message,
        };
  };

  return (
    <Container component="main" maxWidth="xs">
      <div className={classes.paper}>
        <Typography component="h1" variant="h3" className={classes.header}>
          Sign in
        </Typography>

        <Divider />

        <Typography component="h2" variant="h4" className={classes.subheader}>
          <i className="fas fa-paper-plane" />
          Board
        </Typography>

        <Form
          onSubmit={onSubmit}
          render={({ handleSubmit, submitting, submitError }) => (
            <form onSubmit={handleSubmit} className={classes.form}>
              <Field
                name="username"
              >
                {({ input, meta }) => (
                  <TextField
                    variant="outlined"
                    margin="normal"
                    required
                    fullWidth
                    label="Username"
                    {...input}
                    error={(meta.error || meta.submitError) && meta.touched}
                    helperText={
                      (meta.error || meta.submitError) && meta.touched
                        ? meta.error || meta.submitError
                        : null
                    }
                  />
                )}
              </Field>

              <Field
                name="password"
              >
                {({ input, meta }) => (
                  <TextField
                    variant="outlined"
                    margin="normal"
                    required
                    fullWidth
                    autoComplete="current-password"
                    label="Password"
                    type="password"
                    {...input}
                    error={(meta.error || meta.submitError) && meta.touched}
                    helperText={
                      (meta.error || meta.submitError) && meta.touched
                        ? meta.error || meta.submitError
                        : null
                    }
                  />
                )}
              </Field>

              <Button
                type="submit"
                fullWidth
                variant="contained"
                color="secondary"
                className={classes.submitButton}
                disabled={submitting}
              >
                Log in
              </Button>

            </form>
          )}
        />
      </div>
    </Container>
  );
};

export default LoginForm;
