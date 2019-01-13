import itertools
from colorama import Fore, Back, Style, init
init()


def win(current_game):
    """This function checks the current_game state to see if there are any winners."""
    def all_same(l):
        if l.count(l[0]) == len(l) and l[0] != 0:
            return True
        else:
            return False

    # Horizontal winnger algo.
    for row in game:
        print(row)
        if all_same(row):
            print(f"\nPlayer {row[0]} is the winner horizontally!")
            return True


    # Diagonal: bottom left to top right.
    diags = []
    for col, row in enumerate(reversed(range(len(game)))):
        diags.append(game[row][col])
    if all_same(diags):
        print(f"\nPlayer {diags[0]} is the winner diagonally!")
        return True

    # Diagonal: top left to bottom right.
    diags = []
    for col, row in enumerate(range(len(game))):
        diags.append(game[row][col])
    if all_same(diags):
        print(f"\nPlayer {diags[0]} is the winner diagonally!")
        return True


    # Vertical winner algo.
    for col in range(len(game)):
        check = []

        for row in game:
            check.append(row[col])

        if all_same(check):
            print(f"\nPlayer {check[0]} is the winner vertically!")
            return True

    return False
  

def game_board(game_map, player=0, row=0, column=0, just_display=False):
    try:
        if game_map[row][column] != 0:
            print("This position is occupied. Please choice another.")
            return game_map, False
        print("   " + "  ".join([str(i) for i in range(len(game_map))]))
        if not just_display:
            game_map[row][column] = player
        for count, row in enumerate(game_map):
            colored_row =""
            for item in row:
                if item == 0:
                    colored_row += "   "
                elif item == 1:
                    colored_row += Fore.GREEN + " X " + Style.RESET_ALL
                elif item == 2:
                    colored_row += Fore.MAGENTA + " O " + Style.RESET_ALL
            print(count, colored_row)

        return game_map, True

    except IndexError as e:
        print("Error: make sure you input row/column as 0 1 or 2.", e)
        return False

    except Exception as e:
        print("Something went very wrong!", e)
        return False


play = True
players = [1, 2]
while play:
    game_size = int(input("\nWhat board size do you want? "))
    game = [[0 for i in range(game_size)] for i in range(game_size)]
    game_won = False
    game, _ = game_board(game, just_display=True)
    player_choice = itertools.cycle([1, 2])
    while not game_won:
        current_player = next(player_choice)
        print(f"\nCurrent Player: {current_player}")
        played = False

        while not played:
            column_choice = int(input("\nWhat column do you want to play? (0, 1, 2): "))
            row_choice = int(input("\nWhat row do you want to play? (0, 1, 2): "))
            game, played = game_board(game, current_player, row_choice, column_choice)
            
        if win(game):
            game_won = True
            again = input("\nThe game is over, would you like to play again? (y/n) ")
            if again.lower() == "y":
                print("restarting...")
            elif again.lower() == "n":
                print("Byeeeeee.")
                play = False
            else:
                print("Not a valid answer, so.... c u l8tr alig8tor.")
                play = False