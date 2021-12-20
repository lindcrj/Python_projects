"""
File: bouncing_ball
Name:陳蓉靚
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 5
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40
TIME = 0


window = GWindow(800, 500, title='bouncing_ball.py')
ball = GOval(SIZE, SIZE)
start = 1
time = 0


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    global time
    ball.filled = True
    ball.fill_color = 'black'
    window.add(ball, x=START_X, y=START_Y)
    onmouseclicked(fall)


def fall(click):
    global VX, ball, start, time
    if time <= 2:
        time += 1
        if start == 1:
            start = 0
            v = 0
            while True:
                if ball.x <= window.width:
                    ball.move(VX, v)
                    pause(DELAY)
                    if ball.y <= window.height - SIZE:
                        v += GRAVITY
                    elif v >= 0:
                        v *= -REDUCE
                else:
                    window.add(ball, x=START_X, y=START_Y)
                    start = 1
                    break
    else:
        window.add(ball, x=START_X, y=START_Y)
        start = 0




if __name__ == "__main__":
    main()
