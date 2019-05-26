import React from "react"

var snoowrap = require('snoowrap');


export default class UserSubmiss extends React.Component {
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


      r.getUser('Spez').getSubmissions().map(post => post.title).then(console.log);


          //end didmount
       console.log("exit did mount");
     }


    render() {
        return (
          <div>
            <p> IM IN usersubmissions!</p>
          </div>
        )
    }
}
