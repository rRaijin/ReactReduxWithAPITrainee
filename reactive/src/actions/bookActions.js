import axios from 'axios';
import { FETCH_BOOKS_SUCCESS } from '../constants/index';

const local_url = 'http://127.0.0.1:8000/';

export function fetchBooksWithRedux() {
  return dispatch => {
    axios.get(local_url + "books/")
        .then(function (response) {
          dispatch(fetchBooksSuccess(response.data));
        })
  };
}

export const fetchBooksSuccess = books => ({
  type: FETCH_BOOKS_SUCCESS,
  payload: { books }
});
