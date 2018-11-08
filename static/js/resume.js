function hint(){
    var msg = "隨便點點看!! 有提示!!" ;
    alert(msg);
}

function hint2(){
    var msg = "你還記得我之前教你爬蟲，開啟要爬蟲的網頁之後要先按甚麼嗎?";
    alert(msg);
}

function hint3(){
    var msg = "好吧! 既然你都找到這個了，我就大發慈悲跟你說吧!";
    alert(msg);
    msg = "按下F12進入開發者模式，然後找到 console 看看有甚麼!";
    alert(msg);
}

hint();
var cat = document.getElementById("cat");
cat.addEventListener("click", hint2)

var code = document.getElementById("code");
code.addEventListener("click", hint3)
console.log("回去剛剛的game再看看同樣這個地方!!")