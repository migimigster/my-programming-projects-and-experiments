// let max = parseInt(prompt("Enter the maximum number"));
// while (!max){
//         max = parseInt(prompt("Enter valid maximum number"));
// }
// const targetNum = Math.floor(Math.random()*max) + 1;
// console.log(targetNum);

// let guess = prompt("Enter your first guess!");
// let guess_number=1;
// while (parseInt(guess)!==targetNum){
//     if (guess==='q'){
//           break;
//     }
//     if(guess>targetNum){
//         guess=parseInt(prompt("Too high.. Guess more "));
//     }else{
//         guess=parseInt(prompt("Too low.. Guess more "));
//     }
//     guess_number++;
// }
// if (guess==='q'){
//     console.log("wow what a quitter! hahaha");
// }else{
//     console.log("You got it!");
//     console.log(`Your total guess is ${guess_number}`);
// }



// WRITE YOUR LOOP BELOW THIS LINE:
const numbers = [1,2,3,4,5,6,7,8,9]; //DON'T CHANGE THIS LINE PLEASE!

// WRITE YOUR LOOP BELOW THIS LINE:

let list = [];

while (true) {
    x=prompt("What would you like to do?");
    if (x === 'new'){
        add = prompt("What would you like to add? ");
        list.push(add);
        console.log(`${add} added to the list\n`)
    }else if(x==='delete'){
        remove=parseInt(prompt("What index would you like to remove? "))
        list.splice(remove-1,1);
        console.log(`Number ${remove} has been removed to the list\n`) 
    }else if(x==='quit'){
        break;
    }else if(x==='list'){
        console.log("**********");
        for (let i=0; i<list.length; i++){
            console.log(`${i+1}: ${list[i]}`);
        }console.log("**********");
    }
}