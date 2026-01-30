import random as rdm
import time
import keyboard as kb
import os
board=dict()
for y in 'ABCDEFGHI':
    for x in (list('123456789')):
        board[y+x]=' '
def plane(board):
    print('|','- '*9,'\b|')
    for y in 'ABCDEFGHI':
        print('|',end=' ')
        for x in (list('123456789')):
            print((board.get(y+x))[0],end=' ')
        print('|',end='\n')
    print('|','- '*9,'\b|')
def food(snake_pos):
    food=[]
    for i in 'ABCDEFGHI':
        for j in "123456789":
            food.append(i+j)
    for i in snake_pos:
        food.remove(i)
    return rdm.choice(food)
def add_size(board,snake_cord,dir):
    try:
        if snake_cord[-1][0]==snake_cord[-2][0]:
            sign=int(snake_cord[-1][1])-int(snake_cord[-2][1])
            if sign in range(1,8) or sign==-8:
                dir='a'
            else:
                dir='d'
        else:
            sign=ord(snake_cord[-1][0])-ord(snake_cord[-2][0])
            if sign in range(1,8) or sign==-8:
                dir='w'
            else:
                dir='s'
    except:
        pass
    if dir=='w':
        if (snake_cord[-1])[0]=='I':
            oprtn='ord(alpha)-8'
        else:
            oprtn='ord(alpha)+1'
    elif dir=='s':
        if (snake_cord[-1])[0]=='A':
            oprtn='ord(alpha)+8'
        else:
            oprtn='ord(alpha)-1'
    elif dir=='d':
        if (snake_cord[-1])[1]=='1':
            oprtn='ord(num)+8'
        else:
                oprtn='ord(num)-1'
    elif dir=='a':
        if (snake_cord[-1])[1]=='9':
            oprtn='ord(num)-8'
        else:
            oprtn='ord(num)+1'
    new_part=eval(oprtn.replace('num',f'"{snake_cord[-1][1]}"').replace('alpha',f'"{snake_cord[-1][0]}"'))
    new_part=(snake_cord[-1][0]+chr(new_part)) if new_part in range(49,58) else (chr(new_part)+snake_cord[-1][1])
    if board[new_part] in 'Oo':
        return board,'game over'
    snake_cord.append(new_part)
    board[new_part]='o'
    return board,snake_cord
def move(snake_cord,board,dir):
    if dir=='w':
        if (snake_cord[0])[0]=='A':
            oprtn='ord(alpha)+8'
        else:
            oprtn='ord(alpha)-1'
    elif dir=='s':
        if (snake_cord[0])[0]=='I':
            oprtn='ord(alpha)-8'
        else:
            oprtn='ord(alpha)+1'
    elif dir=='d':
        if (snake_cord[0])[1]=='9':
            oprtn='ord(num)-8'
        else:
            oprtn='ord(num)+1'
    elif dir=='a':
        if (snake_cord[0])[1]=='1':
            oprtn='ord(num)+8'
        else:
            oprtn='ord(num)-1'
    head=snake_cord[0]
    new_pos=eval(oprtn.replace('num',f'"{head[1]}"').replace('alpha',f'"{head[0]}"'))
    new_pos=(head[0]+chr(new_pos))if new_pos in range(49,58) else (chr(new_pos)+head[1])
    if board[new_pos] in 'Oo':
        return 'game over',board
    else:
        snake_cord.insert(0,new_pos)
        old_pos=snake_cord.pop()
        board[old_pos]=' '
        board[new_pos]='O'
        try:
            board[snake_cord[1]]='o'
        except:
            pass
        return snake_cord,board
def game(board):
    score=0
    snake_cord=[rdm.choice(list('ABCDEFGHI'))+rdm.choice(list('123456789'))]
    direction=rdm.choice(['w','s','d','a'])
    food_pos=food(snake_cord)
    board[food_pos]='.'
    board[snake_cord[0]]='O'
    plane(board)
    while True:
        if kb.is_pressed('w'):
            if direction=='s':
                pass
            else:
                direction='w'
        elif kb.is_pressed('s'):
            if direction=='w':
                pass
            else:
                direction='s'
        elif kb.is_pressed('a'):
            if direction=='d':
                pass
            else:
                direction='a'
        elif kb.is_pressed('d'):
            if direction=='a':
                pass
            else:
                direction='d'
        snake_cord,board=move(snake_cord,board,direction)
        if snake_cord=='game over':
            plane(board)
            return score
        if snake_cord[0]==food_pos:
            board,snake_cord=add_size(board,snake_cord,direction)
            score+=1
            if snake_cord=='game over':
                return score
            food_pos=food(snake_cord)
            board[food_pos]='.'
        plane(board)
        time.sleep(0.2)
        os.system('cls' if os.name == 'nt' else 'clear')
score=game(board)
print('Game Over!',' ,Score: ',score)
