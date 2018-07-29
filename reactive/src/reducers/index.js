import { combineReducers } from 'redux';

import books from './books';
import auth from './auth';
import authUser from './user';

const rootReducer =  combineReducers({
    books,
    auth,
    authUser,
});

export default rootReducer;
