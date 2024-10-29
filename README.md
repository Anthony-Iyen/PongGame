# PongGame
Python Project simulates retro game pong
------------------------------------------

# Pong Game in Python 🎮

Welcome to **Pong**, a classic arcade game recreated in Python! This project simulates a two-player Pong game where you can choose to play against another player or an AI. The game uses `graphics.py` for rendering and runs in a 500x500 window.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Game Controls](#game-controls)
- [Classes and Methods](#classes-and-methods)
- [How to Play](#how-to-play)
- [Contributors](#contributors)

---

## Features
- **Single-player mode**: Play against a challenging AI opponent.
- **Two-player mode**: Play against a friend.
- **Realistic paddle and ball physics**: Including collision detection and scoring.
- **Scorekeeping**: Game automatically ends when a player reaches 3 points.
- **Customizable speed**: Adjustable paddle speed and ball randomness for difficulty settings.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/pong-game.git
---------------------------------------------------------

[Usage](#usage)
Navigate to the project directory:
  cd pong-game

Run the game:
  python pong.py
  
[Game Controls](#game-controls)
Player 1:
  Move Up: Up Arrow
  Move Down: Down Arrow
Player 2 (if two-player mode is selected):
  Move Up: W
  Move Down: S
  
[Classes and Methods](#classes-and-methods)
1. Paddle Class
  Controls paddle movement and provides methods for moving based on user input.
  Attributes: x1, y1, x2, y2, up_key, down_key
* Methods:
  move(key): Moves the paddle up or down based on the input key.

2. AI_Paddle Class
  Inherits from Paddle and automatically moves the paddle based on the ball's position.
* Methods:
    move(ball): Moves the AI paddle based on the ball's location.
  
3. BALL Class
  Handles ball movement, collisions, and scoring.
  Attributes: dx, dy, p1score, p2score, resetcheck
* Methods:
    ballmove(): Moves the ball and checks for wall collisions.
    contact(paddle): Checks for collisions between the ball and a paddle.
    GameEndcheck(): Ends the game when a player reaches a score of 3.
    getCenter(): Returns the center coordinates of the ball.
  
4. displayMenu()
  Displays a menu for selecting single-player or two-player mode.

5. mainloop()
  The main loop that initializes the game, controls, and runs the Pong game.

[How to Play](#how-to-play)
Run the game and select an option:
  Press 1 to play against AI.
  Press 2 to play against another player.
  Control your paddle using the designated keys to prevent the ball from passing your side.
  The first player to reach 3 points wins the game.
  
[Contributors](#contributors)
Nicholas Rackoff and Anthony Iyengunmwena - Main developer of the game.
Additional Contributors: Tom Finzell, John Zelle, Quox Nguyen, etc for the initial concepts and guidance.
Enjoy the game! 😄 If you encounter any issues or have ideas for improvement, feel free to submit an issue or a pull request.
