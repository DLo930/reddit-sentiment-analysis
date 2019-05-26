import React, { Component } from 'react';
import './app.css';
import Subreddit from "./Subreddit"
import UserComs from "./UserComs"
import UserSubmiss from "./UserSubmiss"

export default class App extends Component {
  render() {
    return (
      <div>
<<<<<<< HEAD
      <p class = "test">Reddit Analyser</p>
            <div class="input-group input-group-lg input-group--username">
              <span id="u-addon" class="input-group-addon">/u/</span>
                <input type="text" placeholder="Username" aria-describedby="u-addon" autocapitalize="off" autocorrect="off" class="form-control username-input"/>
                  <span class="input-group-btn">
                    <button type="button" class="btn btn-secondary">Analyse</button>
                    </span>
                    <button type = "submit" class = "reddit">Reddit</button>
                  <button type = "button" class = "twitter">Twitter</button>
                  <button type ="button" class = "fb"> Facebook</button> 
                </div>

=======
        <h1>Title</h1>
        <Subreddit/>
        <UserComs />
        <UserSubmiss />
>>>>>>> d2e2cf42ad7c7385f82d43bc01b7c0620149342c
      </div>
    );
  }
}
