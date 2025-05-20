from random import randint

TARGET_SCORE = 100
players = [{'score': 0, 'all_in_time': 1}, {'score': 0, 'all_in_time': 1}]
double_six = False
all_in_total = 0
player_1_turn = True

def turn():
    global player_1_turn
    if player_1_turn:
        player = players[0]
    else:
        player = players[1]
    player_1_turn = not player_1_turn
    return player

def dice():
    return randint(1,6)    

def basic_game(player, all_in):
    total = 0
    recent_pt = 0
    while True:
        round_pt = dice()
        print(f"Rolled: {round_pt}")
        if round_pt == 6 and recent_pt == 6:
            global double_six
            double_six = True
            break
        recent_pt = round_pt
        global all_in_total
        all_in_total = total + round_pt
        if round_pt == 1:
            total = 0
            break
        total += round_pt
        if all_in == 'y':
            if 2 * total + player['score'] >= TARGET_SCORE:
                break
        elif total + player['score'] >= TARGET_SCORE:
            break
        go_on = input('Hold?(y/n) ')
        if go_on == 'y':
            break
    return total, all_in_total

def winning():
    if players[0]['score'] >= TARGET_SCORE:
        print('Player 1 wins!')
    else:
        print('Player 2 wins!')

def main():
    print('Welcome to Dice Game!')
    while (
        players[0]['score'] < TARGET_SCORE and 
        players[1]['score'] < TARGET_SCORE
        ):
        if player_1_turn:
            print('Player 1 turn!')
        else:
            print('Player 2 turn!')
        player = turn()
        all_in = 'n'
        if player['all_in_time']:
            all_in = input('All in?(y/n) ')
        all_in_total = 0
        round_total, all_in_total = basic_game(player, all_in)
        global double_six
        if double_six:
            print('What bad luck! Your score is going to be reset to zero!')
            player['score'] = 0
            double_six = False
        elif all_in == 'y':
            player['all_in_time'] -= 1
            if round_total == 0:
                print('All-in failed, you are in trouble!')
                player['score'] -= 2 * all_in_total
            else:
                print('All-in successful, you are so brave!')
                player['score'] += 2 * all_in_total
        else:
            if round_total:
                print('A successful round!')
            else:
                print("You're going to get 0 scores.")
            player['score'] += round_total
        print(f'Your score is {player["score"]}!')
    winning()

if __name__ == '__main__':
    main()