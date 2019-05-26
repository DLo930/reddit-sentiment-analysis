var elems = document.getElementsByClassName('Post');
for(var i = 0; i < elems.length; i++) {
  elems[i].style.backgroundColor = 'blue';
}

var elems2 = document.getElementsByClassName('Comment');
for(var i = 0; i < elems2.length; i++) {
  elems2[i].style.backgroundColor = 'red';
}

var form = new FormData();
form.append('text', 'Hello, world!');
form.append('api_key', 'tgXXTl26MVLbrMgcoIsy8hGKNafAMutI1NdyXR4A9sU');
form.append('lang_code', 'en');

fetch('https://apis.paralleldots.com/v4/emotion/', {
  method: 'POST',
  headers: {
    'Accept': 'application/json',
    'Content-Type': 'multipart/form-data'
  },
  body: form
})
  .then(body => {
    console.log(body);
  });
