import tkinter as tk
import tkinter.ttk as ttk
import random
import time
from threading import Thread


class FractalDisplay(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("The Fractal")
        self.geometry('1200x1000')

        self.resolution = 100
        self.the_grid_canvas = tk.Canvas(self)
        self.the_grid_canvas.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

        self.the_image = None
        self.max_steps = 100

        t = Thread(target=self.draw_fractal, daemon=True)
        t.start()

    def draw_fractal(self):
        a_bitmap = [[[0, 0, 0] for _ in range(2 * self.resolution)] for _ in range(2 * self.resolution)]
        self.the_image = tk.PhotoImage(width=2 * self.resolution, height=2 * self.resolution)
        offset = complex(-.75, .14)
        for i in range(-self.resolution, self.resolution):
            print(i)
            for j in range(-self.resolution, self.resolution):
                c = complex(i/self.resolution, j/self.resolution)
                num_steps = 0
                while abs(c) < 10 and num_steps < self.max_steps:
                    num_steps += 1
                    c = c**2 + offset
                if num_steps == self.max_steps:
                    a_bitmap[i + self.resolution][j + self.resolution] = [0, 0, 255]
        for i in range(2 * self.resolution):
            for j in range(2 * self.resolution):
                self.the_image.put('#%02x%02x%02x' % tuple(a_bitmap[i][j]), (i, j))
        self.the_grid_canvas.create_image(0, 0, image=self.the_image, anchor=tk.NW)


if __name__ == "__main__":
    fractal_window = FractalDisplay()
    fractal_window.mainloop()