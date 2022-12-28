# CONSOLE CARD GAME OF WAR

A sample card game of war

- [https://repl.it/repls/UglySphericalDigits](https://repl.it/repls/UglySphericalDigits)
- [https://repl.it/repls/MerryWhirlwindFreesoftware](https://repl.it/repls/MerryWhirlwindFreesoftware)

### DEPENDENCIES

- names [https://pypi.org/project/names/](https://pypi.org/project/names/)

### INFORMATION

#### *War Game*
War is a card game designed for two players, 
utilizing a standard (French style) 52-card deck of playing-cards. 
The objective is to "capture" all the cards in the game before your opponent.
#### *Gameplay*
All cards are shuffled, and then divided equally to each player in face down stacks (one stack for each player). Each player reveals the top card of their deck simultaneously, with the player revealing the highest-ranking card winning that particular round and thusly "capturing" their opponent's card (in addition to retaining their card). Both cards are then returned to the round-winner's deck, placed face down at the bottom. Gameplay continues in the above fashion, with players playing out consecutive rounds, until one player runs out of cards and loses.
#### *Rankings*
Cards are ranked by face value, with Ace, King, Queen, and Jack each (in order) taking the highest ranking, followed by number cards in numerical order (10 being worth more than a 9, etc.). Output must show face value and suite of the card.
#### *Ties*
In the event of a tie in a round - two players playing the same ranked cards - both cards are left face up between the two players, and play proceeds to the next round. The winner of the next round takes all cards from the current as well as previous round.
#### *Challenge*
Your challenge is to write an application to simulate a game of War. Play out a game in full, and output the winner. Additionally, outputting the results of each round, including the card that each player played as well as the verdict of which player won. If no winner exists after 100 rounds, the game ends with a prompt to play chess instead.
