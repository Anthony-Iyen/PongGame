# #Anthony Iyengunmwena and Nicholas Rackoff
# # Intro to CS Final Project
# #Pong Game

from graphics import *
import time
import random


WIDTH = 500
HEIGHT = 500
win = GraphWin("Pong",WIDTH, HEIGHT)
win.setBackground("Black")

class Paddle:
    ''' Class paddle serves the controls and movement for the paddle sin the pong game
    Returns the X and Y location of the paddle'''

    def __init__(self, x1, y1, x2, y2, up_key,down_key):
        self.player = Rectangle(Point(x1, y1), Point(x2, y2)) #creates a rectangle object representing player 1  
        self.player2=Rectangle(Point(x1, y1), Point(x2, y2)) #creates a rectangle object representing player 2
        self.player.setFill("white")
        self.player.draw(win)
        self.up_key = up_key
        self.down_key = down_key
       
    def move(self, key):
        """Move the paddle based on the pressed key."""

        # Get the rectangle object representing the paddle
        player = self.player

        # Get the coordinates of the top-left corner of the paddle
        B = player.getP1()
        # Get the y-coordinate of the top-left corner of the paddle
        C = B.getY()
        
        # Check if the paddle's top edge is above the window boundary
        if C > 0:
            if key == self.up_key:
                player.move(0, -10) # checks key and move paddle up

        # Get the coordinates of the bottom-right corner of the paddle
        B = player.getP2()
        C = B.getY() # Get the y-coordinate of the bottom-right corner of the paddle
        
        # Check if the paddle's bottom edge is above the window boundary
        if C < 500:
            if key == self.down_key:
                player.move(0, 10) # checks key and move paddle down

class AI_Paddle(Paddle):
    '''class AI_Paddle inherits from Paddle and implements AI-controlled paddle movement.'''

    def __init__(self, x1, y1, x2, y2, up_key, down_key):
        super().__init__(x1, y1, x2, y2, up_key, down_key)  # Inherits from Paddle

    def move(self, ball):
        '''Move the paddle based on the ball's position, Moves when its on the Ai side(half of the screen)'''

        # retrieve and store the center coordinates of the ball (ball_center) as ball_y and ball_x
        # paddle_center_y is the y-coordinate of the center of the paddle
        ball_center = ball.getCenter()
        ball_y = ball_center.getY()
        ball_x = ball_center.getX()
        paddle_center_y = self.player.getCenter().getY()
        
        # Find the difference between ball's Y and paddle's center Y
        # random.randrange makes the AI make "dumber choices"
        trackrange = ball_y - paddle_center_y +random.randrange(-5,5)


        # Move towards the ball 
        speed = random.uniform(-3,5)  

        #Only moves if the ball is on it's side, to reduce lag.
        if ball_x > 250: 
            if trackrange > 20:
               self.player.move(0, speed)
            elif trackrange < -20:
               self.player.move(0, -speed)
        else:
            # Move randomly to the opposite side
            if random.random() < 0.2:  # Adjust the probability as needed
                # Randomly choose the direction to move
                direction = random.choice([-1, 1])  # -1 for up, 1 for down
                self.player.move(0, direction * speed)
               
        # Prevent paddle from going out of bounds
        if self.player.getP1().getY() <= 0:
            self.player.move(0, 10)
        elif self.player.getP2().getY() >= HEIGHT:
            self.player.move(0, -10)


class PlayerTwoPaddle(Paddle):
    '''class PlayerTwoPaddle inherits from Paddle and implements player controlled paddle movement.'''

    def __init__(self, x1, y1, x2, y2, up_key, down_key):
        super().__init__(x1, y1, x2, y2, up_key, down_key) # Inherits from Paddle
        
    
