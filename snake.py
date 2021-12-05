from turtle import Turtle

STARTING_POINT = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake():

    def __init__(self):
        self.snake_body = []
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POINT:
            new_piece = Turtle('square')
            new_piece.color('white')
            new_piece.penup()
            new_piece.goto(position)
            self.snake_body.append(new_piece)

    def move_snake(self):
        for piece_num in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[piece_num - 1].xcor()
            new_y = self.snake_body[piece_num - 1].ycor()
            self.snake_body[piece_num].goto(new_x, new_y)
        self.snake_body[0].forward(MOVE_DISTANCE)
