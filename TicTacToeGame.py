def show():
    print("********TIC TAC TOE GAME********\n")
    print("\t 1 | 2 | 3 \n\t ---------- \n\t 4 | 5 | 6 \n\t ---------- \n\t 7 | 8 | 9 \n")


box=[" " for i in range(0,9)]
x=0
o=0
filled=0

def showGame():
      print(f"\t {box[0]} | {box[1]} | {box[2]} \n\t ---------- \n\t {box[3]} | {box[4]} | {box[5]}\n\t ---------- \n\t {box[6]} | {box[7]} | {box[8]} \n")
	  

def decide_winner(player1,player2):
    global x,o,filled
    win = [
        (0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)
    ]
    for a,b,c in win:
        if box[a]==box[b]==box[c]=='X':
            print(f"{player1} wins the game.")
            x += 1
            return 1
        if box[a]==box[b]==box[c]=='O':
            print(f"{player2} wins the game.")
            o += 1
            return 1
    if filled>=9:
        print("\nGame draw...")
        return -1
    return 0

def gameStart(player1,player2):
	print("\n")
	global filled
	c=""
	player='X'
	filled=0
	while filled<9:
		c=player1 if player=='X' else player2
		
		position=int(input(f"player {c} ({player}): enter the choice:"))
		
		if position>=1 and position<=9 and box[position-1]==' ':
			box[position-1]=player
			filled=filled+1
			showGame()
			player='O' if player=='X' else 'X'
			d=decide_winner(player1,player2);
			if(d==1 or d==-1):
				break
		else:
			print("\nenter the correct position\n")
		

def findHighestScore(player1, player2):
    if o>x:
        print(f"\n{player2} wins {o} times.")
    elif x>o:
        print(f"\n{player1} wins {x} times.")
    else:
        print(f"\nBoth players are tied with {x} wins each.")


if __name__=="__main__":
    player1=input("enter name(player1):")
    player2=input("enter name(player2):")

    while True:
        show()
        box=[" " for i in range(0,9)]
        choice=input("enter s to start and q to quit:")
        if choice.lower()=='s':
            gameStart(player1,player2)
        if choice.lower()=='q' :
            findHighestScore(player1,player2)
            exit(0)

