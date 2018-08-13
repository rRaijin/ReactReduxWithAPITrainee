import React from 'react'
import { connect } from 'react-redux'
import { Redirect } from 'react-router'

import {authErrors, isAuthenticated} from '../reducers'
import LoginForm from '../components/LoginForm'
import {login} from  '../actions/auth'


const Login = (props) => {
  if(props.isAuthenticated) {
    return (
      <Redirect to='/' />
    )
  } else {
      return (
          <div className="login-page">
              <h1>login</h1>
              <LoginForm {...props}/>
          </div>
      )
  }
};

const mapStateToProps = (state) => ({
  errors: authErrors(state),
  isAuthenticated: isAuthenticated(state)
});

const mapDispatchToProps = (dispatch) => ({
  onSubmit: (username, password) => {
    dispatch(login(username, password))
  }
});

export default connect(mapStateToProps, mapDispatchToProps)(Login);
