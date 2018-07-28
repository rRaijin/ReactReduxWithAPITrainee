import { combineReducers } from 'redux';

import books from './books';
import authUser from './user';

const rootReducer =  combineReducers({
    books,
    authUser
});

export default rootReducer;
