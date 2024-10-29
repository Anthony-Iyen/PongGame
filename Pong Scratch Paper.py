

from graphics import *
import time
import math
import random

WIDTH = 500
HEIGHT = 500
win = GraphWin("Pong", WIDTH, HEIGHT)
win.setBackground("Black")


class PADDLE:
    def __init__(self):
        self.player = Rectangle(Point(10, 10), Point(34, 100))
        self.player.setFill("white")
        self.player.draw(win)

        self.PlocationX = self.player.getP2().getX()
        self.PlocationY = self.player.getP2().getY()

    def move(self):
        key = win.checkKey()
        player = self.player

        B = player.getP1()
        C = B.getY()

        if C > 0:

            if key == 'Up':
                player.move(0, -10)

        B = player.getP2()
        C = B.getY()

        if C < 500:

            if key == 'Down':
                player.move(0, 10)

        self.PlocationX = self.player.getP2().getX()
        self.PlocationY = self.player.getP2().getY()

        return self.PlocationX, self.PlocationY  # Meant to return the location of the player after each loop


class BALL:
    def __init__(self):

        center = Point(250, 250)
        self.ball = Circle(center, 20)
        self.ball.setFill("white")
        self.ball.draw(win)

        self.dx = 1
        self.dy = 0

    # def ballmove(self):

    #     self.ball.move(self.dx, self.dy)

    #     if self.ball.getP1().getX() <= 0:
    #         self.dx = -self.dx
    #     elif self.ball.getP2().getX() >= win.getWidth():
    #         self.dx = -self.dx
    #     if self.ball.getP1().getY() <= 0:
    #         self.dy = -self.dy + 1
    #     elif self.ball.getP2().getY() >= win.getHeight():
    #         self.dy = -self.dy + 1

    #     dx, dy = self.dx, self.dy
    #     return dx, dy  # Meant to return the location of the ball after each loop
        
    def ballmove(self):

        self.ball.move(self.dx, self.dy)

    # Check if the ball has gone past the left or right edge of the window
        if self.ball.getP1().getX() <= 0 or self.ball.getP2().getX() >= win.getWidth():
            # Reset the ball to the middle of the window
            self.ball.move(win.getWidth() / 2 - self.ball.getCenter().getX(), 0)
        # Reverse the direction of movement
            self.dx = -self.dx

    # Check if the ball has gone past the top or bottom edge of the window
        if self.ball.getP1().getY() <= 0:
            self.dy = -self.dy
        elif self.ball.getP2().getY() >= win.getHeight():
            self.dy = -self.dy

        dx, dy = self.dx, self.dy
        return dx, dy  # Meant to return the location of the ball after each loop



# def contact(ball, paddle):
#     ball_center = ball.getCenter()
#     ball_x, ball_y = ball_center.getX(), ball_center.getY()
#     paddle_p1, paddle_p2 = paddle.getP1(), paddle.getP2()
#     paddle_x1, paddle_y1 = paddle_p1.getX(), paddle_p1.getY()
#     paddle_x2, paddle_y2 = paddle_p2.getX(), paddle_p2.getY()

#     # Check if the ball is within the bounds of the paddle
#     if (paddle_x1 <= ball_x <= paddle_x2) and (paddle_y1 <= ball_y <= paddle_y2):
#         return True
#     else:
#         return False


    def contact(self,ball, paddle):
        ball_center = ball.getCenter()
        ball_x, ball_y = ball_center.getX(), ball_center.getY()
        paddle_p1, paddle_p2 = paddle.getP1(), paddle.getP2()
        paddle_x1, paddle_y1 = paddle_p1.getX(), paddle_p1.getY()
        paddle_x2, paddle_y2 = paddle_p2.getX(), paddle_p2.getY()

        # Check if the ball is within the bounds of the paddle
        if (paddle_x1 <= ball_x <= paddle_x2) and (paddle_y1 <= ball_y <= paddle_y2):
    
            
            # Adjust the ball's direction based on the angle of reflection
            # (You need to update the ball's dx and dy attributes accordingly)
            return True
        else:
            return False


