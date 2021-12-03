import React from 'react';
import { useSelector } from 'react-redux';
import { BrowserRouter, Route, Switch, Redirect } from 'react-router-dom';
import { selectIsLoggedIn } from './state/auth/authSelectors';
import CssBaseline from '@material-ui/core/CssBaseline';
import Authorization from './components/wrappers/Authorization'
import Layout from "./components/layouts/layout";
import BoardsCards from "./components/Home/BoardsCards";
import BoardDetail from "./components/Board/boardDetail";

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
        <CssBaseline />
      <Authorization>
      <Switch>
        <PrivateRoute exact path="/">
            <Layout>
          <BoardsCards />
            </Layout>
        </PrivateRoute>
          <PrivateRoute
              exact
              path="/board/:id"
              render={({ match: { params } }: any) => (
                <Layout>
                  <BoardDetail boardId={params.id} />
                </Layout>
              )}
            />
      </Switch>
      </Authorization>
    </BrowserRouter>
  );
}

export default App;
