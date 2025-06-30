from turtle import Turtle
import random
class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5)
        self.color("red")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        randomx=random.randint(-270,270)
        random_y=random.randint(-270,270)
        self.goto(randomx,random_y)