def mainloop():
    ball1 = BALL()
    p1 = PADDLE()

    while win.isOpen():

        p1.move()
        dx, dy = ball1.ballmove()

        # # Check for collision with paddle
        if ball1.contact(ball1.ball, p1.player):
            # Bounce back in the opposite direction
            ball1.dx = -ball1.dx
            ball1.dy = -ball1.dy

        time.sleep(00.01)

        # Close window if user clicks close button
        if win.checkMouse() is not None:
            break


mainloop()





#Trajectory example

# from graphics import *
# import time

# # Define constants
# WIDTH = 800
# HEIGHT = 600
# DELTA_TIME = 0.05  # Time step for simulation
# GRAVITY = 9.8  # Acceleration due to gravity (m/s^2)

# # Create a graphics window
# win = GraphWin("Trajectory Simulation", WIDTH, HEIGHT)
# win.setBackground("white")

# # Create a ball object (circle) at the initial position
# initial_position = Point(100, HEIGHT - 50)
# ball_radius = 10
# ball = Circle(initial_position, ball_radius)
# ball.setFill("red")
# ball.draw(win)

# # Define initial velocity components
# velocity_x = 10  # Initial horizontal velocity (pixels/second)
# velocity_y = -50  # Initial vertical velocity (pixels/second), negative since y-axis is inverted

# # Simulation loop
# current_time = 0
# while True:
#     # Update position based on velocity
#     displacement_x = velocity_x * DELTA_TIME
#     displacement_y = velocity_y * DELTA_TIME + 0.5 * GRAVITY * DELTA_TIME ** 2
#     ball.move(displacement_x, displacement_y)
    
#     # Update velocity due to gravity
#     velocity_y += GRAVITY * DELTA_TIME
    
#     # Check for collision with ground
#     if ball.getCenter().getY() + ball_radius >= HEIGHT:
#         velocity_y *= -0.9  # Reverse velocity and dampen for bouncing effect
    
    
#     # Wait for a short time (simulate real-time)
#     time.sleep(DELTA_TIME)
    
#     # Update current time
#     current_time += DELTA_TIME

# # Close the graphics window
# win.close()



    # def contact(self, paddle):
    #     ball_center = self.ball.getCenter()
    #     ball_radius = self.ball.getRadius()
    #     ballX = ball_center.getX() + ball_radius
    #     ballY = ball_center.getY()

    #     paddle_width = paddle.player.getP2().getX() - paddle.player.getP1().getX()
    #     paddle_height = paddle.player.getP2().getY() - paddle.player.getP1().getY()
    #     paddle_leftX = paddle.player.getP1().getX()
    #     paddle_rightX = paddle.player.getP2().getX() + paddle_width + ball_radius
    #     paddle_topY = paddle.player.getP1().getY()
    #     paddle_bottomY = paddle.player.getP2().getY() + paddle_width

    #     if self.dx > 0:
    #         # Ball is moving to the right
    #         if (paddle_leftX <= ballX <= paddle_rightX) and (paddle_topY <= ballY <= paddle_bottomY):
    #             # Ball collides with the paddle
    #             self.dx = -self.dx
    #             return True
    #     else:
    #         # Ball is moving to the left
    #         if (paddle_rightX >= ballX >= paddle_leftX) and (paddle_bottomY >= ballY >= paddle_topY):
    #             # Ball collides with the paddle
    #             self.dx = -self.dx
    #             return True

    #         # Check for collision with top corners and bottom corner of the paddle
    #         if (ballY - ball_radius <= paddle_topY and ballX - ball_radius <= paddle_leftX) and \
    #            (math.sqrt((paddle_leftX - ball_center.getX()) ** 2 + (paddle_topY - ball_center.getY()) ** 2) <= ball_radius):
    #             self.dx = -self.dx
    #             self.dy = -self.dy
    #             return True

    #         # Check for collision with top right corner of the paddle
    #         if (ballY - ball_radius <= paddle_topY and ballX + ball_radius >= paddle_rightX) and \
    #            (math.sqrt((paddle_rightX - ball_center.getX()) ** 2 + (paddle_topY - ball_center.getY()) ** 2) <= ball_radius):
    #             self.dx = -self.dx
    #             self.dy = -self.dy
    #             return True

    #         # Check for collision with bottom left corner of the paddle
    #         if (ballY + ball_radius >= paddle_bottomY and ballX - ball_radius <= paddle_leftX) and \
    #            (math.sqrt((paddle_leftX - ball_center.getX()) ** 2 + (paddle_bottomY - ball_center.getY()) ** 2) <= ball_radius):
    #             self.dx = -self.dx
    #             self.dy = -self.dy
    #             return True

    #         # Check for collision with bottom right corner of the paddle
    #         if (ballY + ball_radius >= paddle_bottomY and ballX + ball_radius >= paddle_rightX) and \
    #            (math.sqrt((paddle_rightX - ball_center.getX()) ** 2 + (paddle_bottomY - ball_center.getY()) ** 2) <= ball_radius):
    #             self.dx = -self.dx
    #             self.dy = -self.dy
    #             return True

    #         return False



    # def contact(self, paddle):
    #     ball_center = self.ball.getCenter()
    #     ball_radius = self.ball.getRadius()
    #     ballX = ball_center.getX() + ball_radius
    #     ballY = ball_center.getY() + ball_radius


    #     paddle_width = paddle.player.getP2().getX() - paddle.player.getP1().getX()
    #     paddle_height = paddle.player.getP2().getY() - paddle.player.getP1().getY()

    #     paddle_leftX = paddle.player.getP1().getX()
    #     paddle_rightX = paddle.player.getP2().getX() + paddle_width + ball_radius
    #     paddle_topY = paddle.player.getP1().getY()
    #     paddle_bottomY = paddle.player.getP2().getY() + paddle_height

    #     if self.dx > 0:
    #         # Ball is moving to the right
    #         if (paddle_leftX <= ballX <= paddle_rightX) and (paddle_topY <= ballY <= paddle_bottomY):
    #             # Ball collides with the paddle
    #             self.dx = -self.dx
    #             return True
    #     else:
    #         # Ball is moving to the left
    #         if (paddle_rightX >= ballX >= paddle_leftX) and (paddle_bottomY >= ballY >= paddle_topY):
    #             # Ball collides with the paddle
    #             self.dx = -self.dx
    #             return True
            


