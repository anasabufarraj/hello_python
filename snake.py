#!./venv/bin/python3.7
# Copyright 2019. Anas Abu Farraj

import tkinter as tk
from random import randint
from PIL import Image, ImageTk  # Pillow: Python Imaging Library

PLAYGROUND_WIDTH = 600
PLAYGROUND_HEIGHT = 620

MOVE_INCREMENT = 20
MOVE_PER_SECOND = 12
GAME_SPEED = 1000 // MOVE_PER_SECOND


class Snake(tk.Canvas):
    def __init__(self):
        super().__init__(width=PLAYGROUND_WIDTH, height=PLAYGROUND_HEIGHT, background='black', highlightthickness=0)

        self.snake_positions = [(100, 100), (80, 100), (60, 100)]
        self.food_position = self.set_new_food_position()
        self.direction = 'Right'
        self.score = 0

        self.load_assets()
        self.create_objects()

        self.bind_all('<Key>', self.on_key_press)
        self.pack()

        self.after(GAME_SPEED, self.perform_actions)

    def load_assets(self):
        try:
            self.snake_body_image = Image.open('./assets/snake.png')
            self.snake_body = ImageTk.PhotoImage(self.snake_body_image)

            self.food_image = Image.open('./assets/food.png')
            self.food = ImageTk.PhotoImage(self.food_image)

        except IOError as error:
            print(error)
            root.destroy()

    def create_objects(self):
        self.create_text(35, 12, text=f'Score: {self.score}', tag='score', fill='#fff', font=14)

        for x_position, y_position in self.snake_positions:
            self.create_image(x_position, y_position, image=self.snake_body, tag='snake')

        self.create_image(*self.food_position, image=self.food, tag='food')
        self.create_rectangle(0, 27, PLAYGROUND_WIDTH, PLAYGROUND_HEIGHT, outline='#000')

    def check_collisions(self):
        head_x_position, head_y_position = self.snake_positions[0]

        return (head_x_position in (0, PLAYGROUND_WIDTH) or head_y_position in (20, PLAYGROUND_HEIGHT)
                or (head_x_position, head_y_position) in self.snake_positions[1:])

    def check_food_collision(self):
        if self.snake_positions[0] == self.food_position:
            self.score += 1
            self.snake_positions.append(self.snake_positions[-1])

            self.create_image(*self.snake_positions[-1], image=self.snake_body, tag='snake')
            self.food_position = self.set_new_food_position()
            self.coords(self.find_withtag('food'), *self.food_position)

            score = self.find_withtag('score')
            self.itemconfigure(score, text=f'Score: {self.score}', tag='score')

    def end_game(self):
        self.delete(tk.ALL)
        self.create_text(self.winfo_width() / 2,
                         self.winfo_height() / 2.3,
                         text=f'Game Over',
                         fill='#ffd278',
                         font=('TkDefaultFont', 35))
        self.create_text(self.winfo_width() / 2,
                         self.winfo_height() / 2,
                         text=f'You scored is {self.score}',
                         fill='#fff',
                         font=('TkDefaultFont', 22))

    def move_snake(self):
        head_x_position, head_y_position = self.snake_positions[0]

        if self.direction == 'Left':
            new_head_position = (head_x_position - MOVE_INCREMENT, head_y_position)
        elif self.direction == 'Right':
            new_head_position = (head_x_position + MOVE_INCREMENT, head_y_position)
        elif self.direction == 'Down':
            new_head_position = (head_x_position, head_y_position + MOVE_INCREMENT)
        elif self.direction == 'Up':
            new_head_position = (head_x_position, head_y_position - MOVE_INCREMENT)

        self.snake_positions = [new_head_position] + self.snake_positions[:-1]

        for segment, position in zip(self.find_withtag('snake'), self.snake_positions):
            self.coords(segment, position)

    def on_key_press(self, e):
        new_direction = e.keysym

        all_directions = ('Up', 'Down', 'Left', 'Right')
        opposites = ({'Up', 'Down'}, {'Left', 'Right'})

        if new_direction in all_directions and {new_direction, self.direction} not in opposites:
            self.direction = new_direction

    def perform_actions(self):
        if self.check_collisions():
            self.end_game()

        self.check_food_collision()
        self.move_snake()

        self.after(GAME_SPEED, self.perform_actions)

    def set_new_food_position(self):
        while True:
            x_position = randint(1, 29) * MOVE_INCREMENT
            y_position = randint(3, 30) * MOVE_INCREMENT
            food_position = (x_position, y_position)

            if food_position not in self.snake_positions:
                return food_position


# Creating main application window
root = tk.Tk()
root.title('Snake Game')  # Window title
root.resizable(False, False)  # Freeze window size
root.geometry('+870+0')  # Offset window

# Creating playground for snake
playground = Snake()
playground.pack()

root.mainloop()  # Application run