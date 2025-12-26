def plane(ABC123):
    print(f"""
     A         B         C
1    {ABC123.get("A1")}    |    {ABC123.get("B1")}    |    {ABC123.get("C1")}
 ---------+---------+---------
2    {ABC123.get("A2")}    |    {ABC123.get("B2")}    |    {ABC123.get("C2")}
 ---------+---------+---------
3    {ABC123.get("A3")}    |    {ABC123.get("B3")}    |    {ABC123.get("C3")}   """)
import random
player_positions=[]
bot_positions=[]
ABC123={"A1":" ","A2":" ","A3":" ","B1":" ","B2":" ","B3":" ","C1":" ","C2":" ","C3":" "}
possible_wins=[["A1","A2","A3"],["B1","B2","B3"],["C1","C2","C3"],["A1","B2","C3"],["C1","B2","A3"],["A1","B1","C1"],["A2","B2","C2"],["A3","B3","C3"]]
player_role=" "
Bot_Role=" "
def player_play():
    while True:
        player_pos=input("Enter your position : ").strip().upper()
        player_pos=player_pos.replace(" ","")
        try:
            if player_pos not in list(ABC123.keys()):
                raise ValueError
            if (player_pos in player_positions) or (player_pos in bot_positions):
                raise Exception
            ABC123[player_pos]=player_role
        except ValueError:
            print("INVALID INPUT!")
        except Exception:
            print("POSITION IS OCCUPIED!")
        else:
            player_positions.append(player_pos)
            break
def bot_play():
    while True:
        Last_key=False
        Algorithm_Used=False
        for i in possible_wins:
            for _ in range(3):
                if (i[0] in bot_positions and i[1] in bot_positions) and (i[2] not in bot_positions and i[2] not in player_positions):
                    bot_pos=i[2]
                    Algorithm_Used=True
                    break
                i.append(i.pop(0))
            if Algorithm_Used:
                bot_positions.append(bot_pos)
                ABC123[bot_pos]=Bot_Role
        if Algorithm_Used:
            break
        for i in possible_wins:
            for _ in range(3):
                if (i[0] in player_positions and i[1] in player_positions) and (i[2] not in bot_positions and i[2] not in player_positions):
                    bot_pos=i[2]
                    Algorithm_Used=True
                    break
                i.append(i.pop(0))
            if Algorithm_Used:
                bot_positions.append(bot_pos)
                ABC123[bot_pos]=Bot_Role
                break
        if Algorithm_Used:
            break
        while not Algorithm_Used:
            num=random.randint(1,3)
            alpha=random.randint(1,3)
            bot_pos=chr(64+alpha)+str(num)
            if not ((bot_pos in player_positions) or (bot_pos in bot_positions)):
                break
        if list(ABC123.values()).count(" ")==1:
            for k in list(ABC123.keys()):
                if ABC123.get(k)==" ":
                    ABC123[k]=Bot_Role
                    Last_key=True
                    break
        if Last_key:
            break
        else:
            ABC123[bot_pos]=Bot_Role
            bot_positions.append(bot_pos)
            break
def status_check():
    for i in possible_wins:
        if (i[0] in player_positions) and (i[1] in player_positions) and (i[2] in player_positions):
            return ("Game Over!","You Won!")
        elif (i[0] in bot_positions) and (i[1] in bot_positions) and (i[2] in bot_positions):
            return ("Game Over!","Bot Won!")
    if (len(bot_positions)+len(player_positions))==9:
        return ("Game Over","Its a tie")
    return ("Game Not over!","")
def game():
    global player_role,Bot_Role,player_positions,bot_positions,ABC123,possible_wins
    player_positions=[]
    bot_positions=[]
    ABC123={"A1":" ","A2":" ","A3":" ","B1":" ","B2":" ","B3":" ","C1":" ","C2":" ","C3":" "}
    possible_wins=[["A1","A2","A3"],["B1","B2","B3"],["C1","C2","C3"],["A1","B2","C3"],["C1","B2","A3"],["A1","B1","C1"],["A2","B2","C2"],["A3","B3","C3"]]
    player_role=" "
    Bot_Role=" "
    while True:
        player_role=input("Which role would you like to play ? X/O ").strip().upper()
        if player_role=="X":
            Bot_Role="O"
            break
        elif player_role=="O":
            Bot_Role="X"
            break
        else:
            print("INVALID INPUT!")
    while True:
        Start_Decision=input("Would you like to start the game ? Yes/No ").strip().upper()
        if Start_Decision[0]=="Y":
            while True:
                plane(ABC123)
                player_play()
                status,game_status=status_check()
                if status=="Game Over!":
                    plane(ABC123)
                    print("\n"+game_status+"\n")
                    break
                bot_play()
                status,game_status=status_check()
                if status=="Game Over!":
                    plane(ABC123)
                    print("\n"+game_status+"\n")   
                    break
        else:
            while True:
                bot_play()
                plane(ABC123)
                status,game_status=status_check()
                if status=="Game Over!":
                    print("\n"+game_status+"\n")
                    break
                player_play()
                status,game_status=status_check()
                if status=="Game Over!":
                    plane(ABC123)
                    print("\n"+game_status+"\n")
                    break
        break
while True:
    game()
    Decision=input("Would you like to play again ? Yes/No ").strip().upper()
    if Decision[0]=="Y":
        continue
    else:
        print("Game Over!")
        break
