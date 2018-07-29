import React, { Component } from "react";
import { connect } from "react-redux";
import { fetchBooksWithRedux } from "../actions/bookActions";
import Book from "./Book";

class BookList extends Component {
  componentDidMount() {
    this.props.dispatch(fetchBooksWithRedux());
  }

  render() {
    const books = this.props.books;

    return (
      <div>
        <ul>
          { books.map(book =>
            <li key={ book.id }>
                <Book book={ book } />
            </li>
          )}
        </ul>
      </div>
    );
  }
}

const mapStateToProps = state => ({
  books: state.books.items
});

export default connect(mapStateToProps)(BookList);
