import pygame
from pygame.locals import *
import random 
colors={"Red":(255,27,150),"Yellow":(230,162,28),"Green":(0,20,0),"Black":(0,0,0),"White":(255,255,255)}
SIZE=20
class Food():
    def __init__(self,surface):
        self.surface=surface
        self.food_x=240
        self.food_y=240
    def draw_food(self):
        pygame.draw.rect(self.surface,colors["Red"],[self.food_x,self.food_y,20,20])
        pygame.display.flip()
    def move_food(self):
        self.food_x=random.randint(0,39)*SIZE
        self.food_y=random.randint(0,29)*SIZE 
class Snake():
    def __init__(self,surface,snake_len):
        self.screen=surface
        self.direction='down'
        self.snake_len = snake_len
        self.snake_x=[160]*snake_len
        self.snake_y=[200]*snake_len  
    def move_left(self):
        self.direction='left'
    def move_right(self):
        self.direction='right'
    def move_down(self):
        self.direction='down'
    def move_up(self):
        self.direction='up'
    def walk(self):
        for i in range (self.snake_len-1,0,-1):
           self.snake_x[i]=self.snake_x[i-1]
           self.snake_y[i]=self.snake_y[i-1]
        if self.direction=='up':
           self.snake_y[0]-= SIZE
        if self.direction=='down':
           self.snake_y[0]+= SIZE
        if self.direction=='left':
           self.snake_x[0]-= SIZE
        if self.direction=='right':
           self.snake_x[0]+= SIZE
        self.draw_snake()
    def draw_snake(self):
        self.screen.fill(colors["Green"])
        for i in range (self.snake_len):
           pygame.draw.rect(self.screen,colors["Yellow"],[self.snake_x[i],self.snake_y[i],20,20],5)
        pygame.display.flip()
    def snake_growth(self):
        self.snake_len+=1
        self.snake_x.append(-1)
        self.snake_y.append(-1)
class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((800,600))
        pygame.display.set_caption("Snake Game")
        self.surface.fill(colors["Green"])
        pygame.display.update()
        self.snake = Snake(self.surface,1)
        self.snake.draw_snake()
        self.food = Food(self.surface)
        self.food.draw_food()
    def game_instructions(self):
        self.surface.fill(colors["Green"])
        font_style=pygame.font.SysFont(None, 30)
        welcome_message=font_style.render("Welcome to Snake Game!", True, colors["Red"])
        self.surface.blit(welcome_message,[250,75])
        font_style2=pygame.font.SysFont(None, 25)
        i1= font_style2.render("-You are required to control the direction of the snake's head using the Arrow keys.", True, colors["Yellow"])
        i2=font_style2.render("-Each time the snake eats a piece of food it will grow.", True, colors["Yellow"])
        i3=font_style2.render("-The game is over when the snake runs into itself or hits the boundary.", True, colors["Yellow"])
        i4=font_style2.render("-Press p to Pause and Enter to continue", True, colors["Yellow"])
        i5=font_style2.render("-Press Escape to quit the game and Enter to play again when the game is over.", True, colors["Yellow"]) 
        self.surface.blit(i1, (50, 120))
        self.surface.blit(i2,(50,145))
        self.surface.blit(i3,(50,170))
        self.surface.blit(i4,(50,195))
        self.surface.blit(i5,(50,220))
        font_instruction = pygame.font.SysFont('Comic Sans Ms', 30)
        i6=font_instruction.render("PRESS ENTER TO START", True, colors["White"])
        i7=font_instruction.render("Enjoy!", True, colors["Red"])
        self.surface.blit(i6,(200,300))
        self.surface.blit(i7,(350,450))
        pygame.display.flip()
    def reset(self):
        self.snake = Snake(self.surface,1)
        self.apple = Food(self.surface)
    def is_collision(self,x1,x2,y1,y2):
        if x1>=x2 and x1<x2+SIZE:
            if y1>=y2 and y1<y2+SIZE:
                return True
        return False
    def display_score(self):
        font_style_score=pygame.font.SysFont(None,30)
        score=font_style_score.render(f"Score: {self.snake.snake_len-1}", True, colors["White"])
        self.surface.blit(score,[660,10]) 
    def game_over(self):
        self.surface.fill(colors["Black"])
        pygame.draw.rect(self.surface,colors["White"],[110,150,550,250],7)
        font_style=pygame.font.SysFont(None, 50)
        gameover_message=font_style.render("GAME OVER!", True, colors["Yellow"])
        self.surface.blit(gameover_message,[250,200])
        score= font_style.render(f"Score: {self.snake.snake_len-1}", True, colors["Yellow"])
        self.surface.blit(score, (300, 260))
        font_instruction = pygame.font.SysFont(None, 30)
        instruction= font_instruction.render("To play again press Enter. To exit press Escape!", True, colors["White"])
        self.surface.blit(instruction, (150, 300))
        pygame.display.flip()
    def game_paused(self):
        self.surface.fill(colors["Black"])
        pygame.draw.rect(self.surface,colors["White"],[110,150,575,250],7)
        font_style=pygame.font.SysFont(None, 50)
        gamepaused_message=font_style.render("GAME PAUSED!", True, colors["Yellow"])
        self.surface.blit(gamepaused_message,[230,200])
        score= font_style.render(f"Score: {self.snake.snake_len-1}", True, colors["Yellow"])
        self.surface.blit(score, (300, 260))
        font_instruction = pygame.font.SysFont(None, 30)
        instruction= font_instruction.render("To CONTINUE press ENTER. To QUIT press ESCAPE.", True, colors["White"])
        self.surface.blit(instruction, (150, 300))
        pygame.display.flip()
    def play(self):
        self.snake.walk()
        self.food.draw_food()
        self.display_score()
        pygame.display.update()
        if self.is_collision(self.snake.snake_x[0],self.food.food_x,self.snake.snake_y[0],self.food.food_y):
            self.snake.snake_growth()
            self.food.move_food()
        for i in range(2, self.snake.snake_len):
            if self.is_collision(self.snake.snake_x[0],self.snake.snake_x[i], self.snake.snake_y[0], self.snake.snake_y[i]):
                raise "Snake ran into itself"
        if not (0<=self.snake.snake_x[0]<800 and 0<=self.snake.snake_y[0]<600):
            raise "Collision at Boundary"
    def run(self):
        start=True
        running = True
        stop=False
        while start:
            self.game_instructions()
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key==K_RETURN:
                        start= False
                elif event.type == QUIT:
                    exit(0)
        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                    if event.key==K_RETURN:
                        stop = False
                    if not stop:
                        if event.key == K_LEFT:
                           self.snake.move_left()
                        if event.key == K_RIGHT:
                           self.snake.move_right()
                        if event.key == K_UP:
                           self.snake.move_up()
                        if event.key == K_DOWN:
                           self.snake.move_down()
                        if event.key == K_p:
                           self.game_paused()
                           stop=True
                elif event.type == QUIT:
                    running = False
            try:
                if not stop:
                    self.play()   
            except Exception as e:
                self.game_over()
                stop = True
                self.reset()
            game_speed=pygame.time.Clock()
            game_speed.tick(4)
game = Game()
game.run()