# size = 3
# board = []

# # prints raw lists that we need for board
# for y in range(size):
#     board.append([])
#     for x in range(size):
#         board[y].append("[%d][%d]" % (y, x))
# # formats the board
# for row in board:
#     for column in row:
#         print("%s " % column, end="")
#     print("\n")

# make each funciotn a funciton!

print("\n\nPlayer X is moving. \n\n")

def move(size=3, location, player):
    board = []
    if size == 3:
        for y in range(size):
            board.append([])
            for x in range(size):
                board[y].append("[%d][%d]" % (y, x))
        for row in board:
            for column in row:
                print("%s " column, end="")
            print("\n")
    else: 
        print("sorry this is an invalid board size")
    if location[0] < 4 and location[1] < 4 and 