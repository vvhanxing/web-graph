console.log("V1.0");
let info ={
  Fake:["你好","请看左边图示"]
}
  


var Fake = {
  Fake:["你好"]
}



function getJson(inputTxt){



//var url = "./static/datasets/index.json"
var url = "http://192.168.31.67:5000/neo"

var request = new XMLHttpRequest();

request.open("POST", url,true);
request.setRequestHeader("Content-Type", "application/json");


request.onload = function (e) {
  if (request.readyState === 4) {
    if (request.status === 200) {
    txt =  request.responseText
    
    info = {
      Fake:[txt,txt]
    }
    console.log("************");
    console.log(info);
    fakeMessage();
    
    } else {
    console.error(request.statusText);
    }
    }
  };
  request.send(JSON.stringify({"inputTxt":[inputTxt]})); 
  //console.log("--------<<<<");
  //console.log(inputTxt );

    return inputTxt;

}


var $messages = $('.messages-content'),
    d, h, m,
    i = 0;

$(window).load(function() {
  $messages.mCustomScrollbar();
  setTimeout(function() {
    fakeMessage();
  }, 100);
});


function updateScrollbar() {
  $messages.mCustomScrollbar("update").mCustomScrollbar('scrollTo', 'bottom', {
    scrollInertia: 10,
    timeout: 0
  });
}

function setDate(){
  d = new Date()
  if (m != d.getMinutes()) {
    m = d.getMinutes();
    $('<div class="timestamp">' + d.getHours() + ':' + m + '</div>').appendTo($('.message:last'));
    $('<div class="checkmark-sent-delivered">&check;</div>').appendTo($('.message:last'));
    $('<div class="checkmark-read">&check;</div>').appendTo($('.message:last'));
  }
}

function insertMessage() {
  msg = $('.message-input').val();
  if ($.trim(msg) == '') {
    return false;
  }
  $('<div class="message message-personal">' + msg + '</div>').appendTo($('.mCSB_container')).addClass('new');
  setDate();
  //$('.message-input').val(null);
  updateScrollbar();
  setTimeout(function() {
    console.log("########");
    console.log(msg);
    getJson(msg);
    
  }, 1 + (Math.random() * 20) * 100);

}

$('.message-submit').click(function() {
 
    insertMessage();
});

$(window).on('keydown', function(e) {
  if (e.which == 13) {
  
    insertMessage();
    return false;
  }
})







function fakeMessage() {

  if ($('.message-input').val() != '') {
    return false;
  }
  $('<div class="message loading new"><figure class="avatar"><img src="./static/chat/17.jpg" /></figure><span></span></div>').appendTo($('.mCSB_container'));
  updateScrollbar();

  setTimeout(function() {
    $('.message.loading').remove();
    var i = 0;
    if (info.Fake== undefined){

      
      info.Fake = ["你好呀"];
      
    }

    //console.log(i);


    console.log("@@@@@@@@@@@@@@@@@@@@@@@@");
    console.log(info.Fake[0]);

    //console.log( JSON.parse( info.Fake[0]).Fake[0]);
    $('<div class="message new"><figure class="avatar"><img src="./static/chat/17.jpg" /></figure>' + info.Fake[0] + '</div>').appendTo($('.mCSB_container')).addClass('new');
    setDate();
    updateScrollbar();
    //i++;
  }, 1 + (Math.random() * 20) * 100);

}

$('.button').click(function(){
  $('.menu .items span').toggleClass('active');
   $('.menu .button').toggleClass('active');
});
