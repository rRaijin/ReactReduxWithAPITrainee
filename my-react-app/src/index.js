import 'bootstrap/dist/css/bootstrap.css';
import createHistory from 'history/createBrowserHistory';
import React from 'react';
import ReactDOM from 'react-dom';
import {Route, Switch, Link} from 'react-router-dom';
import { ConnectedRouter } from 'react-router-redux';
import { Provider } from 'react-redux';

import './index.css';
import App from './App';
import configureStore from './store';
import Login from './containers/Login';
import Register from './containers/Register';
import registerServiceWorker from "./registerServiceWorker";
import PrivateRoute from './containers/PrivateRoute';


const history = createHistory();
const store = configureStore(history);


ReactDOM.render((
    <Provider store={store}>
        <ConnectedRouter history={history}>
            <div>
                <ul>
                    <li><Link to="/register/">register</Link></li>
                    <li><Link to="/login/">login</Link></li>
                </ul>
            <Switch>
                <Route path="/login/" component={Login} />
                <Route path="/register/" component={Register} />
                <PrivateRoute path="/" component={App}/>
            </Switch>
            </div>
        </ConnectedRouter>
    </Provider>
), document.getElementById('root'));

registerServiceWorker();
