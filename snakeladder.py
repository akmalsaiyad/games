from os import system
import random

global score
def display():
    system('cls')
    print('''
    -----------------
    | Playing Board |
    -----------------
    position >>>>> snake/ladder >>>>> position                          
        3   ->->->-> ladder ->->->->  51                     
        6   ->->->-> ladder ->->->->  27
        20  ->->->-> ladder ->->->->  70
        25  ->->->-> snake  ->->->->  5
        34  ->->->-> snake  ->->->->  1
        36  ->->->-> ladder ->->->->  55
        47  ->->->-> snake  ->->->->  19
        63  ->->->-> ladder ->->->->  95
        65  ->->->-> snake  ->->->->  52
        68  ->->->-> ladder ->->->->  98
        87  ->->->-> snake  ->->->->  57
        91  ->->->-> snake  ->->->->  61
        99  ->->->-> snake  ->->->->  69

        100 to WIN
    ------------------------------------------

    ''')


def check_score(a):
    global score
    for m in score:
                if(m>=100):
                    display()
                    print(score)
                    if int(input('Player {} is the winner!!!\nGame Over\nDo you want to continue\nEnter "1" to continue "0" to exit\t'.format(a+1))):
                        start()
                    else:
                        exit(0)   
    pos = score[a]
    if pos == 3:
        print('player {} climbed ladder to 51'.format(a+1))
        return 51
    elif pos == 6:
        print('player {} climbed ladder to 27'.format(a+1))
        return 27
    elif pos == 20:
        print('player {} climbed ladder to 70'.format(a+1))
        return 70
    elif pos == 25:
        print('player {} got bitten by snake to 5'.format(a+1))
        return 5
    elif pos == 34:
        print('player {} got bitten by snake to 1'.format(a+1))
        return 1
    elif pos == 36:
        print('player {} climbed ladder to 55'.format(a+1))
        return 55
    elif pos == 47:
        print('player {} got bitten by snake to 19'.format(a+1))
        return 19
    elif pos == 63:
        print('player {} climbed ladder to 95'.format(a+1))
        return 95
    elif pos == 65:
        print('player {} got bitten by snake to 52'.format(a+1))
        return 52
    elif pos == 68:
        print('player {} climbed ladder to 98'.format(a+1))
        return 98
    elif pos == 87:
        print('player {} got bitten by snake to 57'.format(a+1))
        return 57
    elif pos == 91:
        print('player {} got bitten by snake to 61'.format(a+1))
        return 61
    elif pos == 99:
        print('player {} got bitten by snake to 69'.format(a+1))
        return 69
    else:
        return pos


def start():
    global score
    system('cls')
    print('Welcome to Snakes n Ladders game\nBy Saiyad Akmal')
    n = int(input('\nEnter total number of players: '))
    score = [0]*n
    total_playes = len(score)
    #game loop
    while True:
        for j in range(n):
            display()
            print(score)
            print('Roll dice for player',j+1)
            input('press enter to roll the dice')
            points = random.randint(1,6)
            print('face of dice: ',points)
            score[j] += points
            score[j] = check_score(j)
            if points == 6:
                while points == 6:
                    input('woohooh!!! you get a six and one more chance\npress enter to continue')
                    display()
                    print(score)
                    print('Roll dice for player',j+1)
                    input('press enter to roll the dice')
                    
                    points = random.randint(1,6)
                    print('face of dice: ',points)
                    score[j] += points
                    score[j] = check_score(j)
            input('Press enter to change the player')
        
if __name__ == "__main__":
    start()