#  def menuDisplay(self):
#     #not sure how to make this not reptitive

#         # Display menu options
#         Mainmenu = Text(Point(250,150), "Game Modes")
#         Mainmenu.setSize(20)
#         Mainmenu.setFill("white")
#         Mainmenu.draw(win)

#         Optionai = Text(Point(250,250), "1.Against AI")
#         Optionai.setSize(15)
#         Optionai.setFill("white")
#         Optionai.draw(win)

#         Optionplayer = Text(Point(250, 300), "2.Another player")
#         Optionplayer.setSize(15)
#         Optionplayer.setFill("white")
#         Optionplayer.draw(win)
#         return Mainmenu,Optionai,Optionplayer

#     def choosingGame(self):
#         Mainmenu, Optionai, Optionplayer = self.menuDisplay()
#         while True:
#             click = win.getMouse()
#             Optionai_anchor = Optionai.getAnchor()
#             Optionplayer_anchor = Optionplayer.getAnchor()
#             Optionai_width = Optionai.getWidth()
#             Optionai_height = Optionai.getHeight()
#             Optionplayer_width = Optionplayer.getWidth()
#             Optionplayer_height = Optionplayer.getHeight()

#             if (Optionai_anchor.getX() - Optionai_width / 2 < click.getX() < Optionai_anchor.getX() + Optionai_width / 2) and \
#             (Optionai_anchor.getY() - Optionai_height / 2 < click.getY() < Optionai_anchor.getY() + Optionai_height / 2):
#                 Mainmenu.undraw()
#                 Optionai.undraw()
#                 Optionplayer.undraw()
#                 return 'Ai'
#             elif (Optionplayer_anchor.getX() - Optionplayer_width / 2 < click.getX() < Optionplayer_anchor.getX() + Optionplayer_width / 2) and \
#                 (Optionplayer_anchor.getY() - Optionplayer_height / 2 < click.getY() < Optionplayer_anchor.getY() + Optionplayer_height / 2):
#                 Mainmenu.undraw()
#                 Optionai.undraw()
#                 Optionplayer.undraw()
#                 return 'Player2'


                

# # #Anthony Iyengunmwena and Nicholas Rackoff
# # # Intro to CS Final Project
# # #Pong Game

