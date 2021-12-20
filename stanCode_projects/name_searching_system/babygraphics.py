"""
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.

YOUR DESCRIPTION HERE
"""

import tkinter as tk
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index of the current year in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                              with the specified year.
    """
    space = int((width-(GRAPH_MARGIN_SIZE*2))/len(YEARS))
    if year_index == 0:
        x_coordinate = GRAPH_MARGIN_SIZE
    else:
        x_coordinate = GRAPH_MARGIN_SIZE + space*year_index
    return x_coordinate






def draw_fixed_lines(canvas):
    """
    Erases all existing information on the given canvas and then
    draws the fixed background lines on it.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.

    Returns:
        This function does not return any value.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # Write your code below this line
    #################################
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, fill='black', width=LINE_WIDTH)
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE,
                       fill='black', width=LINE_WIDTH)
    canvas.create_line(GRAPH_MARGIN_SIZE, 0, GRAPH_MARGIN_SIZE, CANVAS_HEIGHT,fill='black', width=LINE_WIDTH)
    canvas.create_line(GRAPH_MARGIN_SIZE, 0, GRAPH_MARGIN_SIZE, CANVAS_HEIGHT, fill='black', width=LINE_WIDTH)
    for i in range(len(YEARS)):
        canvas.create_line(get_x_coordinate(CANVAS_WIDTH, i), 0, get_x_coordinate(CANVAS_WIDTH, i), CANVAS_HEIGHT, fill='black', width=LINE_WIDTH)
        canvas.create_text(get_x_coordinate(CANVAS_WIDTH, i), CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, text = YEARS[i], anchor = tk.NW, fill = 'black')

def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # Write your code below this line
    #################################
    rank_space = (CANVAS_HEIGHT - (GRAPH_MARGIN_SIZE*2))/MAX_RANK
    color_num = len(COLORS)
    c = 0
    color = COLORS[c]
    for n in lookup_names:
        if 0 < c <= 3:
            color = COLORS[c]
            c += 1
        elif c > 3:
            c = 0
            color = COLORS[c]
            c += 1
        else:
            c += 1
        for i in YEARS:  # [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010]
            if str(i) not in name_data[n]:
                if YEARS.index(i) < len(YEARS) - 1:
                    if str(YEARS[YEARS.index(i) + 1]) not in name_data[n]:
                        canvas.create_line(get_x_coordinate(CANVAS_WIDTH, YEARS.index(i)), CANVAS_HEIGHT - GRAPH_MARGIN_SIZE,
                                           get_x_coordinate(CANVAS_WIDTH, YEARS.index(i) + 1),
                                           CANVAS_HEIGHT - GRAPH_MARGIN_SIZE,
                                           fill=color, width=LINE_WIDTH)
                        canvas.create_text(get_x_coordinate(CANVAS_WIDTH, YEARS.index(i)) + TEXT_DX,
                                           CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, text=n + '*',
                                           anchor=tk.SW, fill=color)
                    else:
                        canvas.create_line(get_x_coordinate(CANVAS_WIDTH, YEARS.index(i)),
                                           CANVAS_HEIGHT - GRAPH_MARGIN_SIZE,
                                           get_x_coordinate(CANVAS_WIDTH, YEARS.index(i) + 1),
                                           rank_space * int(name_data[n][str(YEARS[YEARS.index(i)+1])]),
                                           fill=color, width=LINE_WIDTH)
                        canvas.create_text(get_x_coordinate(CANVAS_WIDTH, YEARS.index(i)) + TEXT_DX,
                                           CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, text=n + '*',
                                           anchor=tk.SW, fill=color)
                else:
                    canvas.create_text(get_x_coordinate(CANVAS_WIDTH, YEARS.index(i)) + TEXT_DX,
                                       CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, text=n + '*',
                                       anchor=tk.SW, fill=color)
            else:
                if int(name_data[n][str(i)]) <= MAX_RANK:
                    if YEARS.index(i) < len(YEARS)-1:
                        if str(YEARS[YEARS.index(i) + 1]) in name_data[n]:
                            canvas.create_line(get_x_coordinate(CANVAS_WIDTH, YEARS.index(i)),
                                               rank_space * int(name_data[n][str(i)]),
                                               get_x_coordinate(CANVAS_WIDTH, YEARS.index(i) + 1),
                                               rank_space * int(name_data[n][str(YEARS[YEARS.index(i)+1])]),
                                               fill=color, width=LINE_WIDTH)
                            canvas.create_text(get_x_coordinate(CANVAS_WIDTH, YEARS.index(i)) + TEXT_DX,
                                               rank_space * int(name_data[n][str(i)]), text=n + name_data[n][str(i)],
                                               anchor=tk.NW, fill=color)
                        else:
                            canvas.create_line(get_x_coordinate(CANVAS_WIDTH, YEARS.index(i)),
                                               rank_space * int(name_data[n][str(i)]),
                                               get_x_coordinate(CANVAS_WIDTH, YEARS.index(i) + 1),
                                               CANVAS_HEIGHT - GRAPH_MARGIN_SIZE,
                                               fill=color, width=LINE_WIDTH)
                            canvas.create_text(get_x_coordinate(CANVAS_WIDTH, YEARS.index(i)) + TEXT_DX,
                                               rank_space * int(name_data[n][str(i)]), text=n + name_data[n][str(i)],
                                               anchor=tk.NW, fill=color)
                    else:
                        canvas.create_text(get_x_coordinate(CANVAS_WIDTH, YEARS.index(i)) + TEXT_DX,
                                           rank_space * int(name_data[n][str(i)]), text=n + name_data[n][str(i)],
                                           anchor=tk.NW, fill=color)
                else:
                    canvas.create_text(get_x_coordinate(CANVAS_WIDTH, YEARS.index(i)) + TEXT_DX,
                                       CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, text=n + '*',
                                       anchor=tk.SW, fill=color)


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tk.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
