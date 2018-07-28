import React, {Component} from 'react';
import { connect } from 'react-redux';

import '../styles/App.css';
import BookList from '../components/BookList'

class App extends Component {
    render () {
        return (
            <div>
                <header>
                    <h1>Welcome to React "{this.props.user.username}"</h1>
                </header>
                <BookList/>
            </div>
        )
    }
}

function mapStateToProps (state) {
  console.log(state);
  return {
    user: state.authUser
  }
}

export default connect(mapStateToProps)(App);
