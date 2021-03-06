from tkinter import *
from random import randint
import PySimpleGUI as g
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, FigureCanvasAgg
from matplotlib.figure import Figure
import matplotlib.backends.tkagg as tkagg
import tkinter as Tk


def main():
    fig = Figure()

    ax = fig.add_subplot(111)
    ax.set_xlabel("X axis")
    ax.set_ylabel("Y axis")
    ax.grid()

    layout = [[g.Text('Animated Matplotlib', size=(40, 1), justification='center', font='Helvetica 20')],
              [g.Canvas(size=(640, 480), key='canvas')],
              [g.ReadFormButton('Exit', size=(10, 2), pad=((280, 0), 3), font='Helvetica 14')]]

    # create the form and show it without the plot  
    form = g.FlexForm('Demo Application - Embedding Matplotlib In PySimpleGUI')
    form.Layout(layout)
    form.ReadNonBlocking()

    canvas_elem = form.FindElement('canvas')

    graph = FigureCanvasTkAgg(fig, master=canvas_elem.TKCanvas)
    canvas = canvas_elem.TKCanvas

    dpts = [randint(0, 10) for x in range(10000)]
    for i in range(len(dpts)):
        button, values = form.ReadNonBlocking()
        if button is 'Exit' or values is None:
            exit(69)

        ax.cla()
        ax.grid()

        ax.plot(range(20), dpts[i:i + 20], color='purple')
        graph.draw()
        figure_x, figure_y, figure_w, figure_h = fig.bbox.bounds
        figure_w, figure_h = int(figure_w), int(figure_h)
        photo = Tk.PhotoImage(master=canvas, width=figure_w, height=figure_h)

        canvas.create_image(640 / 2, 480 / 2, image=photo)

        figure_canvas_agg = FigureCanvasAgg(fig)
        figure_canvas_agg.draw()

        tkagg.blit(photo, figure_canvas_agg.get_renderer()._renderer, colormode=2)
        # time.sleep(.1)

if __name__ == '__main__':
    main()