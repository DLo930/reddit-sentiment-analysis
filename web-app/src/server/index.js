const express = require('express');
const fetch = require('node-fetch');

const app = express();
const port = process.env.PORT || 3000;

const TAv3 = require('watson-developer-cloud/tone-analyzer/v3');
const toneAnalyzer = new TAv3({
  version: '2017-09-21',
  iam_apikey: 'gpMRI7IdtqIsUhH6voCUBMbxYGDBMZCql08GxbBap6x2',
  url: 'https://gateway-wdc.watsonplatform.net/tone-analyzer/api/'
});

app.use(express.json());
app.use(express.static('dist'));

// http://apis.paralleldots.com/text_docs/index.html#emotion
app.post("/getColors", (req, res) => {
  const params = {
    "tone_input": { "text": req.body.text },
    "content_type": 'text/plain',
  };

  toneAnalyzer.tone(params)
    .then(toneAnalysis => {
      if(toneAnalysis.document_tone.tones.length == 0) {
        res.send({
          "tone": "Neutral",
          "score": 0
        });
      }
      res.send({
        "tone": toneAnalysis.document_tone.tones[0].tone_name,
        "score": toneAnalysis.document_tone.tones[0].score
      });
    })
      .catch(err => {
        console.log(err);
      });
});

app.listen(port, () => console.log(`Listening on port ${port}!`));
