import React from "react"

const snoowrap = require('snoowrap');

export default class Subreddit extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
          theSub: props.theSub,
          color: "#d3d3d3",
          posts: []
        };
        this.zip = this.zip.bind(this);
    }

    componentDidMount() {
      const r = new snoowrap({
        userAgent: 'austin',
        clientId: 'BDrHDv25GKxYrw',
        clientSecret: 'ZoVdKRLzwAFRbwSa9JWpLBz5E5M',
        refreshToken: '58922884904-ltvIjQL0W4a_tFfVV_C0ZNTe7K4'
      });

      var str = "";
      r.getSubreddit(this.state.theSub).getHot()
        .then(arr => {
          var tmpArr = [];
          for(var i = 0; i < arr.length; i++) {
            tmpArr.push(arr[i].title);
            str = str.concat(" "+arr[i].title);
          }
          fetch('/getColors', {
            method: 'POST',
            headers: {
              "Accept": "application/json",
              "Content-Type": "application/json"
            },
            body: JSON.stringify({
              'text': str
            })
          })
            .then(res => {
              console.log(res);
              // console.log(res.color);
              console.log(tmpArr);
              this.setState({
                color: res.color,
                posts: tmpArr
              });
            });
      });
    }

    render() {
      var tmp = [];
      for(var i = 0; i < this.state.posts.length; i++) {
        tmp.push(<div>{this.state.posts[i]}</div>);
      }
      return (
        <div>
          <h3 style={{ color: this.state.color }}>Sentiment color</h3>
          <div>{tmp}</div>
        </div>
      );
    }
}
