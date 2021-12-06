from turtle import Turtle

STARTING_POINT = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake(self):
        for position in STARTING_POINT:
            self.add_piece(position)

    def move_snake(self):
        for piece_num in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[piece_num - 1].xcor()
            new_y = self.snake_body[piece_num - 1].ycor()
            self.snake_body[piece_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def add_piece(self, position):
        """after eating food, snake gets longer"""
        new_piece = Turtle('square')
        new_piece.color('white')
        new_piece.penup()
        new_piece.goto(position)
        self.snake_body.append(new_piece)

    def extend(self):
        """add new piece of snake"""
        self.add_piece(self.snake_body[-1].position())


