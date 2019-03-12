$("#signup_form").submit(function(e){
  var data = $(this).serialize();
  $.ajax({
    url: '/auth/signup/',
    type: 'POST',
    data: data,
    success: (res) =>{
      if(res.error){
        var errors = create_response_object(JSON.parse(res.data));
        alert(errors);
      }
      else{
        alert(res.data);
      }
      document.location.reload(true);
    },
    error: (res) =>{
      alert('Ошибка подключения к серверу');
      document.location.reload(true);
    }
  });

  e.preventDefault();
});

$("#login_form").submit(function(e){
  var data = $(this).serialize();
  $.ajax({
    url: '/auth/signin/',
    type: 'POST',
    data: data,
    success: (res) =>{
      alert(res.data);
      document.location.reload();
    },
    error: (res) =>{
      alert('Ошибка подключения к серверу');
      document.location.reload(true);
    }
  });

  e.preventDefault();
});

$("#upload_skin").submit(function(e){
  var formData = new FormData(this);
  formData.append('csrfmiddlewaretoken', getCookie('csrftoken'));
  console.log("QWEQWE");
  $.ajax({
    url: '/auth/uploadskin/',
    type: 'POST',
    processData: false,
    contentType: false,
    async: true,
    cache: false,
    enctype: 'multipart/form-data',
    data: formData,
    enctype: 'multipart/form-data',
    success: (res) =>{
      if(res.error){
        alert(create_response_object(JSON.parse(res.data)));
      }
      else{
        alert(res.data);
      }
      document.location.reload(true);
    },
    error: (res) =>{
      alert('Ошибка подключения к серверу');
      document.location.reload(true);
    }
  });

  e.preventDefault();
});

$("#upload_cloak").submit(function(e){
  var formData = new FormData(this);
  formData.append('csrfmiddlewaretoken', getCookie('csrftoken'));
  console.log("QWEQWE");
  $.ajax({
    url: '/auth/uploadcloak/',
    type: 'POST',
    processData: false,
    contentType: false,
    async: true,
    cache: false,
    enctype: 'multipart/form-data',
    data: formData,
    enctype: 'multipart/form-data',
    success: (res) =>{
      if(res.error){
        alert(create_response_object(JSON.parse(res.data)));
      }
      else{
        alert(res.data);
      }
      document.location.reload(true);
    },
    error: (res) =>{
      alert('Ошибка подключения к серверу');
      document.location.reload(true);
    }
  });

  e.preventDefault();
});

$("#console").submit(function(e){
  var data = $(this).serialize();
  $.ajax({
    url: '/query/',
    type: 'POST',
    data: data,
    success: (res) =>{
      alert(res);
      document.location.reload(true);
    },
    error: (res) =>{
      alert('Ошибка подключения к серверу');
      document.location.reload(true);
    }
  });

  e.preventDefault();
});

function create_response_object(errors){
  var response_string = "";
  console.log(errors);
  for(var k in errors){
    response_string += k + ': ';
    var error_array = errors[k];
    for(var i=0; i<error_array.length; i++){
      response_string += error_array[i].message;
    }
    response_string += '\n';
  }
  return response_string;
}

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
