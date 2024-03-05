from tkinter import *

CANVAS_WIDTH, CANVAS_HEIGHT = 600, 400

if __name__ == '__main__':
    root = Tk()

    canvas = Canvas(root, width = CANVAS_WIDTH, height = CANVAS_HEIGHT)

    # Début de votre code
    x0 = CANVAS_WIDTH/2
    y1 = CANVAS_HEIGHT - 100
    y0=100
    canvas.create_line(x0,y0,x0,y1)
    canvas.create_oval(x0 - 50, y0 + 50, x0 + 50, y0 - 50)
    canvas.create_oval(x0 - 50, y1 + 50, x0 + 50, y1 - 50)
    canvas.create_oval(x0 - 50, (y1+y0)/2-50, x0+50, (y1+y0)/2 + 50)
    
    # Fin de votre code

    canvas.pack()
    root.mainloop()
