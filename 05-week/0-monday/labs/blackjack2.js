var deal = document.getElementById('deal-button')
var hit = document.getElementById('hit-button')
var stand = document.getElementById('stand-button')
var reset = document.getElementById('reset-button')
deal.addEventListener('click', playGame)
deal.addEventListener('click', hitmethod)
deal.addEventListener('click', standmethod)
deal.addEventListener('click', resetmethod)

var deck = [2,3,4,5,67,8,9,10,10,10,10,11,
            2,3,4,5,67,8,9,10,10,10,10,11,
            2,3,4,5,67,8,9,10,10,10,10,11,
            2,3,4,5,67,8,9,10,10,10,10,11];

function drawRandomCard(deck){

   var randomIndex = Math.floor((deck.length + Math.random()))
        return deck[randomIndex]
}

var playerHand;
var dealerHand;

function startGame(){

    playerHand = [drawRandomCard(deck), drawRandomCard(deck)];
    dealerHand = [drawRandomCard(deck), drawRandomCard(deck)];

}

startGame();
console.log('Player Hand: ' + playerHand);
console.log('Dealer Hand: ' + dealerHand);