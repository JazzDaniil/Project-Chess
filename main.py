import pygame
import board_setup
import graphics
import logic


class Game:
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.board = []
        self.game_is_on = False
        self.game_mode_selected = False
        self.game_started = False
        self.figure = None
        self.loaded_board = False
        self.data_board = ""
        self.request = "new_save"
        self.infoObject = pygame.display.Info()
        self.width = self.infoObject.current_w
        self.height = self.infoObject.current_h
        print(self.width, self.height)
        self.saved_places = None
        self.player = "white"
        self.saved_places = None
        self.move_click = False
        self.main_menu_art1 = pygame.transform.scale(pygame.image.load("source/main_menu/Chess_Main_Art1.jpg"),
                                                     (self.width, self.height))
        self.main_menu_art2 = pygame.transform.scale(pygame.image.load("source/main_menu/Chess_Main_Art2.jpg"),
                                                     (self.width, self.height))
        self.main_menu_art3 = pygame.transform.scale(pygame.image.load("source/main_menu/Chess_Main_Art3.jpg"),
                                                     (self.width, self.height))
        self.main_menu_art4 = pygame.transform.scale(pygame.image.load("source/main_menu/Chess_Main_Art4.jpg"),
                                                     (self.width, self.height))
        self.play_button = pygame.image.load("source/ui/Play_button.png")
        self.play_button = pygame.transform.scale(self.play_button, (0.1 * self.width, 0.1 * self.height))
        self.play_button_size = self.play_button.get_size()
        self.display_time = 1
        screen.blit(self.main_menu_art1, (0, 0))
        screen.blit(self.play_button, (self.width // 2 - self.play_button_size[0] // 2,
                                       self.height // 2 - self.play_button_size[1] // 2))
        pygame.display.update()
        self.game_mode_selection = pygame.image.load("source/ui/game_mode_selection.png")
        self.game_mode_selection = pygame.transform.scale(self.game_mode_selection, (0.5 * self.width, 0.5 * self.height))
        self.game_mode_selection_size = self.game_mode_selection.get_size()
        self.good_game = pygame.mixer.music.load("source/music/Love me this summer - PLANEON.mp3")
        pygame.mixer.music.play(-1)
        self.main()

    def main(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                if self.game_mode_selected == "classic":
                    self.game_started = True
                    if not self.loaded_board:
                        pygame.mixer.music.unload()
                        self.chess = pygame.mixer.music.load("source/music/Atmospheric chess - PLANEON.mp3")
                        pygame.mixer.music.play(-1)
                        self.loaded_board = True
                        self.load_board()
                        pygame.display.update()
                    else:
                        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not self.move_click:
                            position = pygame.mouse.get_pos()
                            self.saved_places = logic.select(position, self.board, screen, pygame, self.width,
                                                             self.height, self.player)
                            if self.saved_places:
                                self.figure = self.saved_places[4]
                                self.move_click = True
                        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.move_click:
                            position = pygame.mouse.get_pos()
                            if event.button == 1 and self.move_click:
                                self.move_click = False
                                self.board = logic.move(position, self.board,
                                                        self.saved_places, self.width, self.height, self.player,
                                                        self.figure)
                                self.player = self.board[1]
                                self.board = self.board[0]
                                graphics.build_board(self.board, screen, pygame, self.width, self.height)
                                pygame.display.update()
                if self.game_is_on and not self.game_started:
                    screen.blit(self.game_mode_selection, (self.width // 2 - self.game_mode_selection_size[0] // 2,
                                                           self.height // 2 - self.game_mode_selection_size[1] // 2))
                    pygame.display.update()
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not self.game_mode_selected:
                        position = pygame.mouse.get_pos()
                        if self.width // 2 - self.game_mode_selection_size[0] // 2 < position[0] < \
                                self.width // 2 + self.game_mode_selection_size[0] // 2:
                            if self.height // 2 - self.game_mode_selection_size[1] // 2 < position[1] < \
                                    self.height // 2 - self.game_mode_selection_size[1] // 4:
                                self.game_mode_selected = "classic"
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not self.game_is_on:
                    position = pygame.mouse.get_pos()
                    if self.width // 2 - self.play_button_size[0] // 2 \
                            < position[0] < self.width // 2 + self.play_button_size[0] // 2 \
                            and self.height // 2 - self.play_button_size[1] // 2 < position[1] \
                            < self.height // 2 + self.play_button_size[1] // 2:
                        self.game_is_on = True
                if not self.game_is_on and not self.game_started:
                    self.clock.tick(10)
                    if self.display_time == 5:
                        self.display_time = 1
                    if self.display_time == 1:
                        screen.blit(self.main_menu_art1, (0, 0))
                    elif self.display_time == 2:
                        screen.blit(self.main_menu_art2, (0, 0))
                    elif self.display_time == 3:
                        screen.blit(self.main_menu_art3, (0, 0))
                    else:
                        screen.blit(self.main_menu_art4, (0, 0))
                    self.display_time += 1
                    screen.blit(self.play_button, (self.width // 2 - self.play_button_size[0] // 2,
                                                   self.height // 2 - self.play_button_size[1] // 2))
                    pygame.display.update()

    def load_board(self):
        self.board = board_setup.get_save(self.request)
        graphics.build_board(self.board, screen, pygame, self.width, self.height)
        pygame.display.update()


if __name__ == '__main__':
    pygame.init()
    flags = pygame.FULLSCREEN
    screen = pygame.display.set_mode((0, 0), flags, vsync=1)
    pygame.display.set_caption("Chess by JazzDan")
    game = Game()
    pygame.display.flip()
    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()
