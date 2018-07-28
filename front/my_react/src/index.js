import React from 'react';
import ReactDOM from 'react-dom';
import { Provider } from 'react-redux';
import { createStore, applyMiddleware } from 'redux';
import { composeWithDevTools } from 'redux-devtools-extension';
import registerServiceWorker from './registerServiceWorker';
import thunk from 'redux-thunk';
import { Route, Router } from 'react-router';
import { HashRouter} from 'react-router-dom';

import './styles/index.css';
import App from './containers/App';
import configureStore from './store/configureStore';
import reducer from './reducers';

// const store = createStore(reducer, composeWithDevTools(applyMiddleware(thunk)));
const store = configureStore();

ReactDOM.render(
    <Provider store={store}>
        <App/>
    </Provider>
    , document.getElementById('root')
);

registerServiceWorker();
