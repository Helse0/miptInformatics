from random import randint
from tkinter import ttk
from tkinter import  *

WIDTH = 1000
HEIGHT = 700


class Ball:
    def __init__(self, h, w):
        self.R = randint(10, 50) #храним размер, при каждом создании объекта будет выбираться случайно
        self.x = randint(self.R, w - self.R) # храним положение по x и y
        self.y = randint(self.R, h - self.R)
        self.dx, self.dy = (randint(10, 50), randint(10, 50)) # это по сути шаг движения шаров. если увеличить -- будут двигаться быстрее
        self.ball_id = canvas.create_oval(self.x - self.R,
                                     self.y - self.R,
                                     self.x + self.R,
                                     self.y + self.R, fill="green") # при создании шарика отрисовываем его

    def move(self):
        self.x += self.dx
        self.y += self.dy
        if self.x + self.R > root.winfo_width() or self.x - self.R <= 0: # отражение от стенок
            self.dx = -self.dx
        if self.y + self.R > root.winfo_height() or self.y - self.R <= 0: # отр
            self.dy = -self.dy

    def show(self):
        canvas.move(self.ball_id, self.dx, self.dy)


#здесь мы уже привычно обращаемся к balls как к глобальной переменной. На самом деле дело в том, что нам лень писать классы.
def tick():
    for ball in balls:
        ball.move()
        ball.show()
    root.after(50, tick)


root = Tk()
root.geometry(f'{WIDTH}x{HEIGHT}')

canvas = Canvas(root)
canvas.config(height=HEIGHT,  width=WIDTH)
canvas.pack()

balls = [Ball(HEIGHT, WIDTH) for i in range(10**3)]
# делаем шаг перемещения и отрисовки шаров. поскольку mainloop циклит наше приложение, это будет происходить, пока мы не закроем окно
tick()
root.mainloop()