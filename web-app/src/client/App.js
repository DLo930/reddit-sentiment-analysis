import React, { Component } from 'react';
import './app.css';
import Subreddit from "./Subreddit"
import UserComs from "./UserComs"
import UserSubmiss from "./UserSubmiss"


export default class App extends Component {
  render() {
    return (
      <div>
      <p class = "test">Reddit Analyser</p>
            <div class="input-group input-group-lg input-group--username">
              <span id="u-addon" class="input-group-addon">/u/</span>
                <input type="text" placeholder="Username" aria-describedby="u-addon" autocapitalize="off" autocorrect="off" class="form-control username-input"/>
                </div>
                <div class = "button_gr1">
                <button type = "submit" class = "button_gr sub">Subreddit</button>
              <button type = "submit" class = "button_gr com">User Comments</button>
              <button type ="submit" class = "button_gr post">User Posts</button>
              </div>
      </div>
    );
  }
}
