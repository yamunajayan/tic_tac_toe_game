import os

is_game_on = True

display_sign = ("    {0}     |     {1}    |     {2}    \n"
                "----------|----------|----------\n"
                "    {3}     |     {4}    |     {5}    \n"
                "----------|----------|----------\n"
                "    {6}     |     {7}    |     {8}    \n")


def display_board(signs):
    os.environ['TERM'] = 'xterm'
    os.system('clear')
    print(display_sign.format(*signs))


def check_winner(user_combos):
    win_combos = ["012", "345", "678", "036", "147", "258", "048", "246"]
    for combo in win_combos:
        if all(cell in user_combos for cell in combo):
            return True
    return False


def is_board_full(signs):
    return ' ' not in signs


def tic_tac():
    user1_sign = input("Choose your sign: X or O: ")

    if user1_sign.upper() == "X":
        user2_sign = "O"
    else:
        user2_sign = "X"

    signs = [' '] * 9
    user1_combos = []
    user2_combos = []

    while True:
        display_board(signs)

        user1_sel = int(input("User1: Enter the number of cell you want to choose? ")) - 1
        while signs[user1_sel] != ' ':
            print("Cell already taken. Choose another cell.")
            user1_sel = int(input("User1: Enter the number of cell you want to choose? ")) - 1

        user1_combos.append(str(user1_sel))
        signs[user1_sel] = user1_sign  # Adjust indices

        if check_winner(user1_combos):
            display_board(signs)
            print("User1 wins!")
            break

        if is_board_full(signs):
            display_board(signs)
            print("It's a draw!")
            break

        display_board(signs)

        user2_sel = int(input("User2: Enter the number of cell you want to choose? ")) - 1
        while signs[user2_sel] != ' ':
            print("Cell already taken. Choose another cell.")
            user2_sel = int(input("User2: Enter the number of cell you want to choose? ")) - 1

        user2_combos.append(str(user2_sel))
        signs[user2_sel] = user2_sign  # Adjust indices

        if check_winner(user2_combos):
            display_board(signs)
            print("User2 wins!")
            break

        if is_board_full(signs):
            display_board(signs)
            print("It's a draw!")
            break


while is_game_on:
    tic_tac()

    if input("Do you want to play a game of Tic tac toe? Type 'y' or 'n': ").lower() != "y":
        is_game_on = False
