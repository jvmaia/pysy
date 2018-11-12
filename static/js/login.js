function createCookie(name, value, days){
  var expires;
  if (days){
    var date = new Date();
    date.setTime(date.getTime()+(days*24*60*60*1000))
    expires = '; expires=' + date.toGMTString();
  }
  else{
    expires = '';
  }
  document.cookie = name +'='+ value + expires + '; path=/';
}

function login(){
  axios.post('/api/api-token-auth/', {
      username: document.getElementById('inputUser').value,
      password: document.getElementById('inputPassword').value
      })
    .then(function (response) {
      createCookie('token', response.data.token);
      location.reload();
    })
    .catch(function (error) {
      alert('Something was wrong!');
    });
}
