"""
File: my_drawing
Name:陳蓉靚
----------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GRect
from campy.graphics.gwindow import GWindow

window = GWindow(400, 400)

def main():
    """
    Because tulips are beautiful (n_n)/ weeeee~~
    """
    bg = GRect(400, 400, x=0, y=0)
    bg.filled = True
    bg.fill_color = 'gainsboro'

    # f1 = GOval(30, 60, x=117, y=200)
    # f1.filled = True
    # f1.color = 'indianred'
    # f1.fill_color = 'indianred'
    #
    # f6 = GOval(30, 60, x=120, y=200)
    # f6.filled = True
    # f6.color = 'brown'
    # f6.fill_color = 'brown'
    #
    # f5 = GOval(30, 60, x=127, y=200)
    # f5.filled = True
    # f5.color = 'brown'
    # f5.fill_color = 'brown'
    #
    # f3 = GOval(30, 60, x=130, y=200)
    # f3.filled = True
    # f3.color = 'indianred'
    # f3.fill_color = 'indianred'
    #
    # f4 = GOval(30, 60, x=138, y=200)
    # f4.filled = True
    # f4.color = 'lightcoral'
    # f4.fill_color = 'lightcoral'
    #
    # ff1 = GOval(30, 60, x=200, y=175)
    # ff1.filled = True
    # ff1.color = 'mediumslateblue'
    # ff1.fill_color = 'mediumslateblue'
    #
    # ff6 = GOval(30, 60, x=203, y=175)
    # ff6.filled = True
    # ff6.color = 'slateblue'
    # ff6.fill_color = 'slateblue'
    #
    # ff5 = GOval(30, 60, x=206, y=175)
    # ff5.filled = True
    # ff5.color = 'slateblue'
    # ff5.fill_color = 'slateblue'
    #
    # ff3 = GOval(30, 60, x=209, y=175)
    # ff3.filled = True
    # ff3.color = 'mediumslateblue'
    # ff3.fill_color = 'mediumslateblue'
    #
    # ff4 = GOval(30, 60, x=217, y=175)
    # ff4.filled = True
    # ff4.color = 'mediumpurple'
    # ff4.fill_color = 'mediumpurple'
    #
    # g1 = GRect(5, 200, x=140, y=260)
    # g1.color = 'darkseagreen'
    # g1.filled = True
    # g1.fill_color = 'darkseagreen'
    #
    # gg1 = GRect(5, 225, x=220, y=235)
    # gg1.color = 'darkseagreen'
    # gg1.filled = True
    # gg1.fill_color = 'darkseagreen'
    # #
    d1 = GOval(120, 120, x=0, y=100)
    d1.filled = True
    d1.fill_color = 'lavender'
    d1.color = 'lavender'

    d2 = GOval(120, 120, x=170, y=250)
    d2.filled = True
    d2.fill_color = 'lavender'
    d2.color = 'lavender'

    d3 = GOval(120, 120, x=110, y=150)
    d3.filled = True
    d3.fill_color = 'gainsboro'
    d3.color = 'gainsboro'

    d4 = GRect(240, 300, x=0, y= 150)
    d4.filled = True
    d4.fill_color = 'lavender'
    d4.color = 'lavender'

    d5 = GRect(250, 116, x=115, y=150)
    d5.filled = True
    d5.fill_color = 'gainsboro'
    d5.color = 'gainsboro'

    d6 = GOval(50, 50, x=110, y=230)
    d6.filled = True
    d6.fill_color = 'lavender'
    d6.color = 'lavender'
    #
    d7 = GOval(140, 120, x=100, y=355)
    d7.filled = True
    d7.fill_color = 'gainsboro'
    d7.color = 'gainsboro'

    d8 = GRect(100, 50, x=130, y=365)
    d8.filled = True
    d8.fill_color = 'gainsboro'
    d8.color = 'gainsboro'
    #
    dd1 = GOval(120, 120, x=175, y=-50)
    dd1.filled = True
    dd1.fill_color = 'lightcyan'
    dd1.color = 'lightcyan'

    dd2 = GOval(100, 100, x=350, y=50)
    dd2.filled = True
    dd2.fill_color = 'lightcyan'
    dd2.color = 'lightcyan'

    dd3 = GOval(90, 90, x=260, y=45)
    dd3.filled = True
    dd3.fill_color = 'gainsboro'
    dd3.color = 'gainsboro'

    dd4 = GOval(140, 140, x=275, y=-50)
    dd4.filled = True
    dd4.fill_color = 'lightcyan'
    dd4.color = 'lightcyan'

    o1 = GOval(110, 110, x=345, y= 200)
    o1.filled = True
    o1.fill_color = 'lightpink'
    o1.color = 'lightpink'

    o2 = GOval(125, 125, x=200, y=320)
    o2.filled = True
    o2.fill_color = 'lightpink'
    o2.color = 'lightpink'
    #
    o3 = GOval(110, 110, x=235, y=215)
    o3.filled = True
    o3.fill_color = 'gainsboro'
    o3.color = 'gainsboro'
    #
    o4 = GOval(155, 155, x=285, y=255)
    o4.filled = True
    o4.fill_color = 'lightpink'
    o4.color = 'lightpink'

    # y1 = GOval(15, 70, x=145, y=350)
    # y1.color = 'darkseagreen'
    # y1.filled = True
    # y1.fill_color = 'darkseagreen'
    #
    # y2 = GOval(15, 70, x=130, y=350)
    # y2.color = 'darkseagreen'
    # y2.filled = True
    # y2.fill_color = 'darkseagreen'
    #
    # y3 = GRect(20, 30, x=135, y=370)
    # y3.color = 'darkseagreen'
    # y3.filled = True
    # y3.fill_color = 'darkseagreen'
    #
    # yy1 = GOval(20, 100, x=205, y=315)
    # yy1.color = 'darkseagreen'
    # yy1.filled = True
    # yy1.fill_color = 'darkseagreen'
    #
    # yy2 = GOval(20, 100, x=225, y=315)
    # yy2.color = 'darkseagreen'
    # yy2.filled = True
    # yy2.fill_color = 'darkseagreen'
    #
    # yy3 = GRect(20, 20, x=215, y=385)
    # yy3.color = 'darkseagreen'
    # yy3.filled = True
    # yy3.fill_color = 'darkseagreen'
    #
    w1 = GOval(185, 185, x=230, y=85)
    w1.color = 'whitesmoke'
    w1.filled = True
    w1.fill_color = 'whitesmoke'

    w2 = GOval(270, 250, x=-70, y=-70)
    w2.color = 'lightgoldenrodyellow'
    w2.filled = True
    w2.fill_color = 'lightgoldenrodyellow'


    window.add(bg)
    window.add(dd4)
    window.add(dd1)
    window.add(dd3)
    window.add(d4)
    window.add(d5)
    window.add(d6)
    window.add(d7)
    window.add(d8)
    window.add(d3)
    window.add(w2)
    window.add(o4)
    window.add(o3)
    window.add(d1)
    window.add(d2)
    window.add(dd2)
    window.add(w1)
    window.add(o1)
    window.add(o2)
    window.add(f1)
    window.add(f6)
    window.add(f5)
    window.add(f3)
    window.add(f4)
    window.add(g1)
    window.add(ff1)
    window.add(ff6)
    window.add(ff5)
    window.add(ff3)
    window.add(ff4)
    window.add(gg1)
    window.add(y1)
    window.add(y2)
    window.add(y3)
    window.add(yy1)
    window.add(yy2)
    window.add(yy3)






if __name__ == '__main__':
    main()
