class Pawn:
    def __init__(self, color):
        self.color = color
        self.available_cells = []
        self.attack_cells = []
        self.turn = False

    def get_color(self):
        return self.color

    def set_turn(self):
        self.turn = True

    def check_turn(self):
        return self.turn

    def available_turns(self, board, x, y, player):
        if self.available_cells:
            self.available_cells = []
        if self.attack_cells:
            self.attack_cells = []
        if self.color == player:
            if self.color == "black":
                if y == 1:
                    if board[y + 1][x][str(y + 1) + str(x)][0] is None and \
                            board[y + 2][x][str(y + 2) + str(x)][0] is None:
                        self.available_cells.append([y + 2, x])
                if (0 <= (y + 1) <= 7) and board[y + 1][x][str(y + 1) + str(x)][0] is None:
                    self.available_cells.append([y + 1, x])
                if (0 <= (y + 1) <= 7) and (0 <= (x - 1) <= 7) and \
                        (board[y + 1][x - 1][str(y + 1) + str(x - 1)][0] == "shadow_white_attack" or
                         (board[y + 1][x - 1][str(y + 1) + str(x - 1)][0] is not None and
                         board[y + 1][x - 1][str(y + 1) + str(x - 1)][1] == "figure" and
                         board[y + 1][x - 1][str(y + 1) + str(x - 1)][2].get_color() == "white")):
                    self.attack_cells.append([y + 1, x - 1])
                if (0 <= (y + 1) <= 7) and (0 <= (x + 1) <= 7) and \
                        (board[y + 1][x + 1][str(y + 1) + str(x + 1)][0] == "shadow_white_attack" or
                         (board[y + 1][x + 1][str(y + 1) + str(x + 1)][0] is not None and
                         board[y + 1][x + 1][str(y + 1) + str(x + 1)][1] == "figure" and
                         board[y + 1][x + 1][str(y + 1) + str(x + 1)][2].get_color() == "white")):
                    self.attack_cells.append([y + 1, x + 1])
            else:
                if y == 6:
                    if board[y - 1][x][str(y - 1) + str(x)][0] is None and \
                            board[y - 2][x][str(y - 2) + str(x)][0] is None:
                        self.available_cells.append([y - 2, x])
                if (0 <= (y - 1) <= 7) and board[y - 1][x][str(y - 1) + str(x)][0] is None:
                    self.available_cells.append([y - 1, x])
                if (0 <= (y - 1) <= 7) and (0 <= (x - 1) <= 7) and \
                        (board[y - 1][x - 1][str(y - 1) + str(x - 1)][0] == "shadow_black_attack" or
                         (board[y - 1][x - 1][str(y - 1) + str(x - 1)][0] is not None and
                         board[y - 1][x - 1][str(y - 1) + str(x - 1)][1] == "figure" and
                         board[y - 1][x - 1][str(y - 1) + str(x - 1)][2].get_color() == "black")):
                    self.attack_cells.append([y - 1, x - 1])
                if (0 <= (y - 1) <= 7) and (0 <= (x + 1) <= 7) and \
                        (board[y - 1][x + 1][str(y - 1) + str(x + 1)][0] == "shadow_black_attack" or
                         (board[y - 1][x + 1][str(y - 1) + str(x + 1)][0] is not None and
                         board[y - 1][x + 1][str(y - 1) + str(x + 1)][1] == "figure" and
                         board[y - 1][x + 1][str(y - 1) + str(x + 1)][2].get_color() == "black")):
                    self.attack_cells.append([y - 1, x + 1])
        return self.available_cells, self.attack_cells
