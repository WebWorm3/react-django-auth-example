import React, { Component } from 'react';
import Cookies from 'universal-cookie';
import Login from './components/login';
import Home from './components/home';

const cookies = new Cookies();

class App extends Component {
  state = {
    cookie_user: cookies.get('user'),
  }
  setAuth = () => {
    this.setState({cookie_user: cookies.get('user')});
  }
  LogOut = () => {
    cookies.remove('user');
    this.setState({cookie_user: ''});
  }
  render() {
    return (
      <div className="container">
        {this.state.cookie_user ? (<Home cookie_user={this.state.cookie_user} LogOut={this.LogOut}/>) : (<Login setAuth={this.setAuth}/>)}
      </div>
    );
  }
}

export default App;
