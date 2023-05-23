# GUI_Python_Snakes_and_Ladders_Game
This is a Python implementation of the classic board game "Snakes and Ladders." The game is built using the Tkinter library for creating the graphical user interface (GUI). It allows two players to take turns rolling the dice and moving their game pieces on the board until one of them reaches the final square and wins the game.



Tkinter: The game uses Tkinter for GUI.
PIL (Python Imaging Library): PIL is used for loading and resizing images. 

Game Interface: Once you run the script, a graphical window will open, displaying the Snakes and Ladders game board. The GUI allows you to interact with the game.

Gameplay:

Player 1 starts the game. Click the "Player 1" button to roll the dice.
The dice image will change to a random number between 1 and 6, representing the dice roll result.
The game piece for Player 1 will move forward by the number rolled.
If Player 1 lands on the bottom of a ladder, they will automatically climb to the square at the top of the ladder.
If Player 1 lands on the head of a snake, they will move down to the square at the snake's tail.
After Player 1 completes their turn, click the "Player 2" button to roll the dice for Player 2.
The gameplay alternates between the two players until one of them reaches or exceeds square 100.
The game will display a message declaring the winner (Player 1 or Player 2) in a label on the screen.
To restart the game, close the window and run the script again.
Files and Resources
images/: This directory contains the image resources required for the game, including the game board image, dice images, and player coins.
images/snakesandladdersboard.png: The image of the Snakes and Ladders game board.
images/two_red_dice_roll.png: The image representing the dice roll button.
images/Dicey-1.png, images/Dicey-2.png, ..., images/Dicey-6.png: The images representing the faces of a standard six-sided die.

The code is structured as follows:

Libraries are imported at the beginning of the script, including tkinter for GUI and PIL for image manipulation.
Functions are defined for different aspects of the game:
start_game(): Sets up the initial game interface with buttons, images, and labels.
reset_coins(): Resets the positions of the player coins to the starting square.
load_dice_images(): Loads and resizes the dice images used for displaying the dice roll.
check_ladder(turn): Checks if the current player lands on a ladder and moves them to the corresponding square.
check_snake(turn): Checks if the current player lands on a snake and moves them to the corresponding square.
roll_dice(): Handles the dice rolling action, moves the player's game piece, and determines the next player's turn.
is_winner(): Checks if any player has reached or exceeded square 100 and displays a message declaring the winner.
move_coin(turn, r): Moves the player's game piece to the given square on the board.
get_index(): Calculates and stores the x and y coordinates of each square on the game board.
The main part of the code creates the game window, sets up the game board, initializes variables, and starts the Tkinter event loop.