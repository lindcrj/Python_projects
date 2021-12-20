"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random


BRICK_SPACING = 5  # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40  # Height of a brick (in pixels).
BRICK_HEIGHT = 15  # Height of a brick (in pixels).
BRICK_ROWS = 10  # Number of rows of bricks.
BRICK_COLS = 10  # Number of columns of bricks.
BRICK_OFFSET = 50  # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 15  # Radius of the ball (in pixels).
PADDLE_WIDTH = 75  # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15  # Height of the paddle (in pixels).
PADDLE_OFFSET = 50  # Vertical offset of the paddle from the window bottom (in pixels).
FRAME_RATE = 1000 / 120
NUM_LIVES = 3

INITIAL_Y_SPEED = 7  # Initial vertical speed for the ball.
MAX_X_SPEED = 5  # Maximum initial horizontal speed for the ball.


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH,
                 paddle_height=PADDLE_HEIGHT, paddle_offset=PADDLE_OFFSET,
                 brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS,
                 brick_width=BRICK_WIDTH, brick_height=BRICK_HEIGHT,
                 brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING,
                 title='BREAKOUT GAME n_n'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create label
        self.title = GLabel(title, self.window.width / 2 - 55, 25)
        self.window.add(self.title)

        self.bye = GLabel('Try again QQ')
        self.bye.color = 'tomato'


        # Create a paddle
        self.paddle = GRect(width=paddle_width, height=paddle_height, x=(window_width - paddle_width) / 2,
                            y=window_height - paddle_offset - paddle_height)
        self.paddle.filled = True
        self.paddle.color = 'pink'
        self.paddle.fill_color = 'pink'
        self.window.add(self.paddle)

        # Center a filled ball in the graphical window
        self.ball = GOval(width=ball_radius, height=ball_radius)
        self.ball.filled = True
        self.ball.fill_color = 'tomato'
        self.ball.color = 'tomato'
        self.ball_x_position = (window_width - ball_radius) / 2
        self.ball_y_position = (window_height - ball_radius) / 2
        self.window.add(self.ball, x=(window_width - ball_radius) / 2, y=(window_height - ball_radius) / 2)

        # Default initial velocity for the ball
        self.dy = 0
        self.dx = 0
        self.open = 0
        self.lives = NUM_LIVES

        self.lives_label = GLabel('Lives : ' + str(self.lives))
        self.lives_label.color = 'navy'


        # Initialize our mouse listeners
        onmouseclicked(self.start_the_game)
        onmousemoved(self.paddle_position)

        # Draw bricks
        start = 0
        row = brick_offset
        for j in range(brick_rows):
            if j == 0:
                for i in range(brick_cols):
                    self.bricks1 = GRect(width=brick_width, height=brick_height)
                    self.bricks1.filled = True
                    self.bricks1.color = 'cornflowerblue'
                    self.bricks1.fill_color = 'cornflowerblue'
                    self.window.add(self.bricks1, x=start, y=row)
                    start += (brick_width + brick_spacing)
            elif j == 1:
                row += (brick_height + brick_spacing)
                start = 0
                for i in range(brick_cols):
                    self.bricks1 = GRect(width=brick_width, height=brick_height)
                    self.bricks1.filled = True
                    self.bricks1.color = 'cornflowerblue'
                    self.bricks1.fill_color = 'cornflowerblue'
                    self.window.add(self.bricks1, x=start, y=row)
                    start += (brick_width + brick_spacing)
            elif j == 2 or j == 3:
                row += (brick_height + brick_spacing)
                start = 0
                for i in range(brick_cols):
                    self.bricks1 = GRect(width=brick_width, height=brick_height)
                    self.bricks1.filled = True
                    self.bricks1.color = 'gold'
                    self.bricks1.fill_color = 'gold'
                    self.window.add(self.bricks1, x=start, y=row)
                    start += (brick_width + brick_spacing)
            elif j == 4 or j == 5:
                row += (brick_height + brick_spacing)
                start = 0
                for i in range(brick_cols):
                    self.bricks1 = GRect(width=brick_width, height=brick_height)
                    self.bricks1.filled = True
                    self.bricks1.color = 'mediumaquamarine'
                    self.bricks1.fill_color = 'mediumaquamarine'
                    self.window.add(self.bricks1, x=start, y=row)
                    start += (brick_width + brick_spacing)
            elif j == 6 or j == 7:
                row += (brick_height + brick_spacing)
                start = 0
                for i in range(brick_cols):
                    self.bricks1 = GRect(width=brick_width, height=brick_height)
                    self.bricks1.filled = True
                    self.bricks1.color = 'lightcoral'
                    self.bricks1.fill_color = 'lightcoral'
                    self.window.add(self.bricks1, x=start, y=row)
                    start += (brick_width + brick_spacing)
            elif j == 8 or j == 9:
                row += (brick_height + brick_spacing)
                start = 0
                for i in range(brick_cols):
                    self.bricks1 = GRect(width=brick_width, height=brick_height)
                    self.bricks1.filled = True
                    self.bricks1.color = 'mediumpurple'
                    self.bricks1.fill_color = 'mediumpurple'
                    self.window.add(self.bricks1, x=start, y=row)
                    start += (brick_width + brick_spacing)

    def start_the_game(self, mouse):  # onmouseclick之後
        if self.open == 0:
            self.open = 1
            self.dy = INITIAL_Y_SPEED
            self.dx = random.randint(1, MAX_X_SPEED)
            if random.random() > 0.5:
                self.dx *= -1

    def paddle_position(self, mouse):
        self.paddle.x = mouse.x - self.paddle.width / 2
        self.paddle.x_end = self.paddle.x + self.paddle.width
        self.paddle.y = self.window.height - PADDLE_OFFSET
        if mouse.x <= self.window.width - self.paddle.width:
            if mouse.x <= self.paddle.width / 2:
                self.paddle.x = 0
        elif mouse.x > self.window.width - self.paddle.width / 2:
            self.paddle.x = self.window.width - self.paddle.width
            self.paddle.y = self.window.height - PADDLE_OFFSET

    def object_check(self):
        get_1 = self.window.get_object_at(self.ball.x, self.ball.y)
        get_2 = self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y)
        get_3 = self.window.get_object_at(self.ball.x, self.ball.y + self.ball.height)
        get_4 = self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y + self.ball.height)
        if get_1 is not None:
            if get_1 is not self.title:
                if get_1 == self.paddle:
                    self.dy = - self.dy
                else:
                    self.window.remove(get_1)
                    self.dy = - self.dy
        elif get_2 is not None:
            if get_2 is not self.title:
                if get_2 == self.paddle:
                    self.dy = - self.dy
                else:
                    self.window.remove(get_2)
                    self.dy = - self.dy
        elif get_3 is not None:
            if get_3 is not self.title:
                if get_3 == self.paddle:
                    self.dy = - self.dy
                else:
                    self.window.remove(get_3)
                    self.dy = - self.dy
        elif get_4 is not None:
            if get_4 is not self.title:
                if get_4 == self.paddle:
                    self.dy = - self.dy
                else:
                    self.window.remove(get_4)
                    self.dy = - self.dy

    def window_check(self):
        if self.ball.y >= self.window.height - self.ball.height:
            self.window.add(self.ball, x=self.ball_x_position, y=self.ball_y_position)
            self.dx = 0
            self.dy = 0
            self.open = 0
            self.lives -= 1
            self.lives_label.text = 'Lives: ' + str(self.lives)
        else:
            if self.ball.x >= self.window.width - self.ball.width:
                self.dx = - self.dx
            elif self.ball.x <= 0:
                self.dx = - self.dx
            if self.ball.y <= 0:
                self.dy = -self.dy
        return self.ball, self.lives

    def game_over(self):
        self.window.remove(self.ball)
        self.window.remove(self.paddle)

    # def show(self):
    #     if self.ball.y >= self.window.height - self.ball.height:
    #         self.lives -= 1
    #         self.lives_label.text = 'Lives: ' + str(self.lives)
    #     return self.lives_label

        # if self.lives != 0:
        #     if self.open == 1:
        #         if self.ball.y >= self.window.height - self.ball.height:
        #             self.lives -= 1
        #             self.lives_label.text = 'Lives: ' + str(self.lives)

        # while True:
        #     if self.lives != 0:
        #         if self.open == 1:
        #             if self.ball.y >= self.window.height - self.ball.height:
        #                 self.lives -= 1
        #                 self.lives_label.text = 'Lives: ' + str(self.lives)
        #     break