# from graphics import *
# import time
# import random


# WIDTH = 500
# HEIGHT = 500
# win = GraphWin("Pong",WIDTH, HEIGHT)
# win.setBackground("Black")

# class Paddle:
#     def __init__(self, x1, y1, x2, y2, up_key, down_key):
#         self.player = Rectangle(Point(x1, y1), Point(x2, y2))
#         self.player2 = Rectangle(Point(x1, y1), Point(x2, y2))
#         self.player.setFill("white")
#         self.player.draw(win)
#         self.up_key = up_key
#         self.down_key = down_key
       
#     def move(self, key, ball_x, choice):
#         player = self.player

#         B = player.getP1()
#         C = B.getY()

#         if C > 0 and choice == '2':
#             if key == self.up_key and ball_x < WIDTH / 2:
#                 player.move(0, -10)

#         B = player.getP2()
#         C = B.getY()

#         if C < HEIGHT and choice == '2':
#             if key == self.down_key and ball_x < WIDTH / 2:
#                 player.move(0, 10)

# class AI_Paddle(Paddle):
    
#     def __init__(self, x1, y1, x2, y2, up_key, down_key):
#         super().__init__(x1, y1, x2, y2, up_key, down_key)  # Inherits from Paddle

#     def move(self, ball):
#         ball_center = ball.getCenter()
#         ball_y = ball_center.getY()
#         ball_x = ball_center.getX()
#         paddle_center_y = self.player.getCenter().getY()

#         # Find the difference between ball's Y and paddle's center Y
#         trackrange = ball_y - paddle_center_y +random.randrange(-5,5)


#         # Move towards the ball 
#         speed = random.uniform(-3,5)  

#         if ball_x > 250: #Only moves if the ball is on it's side, to reduce lag.
#             if trackrange > 20:
#                self.player.move(0, speed)
#             elif trackrange < -20:
#                self.player.move(0, -speed)
#         else:
#             # Move randomly to the opposite side
#             if random.random() < 0.2:  # Adjust the probability as needed
#                 # Randomly choose the direction to move
#                 direction = random.choice([-1, 1])  # -1 for up, 1 for down
#                 self.player.move(0, direction * speed)
               
#         # Prevent paddle from going out of bounds
#         if self.player.getP1().getY() <= 0:
#             self.player.move(0, 10)
#         elif self.player.getP2().getY() >= HEIGHT:
#             self.player.move(0, -10)


# class PlayerTwoPaddle(Paddle):
#     def __init__(self, x1, y1, x2, y2, up_key, down_key):
#         super().__init__(x1, y1, x2, y2, up_key, down_key)
        
    
# class BALL:
#     def __init__(self):

#         self.center = Point(250,250)
#         self.ball = Circle((self.center), 20)
#         self.ball.setFill("white")
#         self.ball.draw(win)

#         self.dx = -1
#         self.dy = 0

#         self.p1score = 0
#         self.p2score = 0

#         self.resetcheck = False

#         win_width= win.getWidth()
#         self.middlex= win_width/2

#         win_height= win.getHeight()
#         self.middley= win_height/2

#         self.score1 = Text(Point(100, 75),self.p2score)
#         self.score1.setFill("white")
#         self.score1.draw(win)

#         self.score2 = Text(Point(400, 75),self.p1score)
#         self.score2.setFill("white")
#         self.score2.draw(win) 

       
#     def ballmove(self):
        
#         self.ball.move(self.dx,self.dy)
#         self.resetcheck = False

#         # key= win.getKey() #we want key to be the inital start of the game 

#         # if key == "Up" or key == "Down":
#         #     self.ball.move(self.dx,self.dy)
        

#         if self.ball.getP1().getX() <= 0:
#             #need to fix this so it waits for key push
#             self.ball.undraw()
#             self.ball = Circle((self.center), 20)
#             self.ball.setFill("white")

#             self.dx = 1
#             self.dy = 0
#             self.p2score += 1

#             self.score2.undraw()
#             self.score2 = Text(Point(400, 75),self.p2score)
#             self.score2.setFill("white")
#             self.score2.draw(win)

            
#             self.ball.draw(win)  
#             time.sleep(5)
#             self.resetcheck = True

