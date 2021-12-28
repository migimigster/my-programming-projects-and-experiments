const p1t = {
    score: 0,
    button: document.querySelector("#p1"),
    display: document.querySelector("#p1score")
}
const p2t = {
    score: 0,
    button: document.querySelector("#p2"),
    display: document.querySelector("#p2score")
}
const reset = document.querySelector("#reset");
const winningScoreSelect = document.querySelector("#playTo")
let winningScore = 3;
let gameOver = false;

function updateScore(player1,player2){
    if(!gameOver){
        player1.score+=1;
    }
    if (winningScore===player1.score){
        gameOver = true;
        player1.display.classList.add('has-text-success');
        player2.display.classList.add('has-text-danger');
        player1.button.disabled = true;
        player2.button.disabled = true;
    }
    player1.display.textContent = player1.score;
}


p1t.button.addEventListener("click", function (){
    updateScore(p1t,p2t)
})

p2t.button.addEventListener("click", function (){
    updateScore(p2t,p1t)
})

winningScoreSelect.addEventListener('change',function () {
    winningScore = parseInt(this.value);
    res();
})

reset.addEventListener("click", res)

function res(){
    gameOver = false;
    for (let p of [p1t,p2t]){
        p.score=0;
        p.display.textContent=0;
        p.display.classList.remove('has-text-success','has-text-danger');
        p.button.disabled = false;
    }
}