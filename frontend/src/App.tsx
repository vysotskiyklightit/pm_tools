import React from 'react';
import { useSelector } from 'react-redux';
import { BrowserRouter, Route, Switch, Redirect } from 'react-router-dom';
import { selectIsLoggedIn } from './state/auth/authSelectors';
import CssBaseline from '@material-ui/core/CssBaseline';
import Authorization from './components/wrappers/Authorization'
import Layout from "./components/layouts/layout";

const PrivateRoute: React.FC<any> = ({ children, ...rest }) => {
  const isLoggedIn = useSelector(selectIsLoggedIn);

  return (
    <Route {...rest}>
      {isLoggedIn ? children : <Redirect to={{ pathname: '/login' }} />}
    </Route>
  );
};

const App = () => {
  return (
    <BrowserRouter>
        <CssBaseline>
      <Authorization>
      <Switch>
        <PrivateRoute exact path="/">
            <Layout>
          <div>Home</div>
            </Layout>
        </PrivateRoute>
      </Switch>
      </Authorization>
            </CssBaseline>
    </BrowserRouter>
  );
}

export default App;
