import React, { Component } from 'react';
import './css/app.css';
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
    event.preventDefault();
    this.setState({
      searchVal: this.state.value,
      subredBool: true
    });
  }

  handleUserComs(event) {
    event.preventDefault();
    this.setState({
      searchVal: this.state.value,
      usercomBool: true
    });
  }

  handleUserSubmiss(event) {
    event.preventDefault();
    this.setState({
      searchVal: this.state.value,
      usersubmissBool: true
    });
  }

  render() {
    return (
      <div>
        <h1>The Reddit Sentiment Analyzer</h1>
        <h2>Because the Internet is (not) a wonderful place.</h2>
        <form>
          <span class="input">
            <input type="text" value={this.state.value} onChange={this.handleChange} placeholder="Subreddit/User" aria-describedby="u-addon" autocapitalize="off" autocorrect="off" class="inpText"/>
            <span></span>
          </span>
          <br/>
          <br/>
          <div class="inp">
            <button type = "submit" class="pushy__btn pushy__btn--lg pushy__btn--blue" name="subred" onClick={this.handleSubmitSubred}>Subreddit</button>
            <button type = "submit" class="pushy__btn pushy__btn--lg pushy__btn--green" name="usercoms" onClick={this.handleUserComs}>User Comments</button>
            <button type ="submit" class="pushy__btn pushy__btn--lg pushy__btn--red" name="usersubmiss" onClick={this.handleUserSubmiss}>User Posts</button>
          </div>
        </form>
        {this.state.subredBool && <Subreddit theSub={this.state.searchVal} />}
        {this.state.usercomBool && <UserComs theUser={this.state.searchVal} />}
        {this.state.usersubmissBool && <UserSubmiss theUser={this.state.searchVal} />}
      </div>
    );
  }
}
