import React, { Component } from 'react';
import './app.css';
import Subreddit from "./Subreddit"
import UserComs from "./UserComs"
import UserSubmiss from "./UserSubmiss"

export default class App extends Component {
  render() {
    return (
      <div>
        <h1>Title</h1>
        <Subreddit/>
        <UserComs />
        <UserSubmiss />
      </div>
    );
  }
}
