import React, { Component } from 'react';
import './app.css';

export default class App extends Component {
  render() {
    return (
      <div>
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

      </div>
    );
  }
}
