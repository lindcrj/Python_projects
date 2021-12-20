"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 1000 / 120 # 120 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics()
    graphics.window.add(graphics.lives_label, x=graphics.window.width - 70, y=25)
    while True:
        if graphics.lives == 0:
            graphics.game_over()
            graphics.window.add(graphics.bye, (graphics.window.width - graphics.bye.width) / 2, graphics.window.height / 2)
            break
        else:
            dx = graphics.dx
            dy = graphics.dy
            pause(FRAME_RATE)
            graphics.ball.move(dx, dy)
            pause(FRAME_RATE)
            graphics.window_check()
            if graphics.open == 1:
                graphics.object_check()
                # graphics.show()
                # if graphics.ball.y >= graphics.window.height - graphics.ball.height:
                #     graphics.lives -= 1
                #     graphics.lives_label.text = 'Lives: ' + str(graphics.lives)
                #     graphics.window.add(graphics.lives_label, x=graphics.window.width - 70, y=25)










if __name__ == '__main__':
    main()
