"""
File: draw_line
Name:陳蓉靚
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

SIZE = 5
x1 = 0
y1 = 0
x2 = 0
y2 = 0
window = GWindow(width=500, height=500)

TIME = 0

dot = GOval(SIZE, SIZE)


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(create_dot)


def create_dot(click):
    global TIME, x1, x2, y1, y2, dot
    TIME += 1
    if TIME != 2:
        x1 = click.x
        y1 = click.y
        dot.filled = False
        dot.color = 'black'
        window.add(dot, x=x1, y=y1)
    else:
        x2 = click.x
        y2 = click.y
        line = GLine(dot.x, dot.y, x2, y2)
        line.color = 'black'
        window.remove(dot)
        window.add(line)
        TIME = 0






if __name__ == "__main__":
    main()
