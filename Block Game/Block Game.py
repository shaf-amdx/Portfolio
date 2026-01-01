import keyboard as kb
import random as rdm
blocks=["|","||","|||","||||"]
pos={'A':[".",".",".",".",".",".",".",".",".","."],"B":[".",".",".",".",".",".",".",".",".","."],"C":[".",".",".",".",".",".",".",".",".","."],"D":[".",".",".",".",".",".",".",".",".","."],"E":[".",".",".",".",".",".",".",".",".","."],"F":[".",".",".",".",".",".",".",".",".","."],"G":[".",".",".",".",".",".",".",".",".","."],"H":[".",".",".",".",".",".",".",".",".","."],"I":[".",".",".",".",".",".",".",".",".","."],"J":[".",".",".",".",".",".",".",".",".","."]}
def plane(pos,block,x):
    print(f"""
{"  "*x+"| ".join(block.split("|")).strip()}""")
    print(f"""
{pos.get('A')[0]} {pos.get('A')[1]} {pos.get('A')[2]} {pos.get('A')[3]} {pos.get('A')[4]} {pos.get('A')[5]} {pos.get('A')[6]} {pos.get('A')[7]} {pos.get('A')[8]} {pos.get('A')[9]}
{pos.get('B')[0]} {pos.get('B')[1]} {pos.get('B')[2]} {pos.get('B')[3]} {pos.get('B')[4]} {pos.get('B')[5]} {pos.get('B')[6]} {pos.get('B')[7]} {pos.get('B')[8]} {pos.get('B')[9]}
{pos.get('C')[0]} {pos.get('C')[1]} {pos.get('C')[2]} {pos.get('C')[3]} {pos.get('C')[4]} {pos.get('C')[5]} {pos.get('C')[6]} {pos.get('C')[7]} {pos.get('C')[8]} {pos.get('C')[9]}
{pos.get('D')[0]} {pos.get('D')[1]} {pos.get('D')[2]} {pos.get('D')[3]} {pos.get('D')[4]} {pos.get('D')[5]} {pos.get('D')[6]} {pos.get('D')[7]} {pos.get('D')[8]} {pos.get('D')[9]}
{pos.get('E')[0]} {pos.get('E')[1]} {pos.get('E')[2]} {pos.get('E')[3]} {pos.get('E')[4]} {pos.get('E')[5]} {pos.get('E')[6]} {pos.get('E')[7]} {pos.get('E')[8]} {pos.get('E')[9]}
{pos.get('F')[0]} {pos.get('F')[1]} {pos.get('F')[2]} {pos.get('F')[3]} {pos.get('F')[4]} {pos.get('F')[5]} {pos.get('F')[6]} {pos.get('F')[7]} {pos.get('F')[8]} {pos.get('F')[9]}
{pos.get('G')[0]} {pos.get('G')[1]} {pos.get('G')[2]} {pos.get('G')[3]} {pos.get('G')[4]} {pos.get('G')[5]} {pos.get('G')[6]} {pos.get('G')[7]} {pos.get('G')[8]} {pos.get('G')[9]}
{pos.get('H')[0]} {pos.get('H')[1]} {pos.get('H')[2]} {pos.get('H')[3]} {pos.get('H')[4]} {pos.get('H')[5]} {pos.get('H')[6]} {pos.get('H')[7]} {pos.get('H')[8]} {pos.get('H')[9]}
{pos.get('I')[0]} {pos.get('I')[1]} {pos.get('I')[2]} {pos.get('I')[3]} {pos.get('I')[4]} {pos.get('I')[5]} {pos.get('I')[6]} {pos.get('I')[7]} {pos.get('I')[8]} {pos.get('I')[9]}
{pos.get('J')[0]} {pos.get('J')[1]} {pos.get('J')[2]} {pos.get('J')[3]} {pos.get('J')[4]} {pos.get('J')[5]} {pos.get('J')[6]} {pos.get('J')[7]} {pos.get('J')[8]} {pos.get('J')[9]}
""")
def move(temp_pos,direction):
    if direction=="r":
        if (temp_pos["bs"]+temp_pos["bl"])<10:
            temp_pos["bs"]=temp_pos["bs"]+1
        else:
            print("Cant move further right!")
    elif direction=="l":
        if temp_pos["bs"]>0:
            temp_pos["bs"]=temp_pos["bs"]-1
        else:
            print("Cant move further left!")
    return temp_pos
def game():
    print("Hi there!")
    Score=0
    plane(pos,"",0)
    try:
        while True:
            block=rdm.choice(blocks)
            temp_pos={"bs":0,"bl":len(block)}
            plane(pos,block,0)
            while True:
                event=kb.read_event()
                if event.event_type=="up":#Skips key release event
                    continue
                Placed_row=None
                Placed_row_index=None
                if event.name in "aA":#moving the block leftwards
                    temp_pos=move(temp_pos,"l")
                    plane(pos,block,temp_pos['bs'])
                elif event.name in "dD":#moving the block rightwards
                    temp_pos=move(temp_pos,"r")
                    plane(pos,block,temp_pos['bs'])
                elif event.name in "sS":#releasing the block downwards
                    for i in "ABCDEFGHIJ":#Collision check
                        for j in range(temp_pos['bs'],temp_pos['bs']+temp_pos['bl']):
                            if (pos.get(i))[j]=="|":
                                Placed_row_index="ABCDEFGHIJ".find(i)-1
                                Placed_row="ABCDEFGHIJ"[Placed_row_index]
                                Score+=len(block)
                                break
                        else:
                            continue
                        break
                    if Placed_row_index==-1:#check to ensure if a collision occurred in the top block
                        raise Exception#Game over
                    elif Placed_row==None:
                        Placed_row='J'
                    for i in range(temp_pos['bs'],temp_pos['bs']+temp_pos['bl']):#Block placement
                        (pos[Placed_row])[i]="|"
                    plane(pos,block,temp_pos['bs'])
                    break
    except Exception:
        print(f"""
        Game Over!
        Score : {Score}""")
        return
game()