#         elif self.ball.getP2().getX()>= win.getWidth():

#             self.ball.undraw()
#             self.ball = Circle((self.center), 20)
#             self.ball.setFill("white")
#             self.dx = -1
#             self.dy = 0
#             self.p1score += 1

#             self.score1.undraw()
#             self.score1 = Text(Point(100, 75),self.p1score)
#             self.score1.setFill("white")
#             self.score1.draw(win)

#             self.ball.draw(win)
#             time.sleep(5)
#             self.resetcheck = True


#         if self.ball.getP1().getY()<= 0:
#             self.dy=-self.dy
#         elif self.ball.getP2().getY()>= win.getHeight():
#             self.dy=-self.dy



#     #     # # #print statements to see if postion is working 
#     #     # print("Ball X:", ballX, "Ball Y:", ballY)
#     #     # print("Paddle Left X:", paddle_leftX, "Paddle Left Y:", paddle_leftY)
#     #     # print("Paddle Right X:", paddle_rightX, "Paddle Right Y:", paddle_rightY)

  
#     def contact(self, paddle):
#         ball_center = self.ball.getCenter()
#         ball_radius=self.ball.getRadius()
#         ballX = ball_center.getX()+ball_radius
#         ballY = ball_center.getY()+ball_radius

#         paddle_width = paddle.player.getP2().getX() - paddle.player.getP1().getX()
#         paddle_height= (paddle.player.getP2().getY() - paddle.player.getP1().getY())/2

#         paddle_point1X = paddle.player.getP1().getX()
#         paddle_point2X = paddle.player.getP2().getX()+paddle_width+ball_radius
#         paddle_point1Y = paddle.player.getP1().getY()
#         paddle_point2Y = paddle.player.getP2().getY()+paddle_height+ball_radius

#         if self.dx > 0:
#             # Ball is moving to the right
#             if (paddle_point1X <= ballX <= paddle_point2X) and (paddle_point1Y <= ballY <= paddle_point2Y):
#                 # Ball collides with the paddle
#                 self.dx = -self.dx
#                 self.dy += random.uniform(-2, 2) 
              

#                 return True
#         else:
#             # Ball is moving to the left
#             if (paddle_point2X >= ballX >= paddle_point1X) and (paddle_point2Y >= ballY >= paddle_point1Y):
#                 # Ball collides with the paddle
#                 self.dx = -self.dx
#                 self.dy += random.uniform(-1, 1) 
            

#                 return True

#         return False


       

        
#     def GameEndcheck(self): 

#         if self.p1score == 5:
#             Endcard = Text(Point(250, 250),"You Win!")
#             Endcard.setFill("green")
#             Endcard.draw(win)
#             time.sleep(3)
#             win.close()     



#         elif self.p2score == 5:
#             Endcard = Text(Point(250, 250),"You Lost...")
#             Endcard.setFill("red")
#             Endcard.draw(win)
#             time.sleep(3)
#             win.close()

#     def getCenter(self):
#         return self.ball.getCenter()


# def display_menu():
#     print("Welcome to Pong!")
#     print("Select an option:")
#     print("1. Play against AI")
#     print("2. Play against another player")
#     choice = input("Enter your choice (1 or 2): ")
#     return choice

# def mainloop():
#     choice = display_menu()

#     if choice == '1':
#         # Play against AI
#         p2 = AI_Paddle(5, 190, 10, 280, 'w', 's')
#     elif choice == '2':
#         # Play against another player
#         p2 = PlayerTwoPaddle(495, 190, 490, 280, 'w', 's')
#     else:
#         print("Invalid choice. Please enter '1' or '2'.")
#         return

#     ball1 = BALL()
#     p1 = Paddle(10, 10, 34, 100, 'Up', 'Down')

#     while win.isOpen():
#         key = win.checkKey()
#         ball1.ballmove()
#         p1.move(key)
        
#         # If player 2 is controlled by a human
#         if choice == '2':
#             p2.move(key)
#         # If player 2 is controlled by AI
#         else:
#             p2.move(ball1)
            
#         ball1.contact(p1)
#         ball1.contact(p2)
#         ball1.GameEndcheck()
#         time.sleep(0.01)

# mainloop()