import axios from 'axios';

export function fetchBooksWithRedux() {
  return dispatch => {
    axios.get("http://127.0.0.1:8000/books/")
        .then(function (response) {
          dispatch(fetchBooksSuccess(response.data));
        })
  };
}

export const fetchBooksSuccess = books => ({
  type: 'FETCH_BOOKS_SUCCESS',
  payload: { books }
});
