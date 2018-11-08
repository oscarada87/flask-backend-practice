function hint(){
    var msg = "隨便點點看!! 有提示!!" ;
    alert(msg);
}

window.onload(hint)

function hint2(){
    var msg = "你還記得我之前教你爬蟲，開啟要爬蟲的網頁之後要先按甚麼嗎?"
    alert(msg);
}

var cat = document.getElementById("cat");
cat.addEventListener("click", hint2)

console.log("回去剛剛的game再看看同樣這個地方!!")