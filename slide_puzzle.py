import pygame, sys, random
from pygame.locals import *

WINDOWWIDTH=700
WINDOWHEIGHT=600
PUZZLEWIDTH=4

BLACK=(0,0,0)
WHITE=(255,255,255)
BLUE=(29,161,242)

def main():
	pygame.init()
	FPSCLOCK=pygame.time.Clock()
	DISPLAYSURF=pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT))
	DISPLAYSURF.fill(WHITE)
	BASICFONT = pygame.font.Font('freesansbold.ttf', 20)
	board=[]
	numbers=[]
	for i in range(15):
		numbers.append(i+1)
	numbers.append('')
	random.shuffle(numbers)
	for x in range(PUZZLEWIDTH):
		col=[]
		for y in range(PUZZLEWIDTH):
			col.append((x+1)+((PUZZLEWIDTH)*(y)))
		board.append(col)
	board[PUZZLEWIDTH-1][PUZZLEWIDTH-1]=''
	solved=[]
	solved=board
	i=0
	board=[]
	for x in range(PUZZLEWIDTH):
		col=[]
		for y in range(PUZZLEWIDTH):
			col.append(numbers[i])
			i=i+1
		board.append(col)
	random.shuffle(board)
	if board==solved:
		random.shuffle(board)
	z=0
	while True:
		if board==solved:
			z=1
			pygame.display.set_caption('Solved')
			text=BASICFONT.render(str('SOLVED!!!'),True,BLUE)
			textRect=text.get_rect()
			textRect.center=310,430
			DISPLAYSURF.blit(text,textRect)
		for x in range(PUZZLEWIDTH):
			for y in range(PUZZLEWIDTH):
				left=x*81+150
				top=y*81+80
				text=board[x][y]
				if text=='':
					pygame.draw.rect(DISPLAYSURF,BLUE,(left+1,top+1,80,80))
				else:
					pygame.draw.rect(DISPLAYSURF,BLACK,(left+1,top+1,80,80))					
				textSurf = BASICFONT.render(str(text), True, WHITE)
				textRect=textSurf.get_rect()
				textRect.center=left+40,top+40
				DISPLAYSURF.blit(textSurf,textRect)
		for event in pygame.event.get():
			if event.type==QUIT:
				pygame.quit()
				sys.exit()
			elif event.type==MOUSEBUTTONUP and z==0:
				posx,posy=event.pos
				for x in range(PUZZLEWIDTH):
					for y in range(PUZZLEWIDTH):
						left=x*81+150
						top=y*81+80
						boxrect=pygame.Rect(left+1,top+1,80,80)
						if boxrect.collidepoint(posx,posy):
							if x+1<PUZZLEWIDTH and y<PUZZLEWIDTH and board[x+1][y]=='' :
								board[x+1][y]=board[x][y]
								board[x][y]=''
							elif x<PUZZLEWIDTH and y+1<PUZZLEWIDTH and board[x][y+1]=='':
								board[x][y+1]=board[x][y]
								board[x][y]=''
							elif x-1>=0 and y<PUZZLEWIDTH and board[x-1][y]=='':
								board[x-1][y]=board[x][y]
								board[x][y]=''
							elif x<PUZZLEWIDTH and y-1>=0 and board[x][y-1]=='':
								board[x][y-1]=board[x][y]
								board[x][y]=''
						
		pygame.display.update()
		FPSCLOCK.tick(30)

if __name__ == '__main__':
    main()