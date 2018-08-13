import React from 'react'
import { connect } from 'react-redux'
import { Redirect } from 'react-router'

import {authErrors, isAuthenticated} from '../reducers'
import {login} from  '../actions/auth'
import {register} from  '../actions/auth'
import RegisterForm from '../components/RegisterForm'


const Register = (props) => {
  if(props.isAuthenticated) {
    return (
      <Redirect to='/' />
    )
  } else {
      return (
          <div className="login-page">
              <RegisterForm {...props}/>
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
    dispatch(register(username, password))
        .then(
            () => dispatch(login(username, password))
        )
  }
});

export default connect(mapStateToProps, mapDispatchToProps)(Register);
