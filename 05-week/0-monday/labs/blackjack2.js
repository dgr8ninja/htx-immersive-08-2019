
var suite = ['Hearts', 'Diamonds', 'Clubs', 'Spades'];
var value = [2,3,4,5,6,7,8,9,10,10,10,10,11,
    2,3,4,5,6,7,8,9,10,10,10,10,11,
    2,3,4,5,6,7,8,9,10,10,10,10,11,
    2,3,4,5,6,7,8,9,10,10,10,10,11];
var imgElement = document.createElement('img')
      imgElement.src = 'images/' + cards[i].cardNum + '_of_' + cards[i].cardSuit + '.png'
      imgElement.style.height = '120px'
      imgElement.style.width = '100px'

var playerHand;
var dealerHand;


var  dealerInput = document.getElementById('dealer-input')
var playerInput = document.getElementById("player-input")
var deal = document.getElementById('deal-button')

function startGame(){

    playerHand = [drawRandomCard(value), drawRandomCard(value)];
            playerHand.appendChild(imgElement)

    dealerHand = [drawRandomCard(value), drawRandomCard(value)];
            dealerHand.appendChild(imgElement)
    
    playerInput.append(playerHand);
    dealerInput.append(dealerHand);
}

var hit = document.getElementById('hit-button')

function hitMethod(){

    playerHand.push(drawRandomCard(values));
    if(getHandValue(playerHand) > 21){
        console.log('BUST ! ');
    }

var stand = document.getElementById('stand-button')
var reset = document.getElementById('reset-button')
// deal.addEventListener('click', startGame)
deal.addEventListener('click', hitMethod)
// deal.addEventListener('click', standmethod)
// deal.addEventListener('click', resetmethod)


function drawRandomCard(deck){
    console.log(deck.length)
   let randomIndex = Math.floor(Math.random() * deck.length);
   
        return deck[randomIndex];
}



function getHandValue(hand){
    var sum = 0;
    for (var i = 0; i < hand.length; i++){
        sum += hand[i];
    }
    return sum;

}

startGame();
console.log('Player Hand: ' + playerHand);
console.log('Player Hand Value: ' + getHandValue(playerHand));
console.log('Dealer Hand: ' + dealerHand);
console.log('Dealer Hand Value: ' + getHandValue(dealerHand));



}


















