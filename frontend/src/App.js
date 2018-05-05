import React, { Component } from 'react';
import Login from './components/login';
import Home from './components/home';

class App extends Component {
  state = {
    cashe: JSON.parse(localStorage.getItem('auth')),
  }
  setAuth = () => {
    this.setState({cashe: JSON.parse(localStorage.getItem('auth'))});
  }
  LogOut = () => {
    localStorage.removeItem('auth');
    this.setState({cashe: ''});
  }
  render() {
    return (
      <div className="container">
        {this.state.cashe ? (<Home cashe={this.state.cashe} LogOut={this.LogOut}/>) : (<Login setAuth={this.setAuth}/>)}
      </div>
    );
  }
}

export default App;
