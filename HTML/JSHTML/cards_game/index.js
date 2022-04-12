
var myScore = 0
var computerScore = 0

var cards = ["2.png", "3.png", "4.png", "5.png", "6.png", "7.png", "8.png",
  "9.png",
  "10.png", "J.png", "Q.png", "K.png", "A.png"]
// 13 cards. zero based so: 0-12

function draw() {
  var myCard = Math.floor(Math.random() * 13)    // gives a random number between 0-12 
  var computer = Math.floor(Math.random() * 13)  // gives a random  number between 0-12        

  $("#mycardimg").attr("src", cards[myCard])
  $("#computercardimg").attr("src", cards[computer])

  if (myCard > computer) {
    // i won this round
    //alert(`I won! ${cards[myCard]} ${cards[computer]}`)
    myScore++;
  }
  else if (myCard < computer) {
    // computer won this round
    //alert(`Computer won! ${cards[myCard]} ${cards[computer]}`)
    computerScore++;
  }

  $("#myscore").text(myScore)
  $("#compscore").text(computerScore)

}

