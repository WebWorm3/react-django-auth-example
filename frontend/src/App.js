import React, { Component } from 'react';
import Login from './components/login';
import Home from './components/home';

class App extends Component {
  state = {
    cashed_user: localStorage.getItem('user'),
  }
  setAuth = () => {
    this.setState({cashed_user: localStorage.getItem('user')});
  }
  LogOut = () => {
    localStorage.removeItem('user');
    this.setState({cashed_user: ''});
  }
  render() {
    return (
      <div className="container">
        {this.state.cashed_user ? (<Home cashed_user={this.state.cashed_user} LogOut={this.LogOut}/>) : (<Login setAuth={this.setAuth}/>)}
      </div>
    );
  }
}

export default App;
