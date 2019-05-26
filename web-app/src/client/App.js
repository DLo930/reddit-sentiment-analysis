import React, { Component } from 'react';
import './app.css';
import Subreddit from "./Subreddit"
import UserComs from "./UserComs"
import UserSubmiss from "./UserSubmiss"


export default class App extends Component {

  constructor(props) {
    super(props);
    this.state = {
      value: '',
      searchVal: '',
      subredBool: false,
      usercomBool: false,
      usersubmissBool: false
  };

    this.handleChange = this.handleChange.bind(this);
    this.handleSubmitSubred = this.handleSubmitSubred.bind(this);
    this.handleUserComs = this.handleUserComs.bind(this);
    this.handleUserSubmiss = this.handleUserSubmiss.bind(this);
  }

  handleChange(event) {
    this.setState({
      value: event.target.value.toLowerCase()
    });
  }

  handleSubmitSubred(event) {
    alert('A subreddit was submitted: ' + this.state.value);
    event.preventDefault();
    this.setState({
      searchVal: this.state.value,
      subredBool: true
    });
  }

  handleUserComs(event) {
    alert('A user (for comments) was submitted: ' + this.state.value);
    event.preventDefault();
    this.setState({
      searchVal: this.state.value,
      usercomBool: true
    });
  }

  handleUserSubmiss(event) {
    alert('A user (for submissions) was submitted: ' + this.state.value);
    event.preventDefault();
    this.setState({
      searchVal: this.state.value,
      usersubmissBool: true
    });
  }

  render() {
    return (
      <div>
      <p class = "test">Reddit Analyser</p>
            <form>
              <div class="input-group input-group-lg input-group--username">
                  <span id="u-addon" class="input-group-addon">/u/</span>
                  <input type="text" value={this.state.value} onChange={this.handleChange} placeholder="Username" aria-describedby="u-addon" autocapitalize="off" autocorrect="off" class="form-control username-input"/>
              </div>
              <div class = "button_gr1">
                <button type = "submit" class = "button_gr sub" name="subred" onClick={this.handleSubmitSubred}>Subreddit</button>
                <button type = "submit" class = "button_gr com" name="usercoms" onClick={this.handleUserComs}>User Comments</button>
                <button type ="submit" class = "button_gr post" name="usersubmiss" onClick={this.handleUserSubmiss}>User Posts</button>
              </div>
            </form>
            {this.state.subredBool && <Subreddit theSub={this.state.searchVal} />}
            {this.state.usercomBool && <UserComs theUser={this.state.searchVal} />}
            {this.state.usersubmissBool && <UserSubmiss theUser={this.state.searchVal} />}
      </div>
    );
  }
}
