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
          (async () => {
          const rawResp = await fetch('/getColors', {
            method: 'POST',
            headers: {
              "Accept": "application/json",
              "Content-Type": "application/json"
            },
            body: JSON.stringify({
              text: str
            })
          });
          const content = await rawResp.json();
          this.setState({
                color: content.resColor,
                posts: tmpArr
              });
            })();
      });
    }

    render() {
      var tmp = [];
      for(var i = 0; i < this.state.posts.length; i++) {
        tmp.push(this.state.posts[i]);
      }
      const liArr = []
      for (const [index, value] of tmp.entries()) {
         liArr.push(<li key={index}>{value}</li>)
       }
      return (
        <div>
        <p class="verdanaStyle">Sentiment Color: <strong>{document.body.style.background = this.state.color}</strong></p>
        <u><p class="verdanaStyle">Analyzed Submission Titles of <strong>r/{this.state.theSub}</strong>:</p></u>
          <div class="elemLst">{liArr}</div>
        </div>
      );
    }
}
