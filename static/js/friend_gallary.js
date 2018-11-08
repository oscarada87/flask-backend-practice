$(function() {
  $(".box").on("mousedown", function(e) {
    const gate = $(this).children("div");
    $(this).children(".locker").hide();
    for (var i = 0; i < gate.length; i++) {
      if ($(gate[i]).hasClass("ovrl-left")) {
        $(gate[i]).toggleClass("move-right");
      }
      if ($(gate[i]).hasClass("ovrl-right")) {
        $(gate[i]).toggleClass("move-left");
      }
    }
    // removes the click event after reveling the image
    $(this).off();
  });
});

function hint(){
  var msg = "請把所有照片中出現的人的生日的月份和日期相加就是這頁的 key";
  alert(msg);
}

var title = document.getElementById("hint");
title.addEventListener("click", hint, false);