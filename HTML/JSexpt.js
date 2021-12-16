let max = parseInt(prompt("Enter the maximum number"));
while (!max){
        max = parseInt(prompt("Enter valid maximum number"));
}
const targetNum = Math.floor(Math.random()*max) + 1;
console.log(targetNum);

let guess = prompt("Enter your first guess!");
let guess_number=1;
while (parseInt(guess)!==targetNum){
    if (guess==='q'){
          break;
    }
    if(guess>targetNum){
        guess=parseInt(prompt("Too high.. Guess more "));
    }else{
        guess=parseInt(prompt("Too low.. Guess more "));
    }
    guess_number++;
}
if (guess==='q'){
    console.log("wow what a quitter! hahaha");
}else{
    console.log("You got it!");
    console.log(`Your total guess is ${guess_number}`);
}