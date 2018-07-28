import { FETCH_BOOKS_SUCCESS } from '../constants/index'

const initialState = {
  items: []
};

export default function books(state = initialState, action) {
  switch (action.type) {
    case FETCH_BOOKS_SUCCESS:
        return {
            ...state,
            items: action.payload.books
        };
    // case "ADD_BOOK_SUCCESS":
    //     return {
    //         ...state,
    //         items: action.payload
    //     };
    default:
      return state;
  }
}
