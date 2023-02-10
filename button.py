import pygame, sys
from style import *

def get_font(size): 
    return pygame.font.Font("assets/Unique.ttf", size)

class Button:
    def __init__(self, text_input, window, width, height, pos, elevation, onclickFunction):
        #attribute 
        self.text = text_input

        self.window = window
        self.pressed = False
        self.elevation = elevation
        self.dynamic_elevation = elevation
        self.original_y_pos = pos[1]

        self.onclickFunction = onclickFunction
        
        #top rectangle 
        self.top_rect = pygame.Rect(pos,(width,height)) #Pos corresppond top top left corner 
        self.top_color =  main_color

        #bottom rectangle
        self.bottom_rect = pygame.Rect(pos,(width,elevation))
        self.bottom_color = sub_color

        #Text
        gui_font = get_font(30)
        self.text_surf = gui_font.render(text_input,True,font_color)
        self.text_rect = self.text_surf.get_rect(center = self.top_rect.center)

    def draw(self):
        # elevation logic 
        self.top_rect.y = self.original_y_pos - self.dynamic_elevation
        self.text_rect.center = self.top_rect.center

        self.bottom_rect.midtop = self.top_rect.midtop
        self.bottom_rect.height = self.top_rect.height + self.dynamic_elevation

        pygame.draw.rect(self.window,self.bottom_color,self.bottom_rect,border_radius=12)
        pygame.draw.rect(self.window,self.top_color,self.top_rect,border_radius= 12)
        self.window.blit(self.text_surf, self.text_rect)
        self.check_click()

    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.top_rect.collidepoint(mouse_pos):
            self.top_color = hover_color  
            if pygame.mouse.get_pressed()[0]:   # By default tuple of 3 elements (each click)
                self.dynamic_elevation = 0
                self.pressed = True
            else:
                self.dynamic_elevation = self.elevation
                if self.pressed == True:    #.pressed is here to prevent from having multiples clicks
                    print("test")
                    self.onclickFunction
                    print(self.onclickFunction)
                    self.pressed = False
        else:
            self.dynamic_elevation = self.elevation
            self.top_color = "#475F77"
        
    def test():
        print('bruh')



# class Button():   
# 	def __init__(self, image, pos, text_input):
# 		self.image = image
# 		self.x_pos = pos[0]
# 		self.y_pos = pos[1]
# 		self.font = get_font(30)
# 		self.text_input = text_input
# 		self.text = self.font.render(self.text_input, True, font_color)
# 		if self.image is None:
# 			self.image = self.text
# 		self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
# 		self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

# 	def update(self, screen):
# 		if self.image is not None:
# 			screen.blit(self.image, self.rect)
# 		screen.blit(self.text, self.text_rect)

# 	def checkForInput(self, position):
# 		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
# 			return True
# 		return False

# 	def changeColor(self, position):
# 		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
# 			self.text = self.font.render(self.text_input, True, hover_color)
# 		else:
# 			self.text = self.font.render(self.text_input, True, main_color)

