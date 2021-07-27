# VERSION 3
import pygame

# constants
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

BOX_HEIGHT = 200
BOX_WIDTH = 200


# function checks if someone won
# scoring methodology:
# X gets 1 point everytime it is in a cell and 'O' gets 10 points every time it is in a cell
# if sum = 3 X wins and if sum = 30 then O wins
def is_winner(t_array):
    for i in range(0, 3):
        # checking if row is completely filled by all "X" or "O"
        sum = t_array[i][0]+t_array[i][1]+t_array[i][2]
        # checking if the sum is either 3 (x wins) or 30 (o wins)
        if sum == 3:
            return "x"
        elif sum == 30:
            return "o"
    # checking if column is completely filled by all "X" or "O"
    for j in range(0, 3):
        # t_array[0][j]; [0] = x value, [j] = y value
        # if the sum of the column is equal to 3 (x wins) or 30 (o wins)
        sum = t_array[0][j]+t_array[1][j]+t_array[2][j]
        if sum == 3:
            return "x"
        elif sum == 30:
            return "o"

    # checking if there is 3 diagonally (top left to bottom right)
    sum = t_array[0][0]+t_array[1][1]+t_array[2][2]
    # if the sum of the diagonal is equal to 3 (x wins) or 30 (o wins)
    if sum == 3:
        return "x"
    elif sum == 30:
        return "o"

    # checking if there is 3 diagonally (top right to bottom left)
    sum = t_array[2][0] + t_array[1][1] + t_array[0][2]
    # if the sum of the diagonal is equal to 3 (x wins) or 30 (o wins)
    if sum == 3:
        return "x"
    elif sum == 30:
        return "o"

    # if any of the boxes are blank
    for i in range(0, 3):
        for j in range(0, 3):
            # using the scoring array if all of the boxes are not
            # either filled with 1 or 10 then keep playing or their sum is not 3 or 30
            if t_array[i][j] == 0:
                return "continue playing"
    # if it returns "d" it is a tie
    # no blank spaces and still reached up to this point means that it is a tie
    return "d"


# position array
# coordinates of all of the top left corners of the boxes in the tic tac toe
location_array = [[[0, 0], [200, 0], [400, 0]],
                  [[0, 200], [200, 200], [400, 200]],
                  [[0, 400], [200, 400], [400, 400]]]

# scoring array
# setting everything equal to zero, means everything is blank
# if it changes to 1 it is x and if it changes to 10 it is o
# list is 1 by n and an array is n by n
# an array is a collection of elements identified by an index
value_array = [[0, 0, 0],
               [0, 0, 0],
               [0, 0, 0]]

# initializing variables
play = True
row = 0
column = 0
current_location = (0, 0)
player = "x"
win_message = ""

# main
# 1) making the grid
# 2) look for events
# 3) register selection
# 4) check for winner

pygame.init()

mttt_screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Maya's Tic Tac Toe")

font = pygame.font.Font(None, 300)
# drawing a big rectangle for the background
pygame.draw.rect(mttt_screen, BLACK, (location_array[0][0][0], location_array[0][0][1], 600, 600))

# 1) making the grid

# creating tic tac toe grid using the positioning array
for i in range(0, 3):
    for j in range(0, 3):
        pygame.draw.rect(mttt_screen, WHITE, (location_array[i][j][0], location_array[i][j][1], BOX_WIDTH - 10, BOX_HEIGHT - 10))

# starting the game
while play:

    for event in pygame.event.get():

        # 2) look for events

        # if the QUIT button is pressed, then exit
        if event.type == pygame.QUIT:
            play = False
        # if the mouse button is pressed then get the position of the click
        if event.type == pygame.MOUSEBUTTONDOWN:
            current_location = pygame.mouse.get_pos()
            # print(current_location)
            # current_location[0] is the x coordinate of the pygame.mouse.get_pos()
            # then you are flooring it to get the lower, closest number
            # Ex: 90 --> 0
            # using 200 for the divisor because the box is 200 wide and 200 high
            # all values in the first row, if pressed, will start with 0, 2nd row 1, and 3rd row 2
            column = current_location[0] // 200
            # current_location[1] is the y coordinate of the pygame.mouse.get_pos()
            # then you are flooring it to get the lower, closest number
            # Ex: 343 --> 1
            row = current_location[1] // 200
            # print(row, column)
            # if a box is pressed it either changes its value to 1 or 10

            # if the box in the value array is empty i.e value=0 then allow to be changed and render the font
            if value_array[row][column] == 0:
                # font.render() places a font on a surface
                tic_tac = font.render(player, True, BLUE)
                # blit updates the screen
                # location_array[row][column][0] + 35; location_array[row][column] = which cell then [0] is the x value
                # + 35 to make it at the center x pos
                # location_array[row][column][1]); location_array[row][column] = which cell then [1] is the y value
                mttt_screen.blit(tic_tac, (location_array[row][column][0] + 35, location_array[row][column][1]))

                # 3) register selection

                # switching turns and marking the cell as filled with O hence the 1
                if player == "x":
                    player = "o"
                    value_array[row][column] = 1
                # if player is not x switch it to x and mark it as filled with X hence the 10
                else:
                    player = "x"
                    value_array[row][column] = 10
                # print(value_array)

            # 4) check for winner

            # if the is_winner function returns "x" then print("X is the winner")
            # play = False so it quits after 5 seconds
            if is_winner(value_array) == "x":
                win_message = "X is the winner!"
                play = False
            # if the is_winner function returns "o" then print("O is the winner")
            # play = False so it quits after 5 seconds
            elif is_winner(value_array) == "o":
                win_message = "O is the winner!"
                play = False
            # if the is_winner function returns "d" then print("It is a tie")
            # play = False so it quits after 5 seconds
            elif is_winner(value_array) == "d":
                win_message = "It is a tie!"
                play = False
            # then when play = False print the winning message; who won in RED at the middle of the screen
            if not play:
                font = pygame.font.Font(None, 100)
                winner = font.render(win_message, True, RED)
                mttt_screen.blit(winner, (50, 200))

    # update the entire display
    pygame.display.update()
# before quitting waits for 5 seconds
pygame.time.delay(5000)
# and then quit the game
pygame.quit()

# references :
# https://www.pygame.org/docs/
# https://www.youtube.com/watch?v=i6xMBig-pP4&t=582s