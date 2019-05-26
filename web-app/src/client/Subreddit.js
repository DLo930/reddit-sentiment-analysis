import React from "react"

var snoowrap = require('snoowrap');



export default class Subreddit extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
          theSub: props.theSub,
          posts: [],
          colors: []
        };
    }


    componentDidMount() {

      const r = new snoowrap({
        userAgent: 'austin',
        clientId: 'BDrHDv25GKxYrw',
        clientSecret: 'ZoVdKRLzwAFRbwSa9JWpLBz5E5M',
        refreshToken: '58922884904-ltvIjQL0W4a_tFfVV_C0ZNTe7K4'
      })

      r.getSubreddit(this.state.theSub).getHot().map(post => post.title)
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
     }

    render() {
        return (
          <div>
            <p> IM IN Subreddit!</p>
          </div>
        )
    }
}
