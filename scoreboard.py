from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Verdana', 24, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open('data.txt') as file:
            self.highest_score = int(file.read())
        self.hideturtle()
        self.color('white')
        self.penup()
        self.goto(x = 0, y = 260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}    Highest score:  {self.highest_score}",
                   align = ALIGNMENT, font = FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.highest_score:
            self.highest_score = self.score
            with open('data.txt', mode = 'w') as file:
                file.write(f"{self.highest_score}")
        self.score = 0
        self.update_scoreboard()


    # def game_over(self):
    #     self.goto(0, 0)
    #     self.color('red')
    #     self.write("GAME OVER", align = ALIGNMENT, font = FONT)


