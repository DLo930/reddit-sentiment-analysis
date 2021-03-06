# [Reddit Sentiment Analysis](https://reddit-sentiment-analysis.herokuapp.com/)
## [CodeDay Pittsburgh May 2019](https://www.codeday.org/pittsburgh) - 1st place
The chrome extension and web app allow the user to quickly gain insights on the overall sentiment of subreddit posts through colors. By using IBM's [Tone Analyzer API](https://cloud.ibm.com/apidocs/tone-analyzer), the provided text is processed for emotion and intensity thereof. Reddit's [API](https://www.reddit.com/dev/api/) was used to extract posts for sentiment analysis. We utilized React, Express.js, and Node.js to implement our core functionality.

![alt text](https://github.com/DLo930/reddit-sentiment-analysis/blob/master/images/homepage.png?raw=true)

To run the web application locally, make sure you have Node installed (https://nodejs.org/en/).

After cloning the respository, run:
```
$ cd web-app
$ npm i
$ yarn start
```
Navigate to ```localhost:3000``` or the specified port.

---

To use the chrome extension, go to "chrome://extensions/" in your address bar. 

Turn on developer mode on the top right corner and click on "Load unpacked" in the top left corner. Load the reddit-sentiment-analysis folder from where you have cloned the file. The "Reddit Sentiment Analysis" chrome extension should appear and can be toggled on. 

Navigate to anywhere on https://www.reddit.com/ or https://old.reddit.com/.

Enjoy!
