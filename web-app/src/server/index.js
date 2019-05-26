const express = require('express');
const pd = require("paralleldots");
// require("dotenv").configure();
const app = express();
const port = process.env.PORT || 3000;

app.use(express.json());
app.use(express.static('dist'));

pd.apiKey = 'tgXXTl26MVLbrMgcoIsy8hGKNafAMutI1NdyXR4A9sU';

app.post('/test', (req, res) => {
  res.end({ array: ["#FFFFFF"] });
});

// http://apis.paralleldots.com/text_docs/index.html#emotion
app.post("/getColors", (req, res) => {
  console.log("Hello, world!");
  pd.emotionBatch(JSON.stringify(req.body.textArray), 'en')
    .then((res) => {
      console.log(res);
      res.end(res);
    }).catch((err) => {
      console.log(err);
    });
});

app.listen(port, () => console.log(`Listening on port ${port}!`));
