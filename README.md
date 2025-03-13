# PYTHON BLACKJACK
#### Video Demo:  <https://youtu.be/nFIbq-CcwSw>
#### Description:
Classic game of Blackjack, basic game play, get 21!
Closest to 21 wins, over 21 loses immediately.
As long as you haven't reach 21 you have the opportunity to draw as many cards as you want.
If you draw an ACE(11) and you go over 21, the value of the ACE will turn from 11 to 1.
Once you finish drawing cards it's time for the house to play, they will always try to beat your score.
Good luck!

### First things first
I needed to create the deck and initialize both players, user and computer.
The ACE will start with a value of 11 in the deck and change later in the game if the current hand goes over 21. At first I though I had to give both players the 2 cards and hide one of the cards for the computer but soon I saw that it was better to just initialize the computer with 1 card and later finish the computer's hand after the user had stopped drawing cards.

### Creating the functions
Initially I tried to create the functions in a different file, but then it proved too complicated for me to handle and decided to do it in the same file, as I had learned, creating a main function to go first and then all the other functions bellow it, for a more organized look.

At the end, the duck bot advised me that I could create even more functions to make the main function even simpler but ended up leaving it as is, because It meant writing even more code and it felt the improvement of the main function wasn't enough for it too be worth it, if something I think it would make the main function less readable.

I left the questions inside main and the while not winner loop. Also, the program will ask the user if they want to play again and again until the answer is yes.

#### main():
Asks the user if they want to play Blackjack.
Calls initialize_game() and cards_and_scores().

#### initialize_game():
Initializes the user's and computer's starting cards by calling draw() twice for user and once for computer.

#### draw():
Draws a random card from the cards list.
Checks for Aces (adjusting 11 to 1 if necessary) using check_ace().

#### check_ace():
Ensures that if the score exceeds 21, an Ace (11) is adjusted to a 1 to keep the score valid.

#### cards_and_scores():
Displays the user's and computer's current cards and scores.

#### winner_by_21():
Checks if either player has hit 21. If so, calls computer_finish(), blackjack(), finally printing the appropriate winning message.

#### computer_finish():
Makes the computer draw cards until it surpasses the user's cards, either winning or going over 21.

#### blackjack():
Checks for the special "Blackjack" condition (combination of 10 and 11) and declares the winner accordingly.

#### continue_game():
If user chooses 'y'. Calls draw() for the user to get another card.
Displays scores and checks for a winner with winner_by_21() or over_21().

#### over_21():
Checks if either player’s score exceeds 21 and declares the winner.

#### finish_game():
If user chooses 'n'. Calls computer_finish() to finalize the computer's cards.
Displays cards and scores using cards_and_scores().
Determines the winner using winner_by_21(), over_21(), or winner_by_remainder().

#### winner_by_remainder():
Decides the winner based on which player’s score is closer to 21.

#### final_hand():
Prints the final cards and scores of both the user and the computer.

### The files
Ultimately, because I decided to define all the functions in the same file, I ended up with just 2 files, app.py for the game and just an additional file for the art. Just to make it cleaner.

### The design
I really like that old school look. I had though to either make a game like blackjack or a story-based game. I decided over blackjack because I wanted a challenge that involved logic and problem solving, instead of writing a complex story. Although that also sounds fun and I'll probably work on something like that at some point. At this time, working on a game like blackjack felt more difficult and motivating for me. I also had decided I wanted to focus on learning python, so that's the language I decided to use for this project.

### The process
I decided to work on this with minimum help from the duck or any hints, specially in regards to the pseudocode. Because of this it ended up taking me twice as much time as I had initially estimated. Half way through I did need help from the bot, mostly for the winner_by_21 function, which took a long while to work as I wanted it. I wanted it to differentiate between just winning with 21 or winning with blackjack, so I had to create another function called blackjack to call inside the winner_by_21 function to be able to display the correct winner message.

Another thing I wanted out of the game was that the house was always trying to win, even if that meant possibly going over, choosing to draw and draw as long as the score is less than the one from the user. Defining this function brought me a lot of challenges, I went through different versions, trials and errors and the help of the debugger, which was trying to understand what I wanted out of the function in the first place. Finally, I settled with this line of code in the function computer_finish:

    elif computer_score < 21:
        while computer_score < user_score or computer_score < 12:


I learned to use the issubset to find if the winner had won with blackjack, I also learned that math can be quite simple sometimes, in the function winner_by_remainder, which finds who wins by being closest to 21, I used crazy math to figure that out, the duck made it so simple it was quite embarrassing.

Other functions where more simple for me to define and make work as I wanted, in the moment I felt the code was pretty readable and self explanatory.

Finally, after the game worked as I wanted, I looked for the code for this game in python, to my surprise, although, honestly, I should've known, their code was so simple I felt devastated. It took me a while to understand I am just starting this journey and will get better over time.

All things considered I learned a lot and I did it mostly using what I already knew about coding. I had fun with every challenge and after the initial embarrassment passed, I felt very proud of this project and will be continuing my studies of python.
