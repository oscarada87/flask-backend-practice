let inputNumberArray = [];
let globalInputCounter = 0;

const getRandomNumber = () =>{
  let maxNum = 9;
  let minNum = 0;
  let n = Math.floor(Math.random() * (maxNum - minNum + 1));
  return n ;
}

const checkRepeat = (arr, n) =>{
  for(let i = 0; i < n; i++){
    if(arr[n] === arr[i]){
      return true;
    }
  }
  return false;
}
//Becareful array count from 0

const random4Numbers = () =>{
  let arr = [0, 0, 0, 0];
  let counter = 0;
  arr[counter] = getRandomNumber();
  counter++;
  while(counter < 4){
    arr[counter] = getRandomNumber();
    while(checkRepeat(arr, counter)){
      arr[counter] = getRandomNumber();
    }
    counter++;
  }
  return arr;
}
//自訂答案
let answer = [9, 4, 8, 7]
//let answer = random4Numbers();
console.log("答案 = " + answer); //答案
console.log("其實下個英文單字是 friend")
//console.log(random4Numbers());  //use for debug

/*let tempInput = document.getElementsByClassName('inputNumberBtn');
let inputNumberButton = [tempInput[9]];
for(let i = 0; i <= 8; i++){
  inputNumberButton.push(tempInput[i]);
}*/

const checkAnswer = () =>{
  if(inputNumberArray.length != 4){
    window.alert("沒有4位數，母湯喔!");
    return false;
  }
  let hint = [];
  let A = 0;
  let B = 0;
  for(let i = 0; i <= 3; i++){
    for(let j = 0; j <= 3; j++){
      if(inputNumberArray[i] == answer[j]){
        if(i == j){
          A++;
        }
        else{
          B++;
        }
      }
    }
  }
  hint.push(A);
  hint.push(B);
  //console.log("hint = " + hint);
  if(A == 4){
    window.alert("恭喜你! 9487 就是 key!");
    clearHistory();
    return false;
  }
  return hint;
}

//Input Output
const storeInput = (number) =>{
  if(globalInputCounter >= 4){
    return false;
  }
  inputNumberArray.push(number);
  display();
  globalInputCounter++;
}

const deleteInput = () =>{
  if(globalInputCounter >= 1){
    inputNumberArray.pop();
    globalInputCounter--;
    display();
  }
}

const clearInput = () =>{
  let length = inputNumberArray.length;
  for(let i = 0; i <= (length - 1); i++){
    inputNumberArray.pop();
    globalInputCounter--;
    display();
  }
  //console.log("global counter = " + globalInputCounter);
}

const display = () =>{
  let displayName = ('display'+ globalInputCounter);
  let displayTarget = document.getElementById(displayName);
  if(inputNumberArray[globalInputCounter] != null){
    displayTarget.innerHTML = inputNumberArray[globalInputCounter];
  }
  else{
    displayTarget.innerHTML = "-";
  }
}

const createNewHistoryElement = (t) =>{
  let text = document.createTextNode(t);
  let li = document.createElement('li');
  li.appendChild(text);
  return li;
}

const historyDisplay = () =>{
  let hint = checkAnswer();
  if(hint != false){
    let inputHistory = inputNumberArray[0].toString() +  inputNumberArray[1].toString()   + inputNumberArray[2].toString() + inputNumberArray[3].toString();
    let numberHistory = document.getElementById('numberHistory');
    numberHistory.appendChild(createNewHistoryElement(inputHistory));

    let hintHistory = hint[0] + "A" + hint[1] + "B";
    let hintList = document.getElementById('hintList');
    hintList.appendChild(createNewHistoryElement(hintHistory));

    clearInput();
  }
}

const clearHistory = () =>{
  let target = document.querySelectorAll('li');
  let numberHistory = document.getElementById('numberHistory');
  let hintList = document.getElementById('hintList');
  let length = target.length;
  //console.log(target);
  for(let i = 0; i < (length/2); i++){
    numberHistory.removeChild(target[i]);
  }
  for(let i = (length-1); i >= (length/2); i--){
    hintList.removeChild(target[i]);
  }
  clearInput();
  //restart
  //answer = random4Numbers();
  //console.log("answer = " + answer);
}

let inputBox = document.querySelector('.numberInputColumn');
inputBox.addEventListener('click', (e) => {
  let target = e.target;
  if (target.type === 'button') {
    storeInput(target.innerHTML);
    //console.log(inputNumberArray);
  }
});

let submitBox = document.querySelector('.submit');
submitBox.addEventListener('click', (e) =>{
  let target = e.target;
  if (target.type === 'button'){
    if (target.innerHTML === '清除'){
      deleteInput();
      //console.log(inputNumberArray);
    }
    else if(target.innerHTML === '送出'){
      //console.log("input = " + inputNumberArray);
      historyDisplay();
    }
  }
});
