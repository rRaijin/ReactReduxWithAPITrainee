import React from "react";

const Book = ({ book }) => (
    <div>
        <span>{ book.id } - { book.title }</span>
        <span>{ book.description }</span>
    </div>
);

export default Book;
