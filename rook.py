class Rook:
    def __init__(self, color):
        self.color = color
        self.available_cells = []
        self.attack_cells = []

    def get_color(self):
        return self.color

    def available_turns(self, board, x, y, player):
        if self.available_cells:
            self.available_cells = []
        if self.attack_cells:
            self.attack_cells = []
        if self.color == player:
            flag = False
            flag1 = False
            flag2 = False
            flag3 = False
            for i in range(1, 8):
                if 0 <= (y + i) <= 7:
                    if flag is False and board[y + i][x][str(y + i) + str(x)][0] is None:
                        self.available_cells.append([y + i, x])
                    elif flag is False and board[y + i][x][str(y + i) + str(x)][0] is not None and \
                        board[y + i][x][str(y + i) + str(x)][1] == "figure" and \
                            board[y + i][x][str(y + i) + str(x)][2].get_color() !=\
                            board[y][x][str(y) + str(x)][2].get_color():
                        self.attack_cells.append([y + i, x])
                        flag = True
                    elif flag is False and board[y + i][x][str(y + i) + str(x)][0] is not None and \
                        board[y + i][x][str(y + i) + str(x)][1] == "figure" and \
                            board[y + i][x][str(y + i) + str(x)][2].get_color() ==\
                            board[y][x][str(y) + str(x)][2].get_color():
                        flag = True
                if 0 <= (y - i) <= 7:
                    if flag1 is False and board[y - i][x][str(y - i) + str(x)][0] is None:
                        self.available_cells.append([y - i, x])
                    elif flag1 is False and board[y - i][x][str(y - i) + str(x)][0] is not None and \
                            board[y - i][x][str(y - i) + str(x)][1] == "figure" and \
                            board[y - i][x][str(y - i) + str(x)][2].get_color() != \
                            board[y][x][str(y) + str(x)][2].get_color():
                        self.attack_cells.append([y - i, x])
                        flag1 = True
                    elif flag1 is False and board[y - i][x][str(y - i) + str(x)][0] is not None and \
                            board[y - i][x][str(y - i) + str(x)][1] == "figure" and \
                            board[y - i][x][str(y - i) + str(x)][2].get_color() == \
                            board[y][x][str(y) + str(x)][2].get_color():
                        flag1 = True
                if 0 <= (x + i) <= 7:
                    if flag2 is False and board[y][x + i][str(y) + str(x + i)][0] is None:
                        self.available_cells.append([y, x + i])
                    elif flag2 is False and board[y][x + i][str(y) + str(x + i)][0] is not None and \
                        board[y][x + i][str(y) + str(x + i)][1] == "figure" and \
                            board[y][x + i][str(y) + str(x + i)][2].get_color() !=\
                            board[y][x][str(y) + str(x)][2].get_color():
                        self.attack_cells.append([y, x + i])
                        flag2 = True
                    elif flag2 is False and board[y][x + i][str(y) + str(x + i)][0] is not None and \
                        board[y][x + i][str(y) + str(x + i)][1] == "figure" and \
                            board[y][x + i][str(y) + str(x + i)][2].get_color() ==\
                            board[y][x][str(y) + str(x)][2].get_color():
                        flag2 = True
                if 0 <= (x - i) <= 7:
                    if flag3 is False and board[y][x - i][str(y) + str(x - i)][0] is None:
                        self.available_cells.append([y, x - i])
                    elif flag3 is False and board[y][x - i][str(y) + str(x - i)][0] is not None and \
                            board[y][x - i][str(y) + str(x - i)][1] == "figure" and \
                            board[y][x - i][str(y) + str(x - i)][2].get_color() != \
                            board[y][x][str(y) + str(x)][2].get_color():
                        self.attack_cells.append([y, x - i])
                        flag3 = True
                    elif flag3 is False and board[y][x - i][str(y) + str(x - i)][0] is not None and \
                            board[y][x - i][str(y) + str(x - i)][1] == "figure" and \
                            board[y][x - i][str(y) + str(x - i)][2].get_color() == \
                            board[y][x][str(y) + str(x)][2].get_color():
                        flag3 = True
        return self.available_cells, self.attack_cells