class BALL:
    '''Class representing the ball object in the Pong game. Gives Location of the ball.
    Also where our collision and bouncings of the ball is stored.'''

    def __init__(self):
        # drawing and setting the point the ball starts.
        self.center = Point(250,250)
        self.ball = Circle((self.center), 20)
        self.ball.setFill("white")
        self.ball.draw(win)

        #  initial movement of the ball
        self.dx = -3
        self.dy = 0

        # starting score between player 1 and AI
        self.p1score = 0
        self.p2score = 0

        #when true ball resets back to orginial postions
        self.resetcheck = False

        # Middle width of the game
        win_width= win.getWidth()
        self.middlex= win_width/2

        # Middle height of the game
        win_height= win.getHeight()
        self.middley= win_height/2

        # Display of score for player 1
        self.score1 = Text(Point(100, 75),self.p2score)
        self.score1.setFill("white")
        self.score1.draw(win)

        # Display of Player 2(AI) score
        self.score2 = Text(Point(400, 75),self.p1score)
        self.score2.setFill("white")
        self.score2.draw(win) 

       
    def ballmove(self):
        '''moves the ball, checks for collisions with walls, updates the scores,
      and resets the ball if it goes out of bounds.'''


        #Starts ball movement
        self.ball.move(self.dx,self.dy)
        self.resetcheck = False
        
        #  Check if the ball goes out of bound of the window (left side).
        if self.ball.getP1().getX() <= 0:

            # Removes the ball and creates a new one
            self.ball.undraw()
            self.ball = Circle((self.center), 20)
            self.ball.setFill("white")


            # sets the movement of the new ball and adds a point to player 2(Ai)
            self.dx = 3
            self.dy = 0
            self.p2score += 1
            
            # Removes the old display for the point and updates it           
            self.score2.undraw()
            self.score2 = Text(Point(400, 75),self.p2score)
            self.score2.setFill("white")
            self.score2.draw(win)

            # draws the new ball and delays the movement for 5 seconds for the player to get ready for the next round         
            self.ball.draw(win)  
            time.sleep(5)
            self.resetcheck = True
        
        # Check if the ball goes out of the bound of the window (right side).
        elif self.ball.getP2().getX()>= win.getWidth():
            
            #if ball goes about to of bound set the movement of the new ball and add a point to player 1
            self.ball.undraw()
            self.ball = Circle((self.center), 20)
            self.ball.setFill("white")
            self.dx = -3
            self.dy = 0
            self.p1score += 1
            
            # Removes the old display for the point and updates it
            self.score1.undraw()
            self.score1 = Text(Point(100, 75),self.p1score)
            self.score1.setFill("white")
            self.score1.draw(win)

            # draws the new ball and delays the movement for 5 seconds for the player to get ready for the next round
            self.ball.draw(win)
            time.sleep(5)
            self.resetcheck = True
        
         # Check for ball contact with height(top and bottom walls), if in contact send in the opposite dirrection
        if self.ball.getP1().getY()<= 0:
            self.dy=-self.dy
        elif self.ball.getP2().getY()>= win.getHeight():
            self.dy=-self.dy


    def contact(self, paddle):
        '''Check for collision between the ball and the paddle.'''

        # Check for ball contact with height(top and bottom walls), if in contact send in the opposite dirrection
        ball_center = self.ball.getCenter()
        ball_radius=self.ball.getRadius()
        ballX = ball_center.getX()+ball_radius
        ballY = ball_center.getY()+ball_radius

        # Calculate the coordinates of the paddle (paddle is a rectangle made up of two seperare points that each have an (x,y)
        paddle_point1X = paddle.player.getP1().getX()
        paddle_point2X = paddle.player.getP2().getX()+ball_radius*2
        paddle_point1Y = paddle.player.getP1().getY()
        paddle_point2Y = paddle.player.getP2().getY()+ball_radius*2

        if self.dx > 0:
            # Ball is moving to the right
            # Conditions for contact when Ball is moving from the right
            if (paddle_point1X <= ballX <= paddle_point2X) and (paddle_point1Y <= ballY <= paddle_point2Y):
                # Ball collides with the paddle
                self.dx = -self.dx
                self.dy += random.uniform(-2, 2)    # Ball collides with the paddle and sends it back in the opposite direction at a random angle
            
                return True
        else:
            # Conditions for contact when Ball is moving from the left
            if (paddle_point2X >= ballX >= paddle_point1X) and (paddle_point2Y >= ballY >= paddle_point1Y):
                # Ball collides with the paddle
                self.dx = -self.dx
                self.dy += random.uniform(-1, 1)       # Ball collides with the paddle and send it back in the opposite direction at a random angle
            
                return True

        return False   

        
    def GameEndcheck(self): 
        '''function that defined the Game limit function,
      the score goes to 5 before you have to restart the game again'''


        # Checks score of player 1 and when it equals 3 displays you win, then game ends
        if self.p1score == 3:
            Endcard = Text(Point(250, 250),"You Win!")
            Endcard.setFill("green")
            Endcard.draw(win)
            time.sleep(3)
            win.close()     

        # Checks score of player 2 and when it equals 3 displays you win, then game ends
        elif self.p2score == 3:
            Endcard = Text(Point(250, 250),"You Lost...")
            Endcard.setFill("red")
            Endcard.draw(win)
            time.sleep(3)
            win.close()

    def getCenter(self):
        ''' Function use to get the center of our ball'''
        return self.ball.getCenter()


def displayMenu():
    ''' function use to serve as a menu. It will ask the
     if you want to play agaisnt a computer or player 2 with controls'''
    print("Welcome to Pong!")
    print("Select an option:")
    print("1. Play against AI")
    print("2. Play against another player")
    choice = input("Enter your choice (1 or 2): ")
    return choice

def mainloop():
    '''Mainloop uses the different classes and methods combined to run the pong game'''
    
    choice = displayMenu()

    if choice == '1':
        # Play against AI
        p2 = AI_Paddle(495, 190, 490, 280, 'w', 's')
    elif choice == '2':
        # Play against another player
        p2 = PlayerTwoPaddle(495, 190, 490, 280, 'w', 's')
    else:
        print("Invalid choice. Please enter '1' or '2'.")
        return

    ball1 = BALL()
    p1 = Paddle(5, 190, 10, 280, 'Up', 'Down')

    while win.isOpen():
        key = win.checkKey()
        ball1.ballmove()
        p1.move(key)
        
        # If player 2 is controlled by a human
        if choice == '2':
            p2.move(key)
        # If player 2 is controlled by AI
        else:
            p2.move(ball1)
            
        ball1.contact(p1)
        ball1.contact(p2)
        ball1.GameEndcheck()
        time.sleep(0.01)

mainloop()