import React from "react"

var snoowrap = require('snoowrap');


export default class UserComs extends React.Component {
     constructor(props) {
          super(props)
          this.state = {
            theUser: props.theUser,
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


      r.getUser(this.state.theUser).getComments().map(post => post.body).then(console.log);
     }


    render() {
        return (
          <div>
            <p> IM IN usercoms!</p>
          </div>
        )
    }
}
