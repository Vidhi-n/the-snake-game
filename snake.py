from turtle import Turtle
STARTINGPOSITIONS=[(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE=20
UP=90
DOWN=270
LEFT=180
RIGHT=0
class Snake:

    def __init__(self):
        self.segments=[]
        self.createsnake()
        self.head=self.segments[0]


    

    def createsnake(self):
        for positions in STARTINGPOSITIONS:
            new_segment=Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(positions)
            self.segments.append(new_segment)

    def extend(self,pos):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(pos)
        self.segments.append(new_segment)

    
    
    def move(self):
        for seg_num in range(len(self.segments)-1,0,-1):
            xc=self.segments[seg_num-1].xcor()        
            yc=self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(xc,yc)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading()!=DOWN:
            self.head.setheading(UP)
    def left(self):
        if self.head.heading()!=RIGHT:
            self.head.setheading(LEFT)
    def down(self):
        if self.head.heading()!=UP:
            self.head.setheading(DOWN)
    def right(self):
        if self.head.heading()!=LEFT:
            self.head.setheading(RIGHT)


    