import React from 'react';
import ReactDOM from 'react-dom';
import { Provider } from 'react-redux';
import registerServiceWorker from './registerServiceWorker';
import { Route, Router } from 'react-router';

import './styles/index.css';
import App from './containers/App';
import configureStore from './store/configureStore';
// import { createBrowserHistory } from 'history';
//
// const history = createBrowserHistory();
import { history } from './history';

const store = configureStore();

ReactDOM.render(
    <Provider store={store}>
        <Router history={history}>
            <Route path="/" component={App} />
        </Router>
    </Provider>,
    document.getElementById('root')
);

registerServiceWorker();
