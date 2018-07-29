import React, {Component} from 'react';
import { connect } from 'react-redux';

import logo from '../logo.svg';
import '../styles/App.css';
import BookList from '../components/BookList'

class App extends Component {
    render () {
        return (
            <div>
                <header className="App-header">
                    <img src={logo} className="App-logo" alt="logo" />
                    <h1 className="App-title">Welcome to React "{this.props.user.username}"</h1>
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
