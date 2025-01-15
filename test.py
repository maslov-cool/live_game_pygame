# первым ходит синий при желании это изменить можно поменять значение self.now в __init__ класса Board
import pygame


class Life:
    # создание поля
    def __init__(self, width_, height_):
        self.width = width_
        self.height = height_
        self.board = [[0 for _ in range(width_)] for _ in range(height_)]
        # значения по умолчанию
        self.left = 10
        self.top = 10
        self.cell_size = 30
        self.now = 'blue'

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen_):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] == 1:
                    pygame.draw.rect(screen_, 'green',
                                     [self.left + self.cell_size * j + 1, self.top + self.cell_size * i + 1,
                                      self.cell_size - 1, self.cell_size - 1])
                else:
                    pygame.draw.rect(screen_, 'black',
                                     [self.left + self.cell_size * j + 1, self.top + self.cell_size * i + 1,
                                      self.cell_size - 1, self.cell_size - 1])
                pygame.draw.rect(screen_, 'white', [self.left + self.cell_size * j, self.top + self.cell_size * i,
                                                    self.cell_size, self.cell_size], 1)

    def get_cell(self, mouse_pos: tuple):
        if (not self.left <= mouse_pos[0] <= self.left + self.cell_size * self.width or
                not self.top <= mouse_pos[1] <= self.top + self.cell_size * self.height):
            return None
        else:
            return (mouse_pos[1] - self.top) // self.cell_size, (mouse_pos[0] - self.left) // self.cell_size

    def on_click(self, cell):
        if not self.board[cell[0]][cell[1]]:
            self.board[cell[0]][cell[1]] = 1
        else:
            self.board[cell[0]][cell[1]] = 0

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        if cell:
            self.on_click(cell)

    def next_move(self):
        A = self.board.copy()
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):

                if not i and not j:

                    if self.board[i][j]:
                        if sum([self.board[i + 1][j], self.board[i][j + 1], self.board[i + 1][j + 1]]) not in [2, 3]:
                            A[i][j] = 0
                    else:
                        if sum([self.board[i + 1][j], self.board[i][j + 1], self.board[i + 1][j + 1]]) == 3:
                            A[i][j] = 1

                elif i == self.height - 1 and not j:

                    if self.board[i][j]:
                        if sum([self.board[i - 1][j], self.board[i][j + 1], self.board[i - 1][j + 1]]) not in [2, 3]:
                            A[i][j] = 0
                    else:
                        if sum([self.board[i - 1][j], self.board[i][j + 1], self.board[i - 1][j + 1]]) == 3:
                            A[i][j] = 1

                elif i == self.height - 1 and j == self.width - 1:

                    if self.board[i][j]:
                        if sum([self.board[i - 1][j], self.board[i][j - 1], self.board[i - 1][j - 1]]) not in [2, 3]:
                            A[i][j] = 0
                    else:
                        if sum([self.board[i - 1][j], self.board[i][j - 1], self.board[i - 1][j - 1]]) == 3:
                            A[i][j] = 1

                elif not i and j == self.width - 1:

                    if self.board[i][j]:
                        if sum([self.board[i + 1][j], self.board[i][j - 1], self.board[i + 1][j - 1]]) not in [2, 3]:
                            A[i][j] = 0
                    else:
                        if sum([self.board[i + 1][j], self.board[i][j - 1], self.board[i + 1][j - 1]]) == 3:
                            A[i][j] = 1

                elif not i and 0 < j < self.width - 1:

                    if self.board[i][j]:
                        if sum([self.board[i + 1][j], self.board[i + 1][j + 1], self.board[i + 1][j - 1],
                                self.board[i][j + 1], self.board[i][j - 1]]) not in [2, 3]:
                            A[i][j] = 0
                    else:
                        if sum([self.board[i + 1][j], self.board[i + 1][j + 1], self.board[i + 1][j - 1],
                                self.board[i][j + 1], self.board[i][j - 1]]) == 3:
                            A[i][j] = 1

                elif i == self.height - 1 and 0 < j < self.width - 1:

                    if self.board[i][j]:
                        if sum([self.board[i - 1][j], self.board[i - 1][j + 1], self.board[i - 1][j - 1],
                                self.board[i][j + 1], self.board[i][j - 1]]) not in [2, 3]:
                            A[i][j] = 0
                    else:
                        if sum([self.board[i - 1][j], self.board[i - 1][j + 1], self.board[i - 1][j - 1],
                                self.board[i][j + 1], self.board[i][j - 1]]) == 3:
                            A[i][j] = 1

                elif 0 < i < self.height - 1 and not j:

                    if self.board[i][j]:
                        if sum([self.board[i + 1][j], self.board[i - 1][j], self.board[i + 1][j + 1],
                                self.board[i - 1][j + 1], self.board[i][j + 1]]) not in [2, 3]:
                            A[i][j] = 0
                    else:
                        if sum([self.board[i + 1][j], self.board[i - 1][j], self.board[i + 1][j + 1],
                                self.board[i - 1][j + 1], self.board[i][j + 1]]) == 3:
                            A[i][j] = 1

                elif 0 < i < self.height - 1 and j == self.width - 1:

                    if self.board[i][j]:
                        if sum([self.board[i - 1][j], self.board[i + 1][j], self.board[i - 1][j - 1],
                                self.board[i + 1][j - 1], self.board[i][j - 1]]) not in [2, 3]:
                            A[i][j] = 0
                    else:
                        if sum([self.board[i - 1][j], self.board[i + 1][j], self.board[i - 1][j - 1],
                                self.board[i + 1][j - 1], self.board[i][j - 1]]) == 3:
                            A[i][j] = 1

                else:

                    if self.board[i][j]:
                        if sum([self.board[i - 1][j - 1], self.board[i - 1][j], self.board[i - 1][j + 1],
                                self.board[i][j - 1], self.board[i][j + 1], self.board[i + 1][j - 1],
                                self.board[i + 1][j], self.board[i + 1][j + 1]]) not in [2, 3]:
                            A[i][j] = 0
                    else:
                        if sum([self.board[i - 1][j - 1], self.board[i - 1][j], self.board[i - 1][j + 1],
                                self.board[i][j - 1], self.board[i][j + 1], self.board[i + 1][j - 1],
                                self.board[i + 1][j], self.board[i + 1][j + 1]]) == 3:
                            A[i][j] = 1
        self.board = A



if __name__ == '__main__':
    # инициализация Pygame:
    pygame.init()
    # размеры окна:
    size = width, height = 500, 500
    # screen — холст, на котором нужно рисовать:
    screen = pygame.display.set_mode(size)
    # формирование кадра:
    # команды рисования на холсте
    pygame.display.set_caption('Игра «Жизнь»')

    board = Board(25, 25)
    board.set_view(0, 0, 20)
    running = True
    flag = False
    v = 10
    clock = pygame.time.Clock()
    while running:
        # внутри игрового цикла ещё один цикл
        # приема и обработки сообщений
        for event in pygame.event.get():
            # при закрытии окна
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and not flag:
                board.get_click(event.pos)
                board.render(screen)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    v = 20
                    if flag:
                        flag = False
                    else:
                        flag = True
            elif event.type == pygame.MOUSEWHEEL:
                if event.y > 0:
                    v += 10
                else:
                    if v == 10:
                        v = 3
                    elif v > 10:
                        v -= 10
        if flag:
            board.next_move()
            board.render(screen)
        board.render(screen)
        clock.tick(v)
        # обновление экрана
        pygame.display.flip()
    # завершение работы:
    pygame.quit()
