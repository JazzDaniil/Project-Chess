import graphics
import pawn
import rook
import bishop


def select(pos, board, screen, pygame, width, height, player):
    cell_status = None
    x = None
    y = None
    flag = None
    available_cells = [[], [], []]
    special_height = -(height // 8)
    for i in range(8):
        special_width = (width - height) // 2
        special_height += height // 8
        for j in range(8):
            if special_width < pos[0] < special_width + (height // 8) and special_height < pos[1] < \
                    special_height + (height // 8):
                cell_status = board[i][j][str(i) + str(j)]
                x = j
                y = i
                flag = True
                break
            special_width += height // 8
        if flag is True:
            break
    if cell_status:
        if "figure" in cell_status:
            if "rook" in cell_status:
                available_cells = rook.Rook.available_turns(cell_status[2], board, x, y, player)
            elif "knight" in cell_status:
                pass
            elif "bishop" in cell_status:
                available_cells = bishop.Bishop.available_turns(cell_status[2], board, x, y, player)
            elif "queen" in cell_status:
                pass
            elif "king" in cell_status:
                pass
            elif "pawn" in cell_status:
                available_cells = pawn.Pawn.available_turns(cell_status[2], board, x, y, player)
            attack_cells = available_cells[1]
            available_cells = available_cells[0]
            figure = cell_status[0]
            if available_cells or attack_cells:
                graphics.show_available_turns(available_cells, attack_cells, screen, pygame, width, height)
                return available_cells, attack_cells, y, x, figure
            return None


def move(pos, board, cells, width, height, player, figure):
    available_cells = cells[0]
    attack_cells = cells[1]
    y = cells[2]
    x = cells[3]
    flag = False
    for j in range(len(attack_cells)):
        if attack_cells[j][1] * (height // 8)\
                < pos[0] < attack_cells[j][1] * (height // 8) * 2 and\
                attack_cells[j][0] * (height // 8) < pos[1]\
                < attack_cells[j][0] * (height // 8) * 2:
            if player == "white":
                if board[attack_cells[j][0]][attack_cells[j][1]][str(attack_cells[j][0]) +
                                                                 str(attack_cells[j][1])][0] == "shadow_black_attack":
                    board[attack_cells[j][0]][attack_cells[j][1]][str(attack_cells[j][0]) +
                                                                  str(attack_cells[j][1])] = [None]
            else:
                if board[attack_cells[j][0]][attack_cells[j][1]][str(attack_cells[j][0]) +
                                                                 str(attack_cells[j][1])][0] == "shadow_white_attack":
                    board[attack_cells[j][0]][attack_cells[j][1]][str(attack_cells[j][0]) +
                                                                  str(attack_cells[j][1])] = [None]
            board[attack_cells[j][0]][attack_cells[j][1]][str(attack_cells[j][0]) +
                                                          str(attack_cells[j][1])]\
                = board[y][x][str(y) + str(x)]
            board[y][x][str(y) + str(x)] = [None]
            flag = True
            if figure == "pawn":
                if not board[attack_cells[j][0]][attack_cells[j][1]][str(attack_cells[j][0]) +
                                                                     str(attack_cells[j][1])][2].check_turn():
                    board[attack_cells[j][0]][attack_cells[j][1]][str(attack_cells[j][0]) +
                                                                  str(attack_cells[j][1])][2].set_turn()
            break
    for i in range(len(available_cells)):
        if available_cells[i][1] * (height // 8)\
                < pos[0] < available_cells[i][1] * \
                (height // 8) * 2 and\
                available_cells[i][0] * (height // 8) < pos[1]\
                < available_cells[i][0] * (height // 8) * 2:
            board[available_cells[i][0]][available_cells[i][1]][str(available_cells[i][0]) +
                                                                str(available_cells[i][1])]\
                = board[y][x][str(y) + str(x)]
            board[y][x][str(y) + str(x)] = [None]
            flag = True
            if figure == "pawn":
                if not board[available_cells[i][0]][available_cells[i][1]][str(available_cells[i][0]) +
                                                                           str(available_cells[i][1])][2].check_turn():
                    board[available_cells[i][0]][available_cells[i][1]][str(available_cells[i][0]) +
                                                                        str(available_cells[i][1])][2].set_turn()
                    if player == "white":
                        if board[available_cells[i][0] + 1][available_cells[i][1]][str(available_cells[i][0] + 1) +
                                                                                   str(available_cells[i][1])] ==\
                                [None]:
                            board[available_cells[i][0] + 1][available_cells[i][1]][str(available_cells[i][0] + 1) +
                                                                                    str(available_cells[i][1])] =\
                                ["shadow_white_attack"]
                    else:
                        if board[available_cells[i][0] - 1][available_cells[i][1]][str(available_cells[i][0] - 1) +
                                                                                   str(available_cells[i][1])] ==\
                                [None]:
                            board[available_cells[i][0] - 1][available_cells[i][1]][str(available_cells[i][0] - 1) +
                                                                                    str(available_cells[i][1])] =\
                                ["shadow_black_attack"]
            break
    if flag:
        if player == "white":
            for i in range(len(board)):
                for j in range(len(board[i])):
                    if board[i][j][str(i) + str(j)][0] == "shadow_black_attack":
                        board[i][j][str(i) + str(j)] = [None]
            player = "black"
        else:
            for i in range(len(board)):
                for j in range(len(board[i])):
                    if board[i][j][str(i) + str(j)][0] == "shadow_white_attack":
                        board[i][j][str(i) + str(j)] = [None]
            player = "white"
    return board, player
