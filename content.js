function getColor() {

}

var elems = document.getElementsByClassName('Post');
for(var i = 0; i < elems.length; i++) {
  elems[i].style.backgroundColor = 'blue';

}

var elems2 = document.getElementsByClassName('Comment');
for(var i = 0; i < elems2.length; i++) {
  elems2[i].style.backgroundColor = 'red';
}

fetch('https://apis.paralleldots.com/v4/emotion/', {
  method: 'POST',
  headers: {
    'Content-Type': 'multipart/form-data'
  },
  body: JSON.stringify({
    text: 'Hello, world!',
    api_key: 'tgXXTl26MVLbrMgcoIsy8hGKNafAMutI1NdyXR4A9sU',
    lang_code: 'en'
  })
})
  .then(res => {
    console.log(res.body);
  });
