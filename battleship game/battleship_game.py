
# ********* BATTLESHIP GAME **********************************

# Once you run all the codes below, you can use only start(path) function to try the game with different maps.
# Start function takes txt file path as input.
# start("..\\..\\abc.txt")

# readFile function - to read a txt file (original map)


def read_file(path, letters, numbers, real_map):
    space = " "
    file = open(path, "r")
    lines = file.readlines()
    txt = list()
    for line in lines:
        if line[-1] == "\n":
            line = line[:-1]
        words = line.split(",")
        txt.append(words)
    for i in range(len(letters) + 1):
        if i == 0:
            real_map[space] = numbers
        else:
            real_map[letters[i - 1]] = txt[i - 1]
    return real_map

# showMap function - to show the raw map to player on the screen


def show_map(board, letters):
    space = " "
    double_space = "  "
    for i in range(len(letters) + 1):
        if i == 0:
            r1 = board[space]
            row1 = double_space.join(r1)
            print("   ", row1)
        else:
            other_r = board[letters[i - 1]]
            other_rows = double_space.join(other_r)
            print(letters[i - 1], space, other_rows)

# creatingMap function - creating the baseline of raw map


def create_map(board, letters, numbers):
    o_list = [["O", "O", "O", "O", "O", "O", "O", "O"],
              ["O", "O", "O", "O", "O", "O", "O", "O"],
              ["O", "O", "O", "O", "O", "O", "O", "O"],
              ["O", "O", "O", "O", "O", "O", "O", "O"],
              ["O", "O", "O", "O", "O", "O", "O", "O"],
              ["O", "O", "O", "O", "O", "O", "O", "O"],
              ["O", "O", "O", "O", "O", "O", "O", "O"],
              ["O", "O", "O", "O", "O", "O", "O", "O"]]
    for i in range(len(letters) + 1):
        if i == 0:
            board[" "] = numbers
        else:
            board[letters[i - 1]] = o_list[i - 1]

    return show_map(board, letters)

# start function - to initiate the game for player
# this function is where the rules of the game are also determined


def start(path):
    global prediction
    real_map = {}  # original map
    board = dict()  # raw map
    predictions = list()  # the list of all player's inputs
    damage_situation = list()  # the damage situation of the ships
    letters = ["A", "B", "C", "D", "E", "F", "G", "H"]
    numbers = ["1", "2", "3", "4", "5", "6", "7", "8"]
    remaining_guesses = 25

    read_file(path, letters, numbers, real_map)

    print("*" * 40, "\n")
    print("Welcome to the Battleship game!!\n")
    print("*" * 40)

    create_map(board, letters, numbers)

    while True:
        if count_ship("B", letters, board) == 4 and count_ship("C", letters, board) == 3 and \
                count_ship("D", letters, board) == 2 and count_ship("S", letters, board) == 1:
            break  # checking whether all the ships are sank or not

        elif remaining_guesses == 0:
            break  # checking if the remaining guesses over

        print("*" * 40)
        print("Remaining guesses:", remaining_guesses)

        for i in damage_situation:
            print(i)

        prediction = input("Make a guess:  ")  # player's guess

        if prediction in predictions:
            print("You have already chosen that cell!")
            continue

        predictions.append(prediction)

        if prediction == "GG":  # When the player is bored playing the game this code helps them to quit game
            # and see the original map
            print("See you later")
            break

        elif len(prediction) != 2:  # for input validation
            print("Please enter a valid coordinate('A1', 'B2', etc..)")
            show_map(board, letters)

        else:
            letter = prediction[0]
            number = prediction[1]

            if letter not in letters or number not in numbers:
                print("Please enter a valid coordinate('A1', 'B2', etc..)")
                show_map(board, letters)

            else:  # after the valid input the codes below matches the player's choice with the real map
                # to check if any ship is damaged
                if board[letter][int(number) - 1] == real_map[letter][int(number) - 1]:
                    board[letter][int(number) - 1] = "X"
                    remaining_guesses -= 1
                    show_map(board, letters)

                else:
                    if real_map[letter][int(number) - 1] == "M":
                        board[letter][int(number) - 1] = "M"
                        remaining_guesses -= 3
                        show_map(board, letters)

                    elif real_map[letter][int(number) - 1] == "B":
                        board[letter][int(number) - 1] = "B"
                        remaining_guesses -= 1

                        if count_ship("B", letters, board) < 4:
                            if "Battleship is damaged!" not in damage_situation:
                                damage_situation.append("Battleship is damaged!")

                        elif count_ship("B", letters, board) == 4:
                            damage_situation.remove("Battleship is damaged!")
                            damage_situation.append("Battleship is sank!")
                        show_map(board, letters)

                    elif real_map[letter][int(number) - 1] == "C":
                        board[letter][int(number) - 1] = "C"
                        remaining_guesses -= 1

                        if count_ship("C", letters, board) < 3:
                            if "Cruiser is damaged!" not in damage_situation:
                                damage_situation.append("Cruiser is damaged!")

                        elif count_ship("C", letters, board) == 3:
                            damage_situation.remove("Cruiser is damaged!")
                            damage_situation.append("Cruiser is sank!")
                        show_map(board, letters)

                    elif real_map[letter][int(number) - 1] == "D":
                        board[letter][int(number) - 1] = "D"
                        remaining_guesses -= 1

                        if count_ship("D", letters, board) < 2:
                            if "Destroyer is damaged!" not in damage_situation:
                                damage_situation.append("Destroyer is damaged!")

                        elif count_ship("D", letters, board) == 2:
                            damage_situation.remove("Destroyer is damaged!")
                            damage_situation.append("Destroyer is sank!")
                        show_map(board, letters)

                    elif real_map[letter][int(number) - 1] == "S":
                        board[letter][int(number) - 1] = "S"
                        remaining_guesses -= 1
                        damage_situation.append("Submarine is sank!")
                        show_map(board, letters)

    return win_or_lose(prediction, letters, board, real_map, damage_situation)

# win_or_lose function - when the game is over it runs and returns output about the result of the game


def win_or_lose(prediction, letters, board, real_map, damage_situation):
    if prediction == "GG":
        print("Good game!")
        return show_map(real_map, letters)

    elif count_ship("B", letters, board) == 4 and count_ship("C", letters, board) == 3 and \
            count_ship("D", letters, board) == 2 and count_ship("S", letters, board) == 1:
        return 'You won!'

    else:
        return you_lost(board, real_map, letters, damage_situation)

# countShip function - it counts the number of a certain ship the player has found until that time


def count_ship(ship, letters, board):
    count = 0

    for i in letters:
        count += board[i].count(ship)

    return count


# you_lost function - it runs when the player has lost the game and returns the necessary output


def you_lost(board, real_map, letters, damage_situation):
    for key in board:
        for i in range(len(board[key])):
            if board[key][i] != real_map[key][i]:

                if board[key][i] != "X":
                    board[key][i] = real_map[key][i]

    print("*" * 40, "\n")
    print("Remaining guesses: 0\n")

    for i in damage_situation:
        print(i, "\n")

    print("You lost!\n")
    print("*" * 40, "\n")

    return show_map(board, letters)



start("battlefield.txt") #uncomment this line to run the program
