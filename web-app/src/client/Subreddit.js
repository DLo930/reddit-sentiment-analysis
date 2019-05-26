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
        this.zip = this.zip.bind(this);
    }

    zip(A, B) {
      return A.map((e, i) => {
        return [ e, B[i] ];
      });
    }


    componentDidMount() {
      const r = new snoowrap({
        userAgent: 'austin',
        clientId: 'BDrHDv25GKxYrw',
        clientSecret: 'ZoVdKRLzwAFRbwSa9JWpLBz5E5M',
        refreshToken: '58922884904-ltvIjQL0W4a_tFfVV_C0ZNTe7K4'
      });

      r.getSubreddit(this.state.theSub).getHot().map(post => {
        fetch('/getColors', {
          method: 'POST',
          body: {
            'text': post.title
          }
        })
          .then(color => {
            var posts = this.state.posts.concat(post.title);
            var colors = this.state.colors.concat(color);
            this.setState({
              posts: posts,
              colors: colors
            });
          });
        console.log(this.zip(this.state.posts, this.state.colors));
      });
     }

    render() {
        return (
          <div>
            {
              this.zip(this.state.posts, this.state.colors).map(elem => {
                <div style={{ color: elem[1] }}>
                  <h3>{elem[0]}</h3>
                </div>
              })
            }
          </div>
        )
    }
}
