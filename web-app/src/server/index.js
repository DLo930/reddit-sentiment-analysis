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
  switch(obj.emotion) {
    case 'Anger': // red
    return `#${((k*255) | 0).toString(16)}0000`;
    case 'Fear': // orange
    return `#${((k*255) | 0).toString(16)}${((k*165) | 0).toString(16)}00`;
    case 'Joy': // yellow
    return `#${((k*255) | 0).toString(16)}${((k*255) | 0).toString(16)}00`;
    case 'Sadness': // blue
    return `#0000${((k*255) | 0).toString(16)}`;
    case 'Analytical': // magenta
    return `#${((k*255) | 0).toString(16)}00${((k*255) | 0).toString(16)}`;
    case 'Confident': // lime
    return `#00${((k*255) | 0).toString(16)}00`;
    default: // white
    return `#${((k*255) | 0).toString(16)}${((k*255) | 0).toString(16)}${((k*255) | 0).toString(16)}`;
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
        color: "#d3d3d3"
      });
    }
    var intensity = 0;
    var strongestEmotion = "";
    for(var i = 0; i < arr.length; i++) {
      if(arr[i].score > intensity) {
        intensity = arr[i].score;
        strongestEmotion = arr[i].tone_name;
      }
    }
    const toneColor = getColor({
      k: intensity,
      emotion: strongestEmotion
    });
    //console.log(toneColor);
    res.send({
      resColor: toneColor
    });
  });
});

app.listen(port, () => console.log(`Listening on port ${port}!`));
