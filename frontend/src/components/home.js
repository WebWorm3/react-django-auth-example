import React, { Component } from 'react';

export default class Home extends Component{
    render(){
      return(
        <div className="center">
          <h3>Logged as {this.props.cookie_user}</h3>
          <button onClick={this.props.LogOut} className="btn btn-danger">Log out</button>
        </div>
      );
    }
}
