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

function getColor(obj) {
  const k = obj.k;
  console.log(k+" "+obj.strongestEmotion);
  switch(obj.strongestEmotion) {
    case 'Anger':
      return `#${((k*255) | 0).toString(16)}0000`;
    case 'Fear':
      return `#${((k*255) | 0).toString(16)}${((k*140) | 0).toString(16)}00`;
    case 'Joy':
      return `#${((k*255) | 0).toString(16)}${((k*255) | 0).toString(16)}00`;
    case 'Sadness':
      return `#${((k*148) | 0).toString(16)}00${((k*211) | 0).toString(16)}`;
    case 'Analytical':
      return `#${((k*51) | 0).toString(16)}00${((k*153) | 0).toString(16)}`;
    case 'Confident':
      return `#0000${((k*255) | 0).toString(16)}`;
    default:
      return `#00${((k*255) | 0).toString(16)}00`;
  }
}

// http://apis.paralleldots.com/text_docs/index.html#emotion
app.post("/getColors", (req, res) => {
  const params = {
    "tone_input": { "text": req.body.text },
    "content_type": 'text/plain',
  };

  toneAnalyzer.tone(params)
    .then(toneAnalysis => {
      const arr = toneAnalysis.document_tone.tones;
      if(arr.length == 0) {
        res.send({
          "color": "#000000"
        });
      }
      var intensity = 0;
      var strongestEmotion = "";
      for(var i = 0; i < arr.length; i++) {
        if(arr[i].score > intensity) {
          intensity = arr[i].score;
          console.log(arr[i].tone_name);
          strongestEmotion = arr[i].tone_name;  //not being updated :(
        }
      }
      const color = getColor({
        k: intensity,
        emotion: strongestEmotion
      });
      res.send({
        "color": color
      });
    });
});

app.listen(port, () => console.log(`Listening on port ${port}!`));
