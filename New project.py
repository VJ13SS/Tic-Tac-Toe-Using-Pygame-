#Hey all tbis is a simple demonstration of the Tic Tac Toe Game created using Pygame module in python
#This code is designed for those who are new to this module and who had just stepped from the CLI interfaces to explore for more
#I do belive that this code provided here wipl give you a brief introduction about pygame module and its work flow .Feel happy to explore

#Note: The points taken here are static and is based on my window screen...Adjust them for yours

#This is not the final version but just a base for model and so many cool features can be added...Happy to add yours...
#I will surely work upon them....VJ 13 SS

import pygame

#initialization
pygame.init()

#constants
WIDTH, HEIGHT = 2500, 2200
BG_COLOR = (0, 20,40)

LABEL_FONT = pygame.font.SysFont('comicsans',100)#Comicsans font of size 100

#screen setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))

#Constants
ROWS = 3
COLS = 3

#initializing board
board = [['' for _ in range(COLS)] for _ in range(ROWS)]

def draw_square(screen):
	board_start_x = 200
	board_start_y = 600
	SIDE = 800
	pygame.draw.rect(screen, 'white', (board_start_x,board_start_y,SIDE,SIDE))
	
	#Vertical lines
	for i in range(1,COLS):
		x = board_start_x + (SIDE  * (i/3))
		y1 = board_start_y 
		y2 = y1 + SIDE
		pygame.draw.line(screen, 'black' , (x, y1), (x, y2), 5)
		
	#Horizontal lines
	for j in range(1,ROWS):
			y = board_start_y + (SIDE  * (j/3))
			x1 = board_start_x
			x2 = x1 + SIDE
			
			pygame.draw.line(screen, 'black', (x1, y), (x2, y), 5)
		
	pygame.display.update()

def draw_player(mouse_x,mouse_y,PLAYER):
	
	SIDE = 800
	board_start_x = 200
	board_start_y = 600
	
	#Ensures that markers are drawn only at the board
	for i in range(0,ROWS):
		for j in range(0,COLS):
			x1= board_start_x + (SIDE  * (i/3))
			y1 = board_start_y + (SIDE  * (j/3))
			x2= board_start_x + (SIDE  *((i+1)/3)) - 50 #padding of 50 for adjustment
			y2 = board_start_y + (SIDE  * ((j+1)/3)) - 60 #padding of 60 for adjustment
			
			#Coodinates to draw the marker at the centre of each cell
			mid_x = (x1 + x2)/2
			mid_y = (y1 + y2)/2
			
			if x1 <= mouse_x <= x2 and y1 <= mouse_y <= y2 and board[i][j] == '':
				
				#Update board
				board[i][j] = PLAYER
				
				
				#Draw Player
				text_label = LABEL_FONT.render(PLAYER,1, 'red')
				screen.blit(text_label,(mid_x,mid_y))
				break
	pygame.display.update()

def check_winner(board):
		#To check horizontally
		for i in range(ROWS):
			if board[i][0] != '':
				if board[i][0] == board[i][1] and board[i][0] == board[i][2]:
					return True
					
		for j in range(COLS):
			if board[0][j] != '':
				if board[0][j] == board[1][j] and board[0][j] == board[2][j]:
					return True
		if board[0][0] != '' and board[0][0] == board[1][1] == board[2][2]:
			return True
		if board[0][2] != '' and board[0][2] == board[1][1] and  board[0][2] == board[2][0]:
			return True
		
		draw = all(cell !='' for row in board for cell in row)
		if draw:
			return 'draw'
		
		return False
		
def draw_winner(result,PLAYER):
		pygame.draw.rect(screen, 'white', (200,1500,800,100))
		if result == 'draw':
				text = "IT'S A DRAW"
				text_label = LABEL_FONT.render(text,1, 'red')
				screen.blit(text_label,(300,1530))
	
		elif result == True:
				text = PLAYER
				text_label = LABEL_FONT.render(f'PLAYER {PLAYER} WINS',1, 'red')
				screen.blit(text_label,(300,1530))
		pygame.display.update()
	
				
def main():
	PLAYER = 'O'
	screen.fill(BG_COLOR)
	draw_square(screen)
	run = True
	while run:
		
		mouse_x,mouse_y = pygame.mouse.get_pos()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quit()
			
			if event.type == pygame.MOUSEBUTTONDOWN:
				
				#To display the current player
				pygame.draw.rect(screen, 'white', (200,380,850,100))
				text_label = LABEL_FONT.render(f'PLAYER : {PLAYER} HAS PLAYED',1, 'red')
				screen.blit(text_label,(200,400))
				
							
				#To draw the current player
				
				draw_player(mouse_x,mouse_y,PLAYER)
			
				result = check_winner(board)
				
				if result != False:
					while True:
						draw_winner(result,PLAYER)
					
			if  PLAYER == 'O':
				PLAYER = 'X'
			else:
				PLAYER = 'O'
				
		
			#Update the display
		pygame.display.update()
	
if __name__ == '__main__':
	main()