import React, { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { useHistory } from 'react-router-dom';
import { selectIsLoggedIn, selectIsUserFetching ,selectUsername} from '../../state/auth/authSelectors'
import { autologin, logout } from '../../state/auth/authReducer';
import LoginForm from '../LoginForm'

const Authorization: React.FC = ({ children }) => {
  const dispatch = useDispatch();
  const history = useHistory();

  const isLoggedIn = useSelector(selectIsLoggedIn);
  const isFetching = useSelector(selectIsUserFetching);
  const username = useSelector(selectUsername);

  useEffect(() => {
    const autolog = async () => {
      const autotoken = await localStorage.getItem('access');

      if (!autotoken) {
          await dispatch(logout());
      } else {
        await dispatch(autologin(autotoken));
      }

    };

    if (!isLoggedIn) {
      autolog();
    }

  }, [isLoggedIn, dispatch, username, history]);

  return isLoggedIn ? <>{children}</> : <LoginForm />;
};

export default Authorization;
