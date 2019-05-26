import React from "react"

var snoowrap = require('snoowrap');


export default class Subreddit extends React.Component {
    constructor() {
        super()
        this.state = {
          posts: [],
          colors: []
        };
    }

    componentDidMount() {
      console.log("Enter Mount");

      const r = new snoowrap({
        userAgent: 'austin',
        clientId: 'BDrHDv25GKxYrw',
        clientSecret: 'ZoVdKRLzwAFRbwSa9JWpLBz5E5M',
        refreshToken: '58922884904-ltvIjQL0W4a_tFfVV_C0ZNTe7K4'
      })

      console.log("access reddit api");


      r.getSubreddit('nba').getHot().map(post => post.title)
        .then(textArray => {
          fetch('/test', {
            method: 'POST',
            body: JSON.stringify({
              textArray: textArray
            })
          }).then(res => res.json())
            .then(res => {
              this.setState({ colors: res.array });
            });
          });
          //end didmount
       console.log("exit did mount");
     }


    render() {
        return (
          <div>
            <p> IM IN Subreddit!</p>
          </div>
        )
    }
}
