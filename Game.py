import random
while 1:
    user = input("Enter the choice:'r' for Rock, 's' for scissors and 'p' for Paper: ")
    computer = random.choice(['r','p','s'])
    if user not in ['r','p','s']:
        print("Oops. You Accidently choosen another option please choose among 'rock,paper,scissors'")
    if user == computer:
        print(f"\nUser {user} VS Computer {computer}:",end = " ")
        print("\nIt's a tie. Try Again")
    else:
        '''There are only 3 possiblities that one can win in this game 
        1.scissor vs paper
        2.paper vs rock
        3.rock vs scissor'''
    
        if((user == 'r' and computer == 's') or (user == 'p' and computer == 'r') or (user == 's' and computer == 'p')):
            print(f"\nUser {user} VS Computer {computer}:", end = " ")
            print("\nYeah!, You Won")
        else:
            print(f"\nUser {user} VS Computer {computer}:", end = " ")
            print("\nOoops!,You Lost")