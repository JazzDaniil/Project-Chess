def build_board(board, screen, pygame, width, height):
    black_cell = pygame.image.load("source/board/Black_cell.png")
    white_cell = pygame.image.load("source/board/White_cell.png")
    visual_board = pygame.image.load("source/board/Board.png")
    black_rook = pygame.image.load("source/figures/Black_rook.png")
    black_rook = pygame.transform.scale(black_rook, (height // 8, height // 8))
    black_knight = pygame.image.load("source/figures/Black_knight.png")
    black_knight = pygame.transform.scale(black_knight, (height // 8, height // 8))
    black_bishop = pygame.image.load("source/figures/Black_bishop.png")
    black_bishop = pygame.transform.scale(black_bishop, (height // 8, height // 8))
    black_queen = pygame.image.load("source/figures/Black_queen.png")
    black_queen = pygame.transform.scale(black_queen, (height // 8, height // 8))
    black_king = pygame.image.load("source/figures/Black_king.png")
    black_king = pygame.transform.scale(black_king, (height // 8, height // 8))
    black_pawn = pygame.image.load("source/figures/Black_pawn.png")
    black_pawn = pygame.transform.scale(black_pawn, (height // 8, height // 8))
    white_rook = pygame.image.load("source/figures/White_rook.png")
    white_rook = pygame.transform.scale(white_rook, (height // 8, height // 8))
    white_knight = pygame.image.load("source/figures/White_knight.png")
    white_knight = pygame.transform.scale(white_knight, (height // 8, height // 8))
    white_bishop = pygame.image.load("source/figures/White_bishop.png")
    white_bishop = pygame.transform.scale(white_bishop, (height // 8, height // 8))
    white_queen = pygame.image.load("source/figures/White_queen.png")
    white_queen = pygame.transform.scale(white_queen, (height // 8, height // 8))
    white_king = pygame.image.load("source/figures/White_king.png")
    white_king = pygame.transform.scale(white_king, (height // 8, height // 8))
    white_pawn = pygame.image.load("source/figures/White_pawn.png")
    white_pawn = pygame.transform.scale(white_pawn, (height // 8, height // 8))
    visual_board = pygame.transform.scale(visual_board, (height, height))
    screen.blit(visual_board, ((width - height) // 2, 0))
    special_height = -(height // 8)
    for i in range(len(board)):
        special_height += height // 8
        special_width = (width - height) // 2
        for j in range(len(board)):
            status = board[i][j][str(i) + str(j)]
            if status:
                if "figure" in status:
                    if status[2].get_color() == "black":
                        if "rook" in status:
                            screen.blit(black_rook, (special_width, special_height))
                        elif "knight" in status:
                            screen.blit(black_knight, (special_width, special_height))
                        elif "bishop" in status:
                            screen.blit(black_bishop, (special_width, special_height))
                        elif "queen" in status:
                            screen.blit(black_queen, (special_width, special_height))
                        elif "king" in status:
                            screen.blit(black_king, (special_width, special_height))
                        elif "pawn" in status:
                            screen.blit(black_pawn, (special_width, special_height))
                    else:
                        if "rook" in status:
                            screen.blit(white_rook, (special_width, special_height))
                        elif "knight" in status:
                            screen.blit(white_knight, (special_width, special_height))
                        elif "bishop" in status:
                            screen.blit(white_bishop, (special_width, special_height))
                        elif "queen" in status:
                            screen.blit(white_queen, (special_width, special_height))
                        elif "king" in status:
                            screen.blit(white_king, (special_width, special_height))
                        elif "pawn" in status:
                            screen.blit(white_pawn, (special_width, special_height))
            special_width += height // 8
    pygame.display.update()


def show_available_turns(ava_cells, att_cells, screen, pygame, width, height):
    attack_cell = pygame.image.load("source/cell_selection/Attack_cell.png")
    available_cell = pygame.image.load("source/cell_selection/Available_cell.png")
    for cell in ava_cells:
        screen.blit(available_cell, (cell[1] * height // 8, cell[0] * height // 8))
    for cell in att_cells:
        screen.blit(attack_cell, (cell[1] * height // 8, cell[0] * (height // 8)))
    pygame.display.update()
