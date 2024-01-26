import pygame
import os
import sys


def load_image(name):
    fullname = os.path.join(name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


class Objects:
    def __init__(self):
        self.image_ConUp = [load_image(f"Вверх\КонВВ {str(i)}.png") for i in range(1, 18)]
        self.image_ConRight = [load_image(f"Право\КонПр {str(i)}.png") for i in range(1, 18)]
        self.image_ConLeft = [load_image(f"Лево\КонЛв {str(i)}.png") for i in range(1, 18)]
        self.image_ConDown = [load_image(f"Вниз\КонВн {str(i)}.png") for i in range(1, 18)]
        self.image_ConRight_Up = [load_image(f"Правый Поворот 2\КонПП {str(i)}.png") for i in range(1, 18)]
        self.image_ConLeft_Up = [load_image(f"Левый Поворот\КонЛП {str(i)}.png") for i in range(1, 18)]
        self.image_ConDown_Right = [pygame.transform.rotate(self.image_ConRight_Up[i], 270) for i in range(17)]
        self.image_ConLeft_Down = [pygame.transform.rotate(self.image_ConRight_Up[i], 180) for i in range(17)]
        self.image_ConUp_Left = [pygame.transform.rotate(self.image_ConRight_Up[i], 90) for i in range(17)]
        self.image_ConDown_Left = [pygame.transform.rotate(self.image_ConLeft_Up[i], 90) for i in range(17)]
        self.image_ConRight_Down = [pygame.transform.rotate(self.image_ConLeft_Up[i], 180) for i in range(17)]
        self.image_ConUp_Right = [pygame.transform.rotate(self.image_ConLeft_Up[i], 270) for i in range(17)]

        self.image_hub = load_image('Хаб.png')
        self.image_drill1 = [load_image(f"Бур\Бур {str(i)}.png") for i in range(1, 18)]
        self.image_drill2 = [pygame.transform.rotate(self.image_drill1[i], 270) for i in range(17)]
        self.image_drill3 = [pygame.transform.rotate(self.image_drill1[i], 180) for i in range(17)]
        self.image_drill4 = [pygame.transform.rotate(self.image_drill1[i], 90) for i in range(17)]

    def draw_drill(self, left, top, vector, pos, r):
        if vector == 0:
            if r == 0:
                screen.blit(self.image_drill1[pos], (left, top))
            elif r >= 1:
                screen.blit(list(reversed(self.image_drill1))[pos], (left, top))
        elif vector == 1:
            if r == 0:
                screen.blit(self.image_drill2[pos], (left, top))
            elif r >= 1:
                screen.blit(list(reversed(self.image_drill2))[pos], (left, top))
        elif vector == 2:
            if r == 0:
                screen.blit(self.image_drill3[pos], (left, top))
            elif r >= 1:
                screen.blit(list(reversed(self.image_drill3))[pos], (left, top))
        else:
            if r == 0:
                screen.blit(self.image_drill4[pos], (left, top))
            elif r >= 1:
                screen.blit(list(reversed(self.image_drill4))[pos], (left, top))

    def draw_figure_counting_platform(self, left, top):
        pygame.draw.rect(screen, 'dimgray', (left, top, 204, 204), 0)

    def menu_icon_for_objects_not_active(self):
        pygame.draw.circle(screen, (224, 238, 238), (1224, 357), 25, draw_top_left=True)
        pygame.draw.circle(screen, (224, 238, 238), (1224, 357), 25, draw_bottom_left=True)
        pygame.draw.line(screen, 'dimgray', (1207, 357), (1215, 344), 3)
        pygame.draw.line(screen, 'dimgray', (1207, 357), (1215, 369), 3)

    def draw_hub(self):
        screen.blit(self.image_hub, (510, 255))
        pygame.draw.rect(screen, 'gray', (550, 295, 122, 122), 0)
        font = pygame.font.Font(None, 50)
        text = font.render(str(board.hub.count), True, 'black')
        text_x = width // 2 - text.get_width() // 2
        text_y = height // 2 - text.get_height() // 2
        screen.blit(text, (text_x, text_y))


    def menu_icon_for_objects_active(self):
        pygame.draw.rect(screen, (224, 238, 238), (1122, 204, 102, 306), 0)
        pygame.draw.rect(screen, (224, 238, 238), (1071, 255, 51, 204), 0)
        pygame.draw.circle(screen, (224, 238, 238), (1122, 255), 51, draw_top_left=True)
        pygame.draw.circle(screen, (224, 238, 238), (1122, 459), 51, draw_bottom_left=True)
        pygame.draw.circle(screen, (224, 238, 238), (1071, 357), 26, draw_top_left=True)
        pygame.draw.circle(screen, (224, 238, 238), (1071, 357), 26, draw_bottom_left=True)
        pygame.draw.line(screen, 'dimgray', (1055, 357), (1063, 344), 3)
        pygame.draw.line(screen, 'dimgray', (1055, 357), (1063, 369), 3)
        if board.board_menu_buttons[0]:
            pygame.draw.rect(screen, (105, 147, 255), (1086, 219, 61, 61), 0)
        elif board.board_menu_buttons[1]:
            pygame.draw.rect(screen, (105, 147, 255), (1158, 219, 61, 61), 0)
        self.draw_conveyor_down_up(1091, 224, 0)
        self.draw_drill(1163, 224, 0, 16, 0)
        pygame.draw.rect(screen, 'dimgray', (1091, 296, 51, 51), 0)
        pygame.draw.rect(screen, 'dimgray', (1091, 367, 51, 51), 0)
        pygame.draw.rect(screen, 'dimgray', (1091, 439, 51, 51), 0)
        pygame.draw.rect(screen, 'dimgray', (1163, 296, 51, 51), 0)
        pygame.draw.rect(screen, 'dimgray', (1163, 367, 51, 51), 0)
        pygame.draw.rect(screen, 'dimgray', (1163, 439, 51, 51), 0)

    def draw_conveyor_turn_right_up(self, left, top, pos):
        screen.blit(self.image_ConRight_Up[pos], (left, top))

    def draw_conveyor_turn_up_right(self, left, top, pos):
        screen.blit(self.image_ConUp_Right[pos], (left, top))

    def draw_conveyor_turn_left_up(self, left, top, pos):
        screen.blit(self.image_ConLeft_Up[pos], (left, top))

    def draw_conveyor_turn_up_left(self, left, top, pos):
        screen.blit(self.image_ConUp_Left[pos], (left, top))

    def draw_conveyor_turn_down_left(self, left, top, pos):
        screen.blit(self.image_ConDown_Left[pos], (left, top))

    def draw_conveyor_turn_left_down(self, left, top, pos):
        screen.blit(self.image_ConLeft_Down[pos], (left, top))

    def draw_conveyor_turn_down_right(self, left, top, pos):
         screen.blit(self.image_ConDown_Right[pos], (left, top))

    def draw_conveyor_turn_right_down(self, left, top, pos):
        screen.blit(self.image_ConRight_Down[pos], (left, top))

    def draw_conveyor_left_right(self, left, top, pos):
        screen.blit(self.image_ConRight[pos], (left, top))

    def draw_conveyor_right_left(self, left, top, pos):
        screen.blit(self.image_ConLeft[pos], (left, top))

    def draw_conveyor_down_up(self, left, top, pos):
        screen.blit(self.image_ConUp[pos], (left, top))

    def draw_conveyor_up_down(self, left, top, pos):
        screen.blit(self.image_ConDown[pos], (left, top))


class Hub:
    def __init__(self):
        self.ind = 0
        self.order_of_requests = ['круг', 'круг1']
        self.request_quantity = {'круг': 10, 'круг1': 10}
        self.count = self.request_quantity[self.order_of_requests[self.ind]]

    def delivery_calculation(self):
        if self.count > 0:
            self.count -= 1
        else:
            self.ind += 1
            self.ind %= len(self.order_of_requests)
            self.count = self.request_quantity[self.order_of_requests[self.ind]]
            if board.image_map != board.image_map2:
                board.image_map = board.image_map2
                list = [(1, 6), (1, 7), (1, 8), (2, 6), (2, 7), (2, 8), (3, 6), (3, 7), (0, 23), (0, 18), (0, 17),
                        (13, 23), (13, 22), (13, 21), (12, 23), (12, 22), (12, 21), (11, 23), (11, 22)]

                list_not_work = []
                for i in range(12, 17):
                    list_not_work.append((0, i))
                for i in range(13, 17):
                    list_not_work.append((1, i))
                list_not_work += [(0, 19), (0, 20), (0, 21), (2, 13), (2, 14), (2, 15), (6, 20), (6, 21), (3, 19),
                                  (3, 20), (3, 21), (3, 23), (2, 23), (4, 23), (5, 23), (7, 22), (8, 22), (7, 23),
                                  (8, 23), (9, 23), (4, 3), (4, 4), (4, 5), (11, 12), (12, 12), (13, 12), (12, 13),
                                  (13, 13), (13, 14)]
                for i in range(18, 22):
                    for j in range(2):
                        list_not_work.append((4 + j, i))
                for i in range(8):
                    for j in range(5, 14):
                        list_not_work.append((j, i))
                for i in range(7, 14):
                    list_not_work.append((i, 8))
                for i in range(9, 14):
                    list_not_work.append((i, 9))
                for i in range(2):
                    for j in range(10, 14):
                        list_not_work.append((j, 10 + i))

            else:
                board.image_map = board.image_map1
                list = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (13, 12), (13, 11)]

                list_not_work = []
                for i in range(7, 24):
                    list_not_work.append((0, i))
                for i in range(8, 24):
                    list_not_work.append((1, i))
                for i in range(9, 24):
                    list_not_work.append((2, i))
                for i in range(15, 24):
                    list_not_work.append((3, i))
                for i in range(2):
                    for j in range(17, 24):
                        list_not_work.append((4 + i, j))
                for i in range(18, 24):
                    list_not_work.append((6, i))
                for i in range(19, 24):
                    list_not_work.append((7, i))
                for i in range(21, 24):
                    list_not_work.append((8, i))
                for j in range(4):
                    for i in range(5, 14):
                        list_not_work.append((i, j))
                for j in range(2):
                    for i in range(8, 14):
                        list_not_work.append((i, 4 + j))
                list_not_work += [(8, 4), (12, 8), (13, 9), (13, 8)]
                for j in range(2):
                    for i in range(11, 14):
                        list_not_work.append((i, 6 + j))

            board.board = [[[0, True, 0, 'ноль'] for _ in range(board.width)] for _ in range(board.height)]
            for i in range(4):
                for j in range(4):
                    board.board[5 + i][10 + j] = [13, True]
            for i in list:
                board.board[i[0]][i[1]][3] = 'круг'
            for i in list_not_work:
                board.board[i[0]][i[1]][0] = 18


class Board:
    def __init__(self, width, height):
        self.list = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (13, 12), (13, 11)]
        self.conveyor_length_argument = []

        self.list_not_work = []
        for i in range(7, 24):
            self.list_not_work.append((0, i))
        for i in range(8, 24):
            self.list_not_work.append((1, i))
        for i in range(9, 24):
            self.list_not_work.append((2, i))
        for i in range(15, 24):
            self.list_not_work.append((3, i))
        for i in range(2):
            for j in range(17, 24):
                self.list_not_work.append((4 + i, j))
        for i in range(18, 24):
            self.list_not_work.append((6, i))
        for i in range(19, 24):
            self.list_not_work.append((7, i))
        for i in range(21, 24):
            self.list_not_work.append((8, i))
        for j in range(4):
           for i in range(5, 14):
                self.list_not_work.append((i, j))
        for j in range(2):
            for i in range(8, 14):
                self.list_not_work.append((i, 4 + j))
        self.list_not_work += [(8, 4), (12, 8), (13, 9), (13, 8)]
        for j in range(2):
            for i in range(11, 14):
                self.list_not_work.append((i, 6 + j))

        self.board_menu_buttons = [False, False, False, False, True, False, False, False]
        self.product_of_production = []
        self.objects = Objects()
        self.width = width
        self.height = height
        self.board = [[[0, True, 0, 'ноль'] for _ in range(width)] for _ in range(height)]
        for i in range(4):
            for j in range(4):
                self.board[5 + i][10 + j] = [13, True]
        for i in self.list:
            self.board[i[0]][i[1]][3] = 'круг'
        for i in self.list_not_work:
            self.board[i[0]][i[1]][0] = 18
        self.board2 = [[] * width for _ in range(height)]

        self.list_turn_down_right = [(26, 50), (26, 49), (26, 48), (26, 47), (27, 46), (27, 45), (27, 44), (27, 43),
                                    (28, 42), (28, 41), (29, 40), (29, 39), (30, 38), (30, 37), (31, 36), (32, 35),
                                    (33, 34), (34, 33), (35, 32), (36, 31), (37, 30), (38, 30), (39, 29), (40, 29),
                                    (41, 28), (42, 28), (43, 27), (44, 27), (45, 27), (46, 27), (47, 26), (48, 26),
                                    (49, 26), (50, 26)]
        self.list_turn_right_down = list(reversed(self.list_turn_down_right))
        self.list_turn_left_down = [(0, 26), (1, 26), (2, 26), (3, 26), (4, 27), (5, 27), (6, 27), (7, 27), (8, 28),
                                    (9, 28), (10, 29), (11, 29), (12, 30), (13, 30), (14, 31), (15, 32), (16, 33),
                                    (17, 34), (18, 35), (19, 36), (20, 37), (20, 38), (21, 39), (21, 40), (22, 41),
                                    (22, 42), (23, 43), (23, 44), (23, 45), (23, 46), (24, 47), (24, 48), (24, 49),
                                    (24, 50)]
        self.list_turn_down_left = list(reversed(self.list_turn_left_down))
        self.list_turn_up_left = [(24, 0), (24, 1), (24, 2), (24, 3), (23, 4), (23, 5), (23, 6), (23, 7), (22, 8),
                                   (22, 9), (21, 10), (21, 11), (20, 12), (20, 13), (19, 14), (18, 15), (17, 16),
                                   (16, 17), (15, 18), (14, 19), (13, 20), (12, 20), (11, 21), (10, 21), (9, 22),
                                   (8, 22), (7, 23), (6, 23), (5, 23), (4, 23), (3, 24), (2, 24), (1, 24), (0, 24)]
        self.list_turn_left_up = list(reversed(self.list_turn_up_left))
        self.list_turn_right_up = [(50, 24), (49, 24), (48, 24), (47, 24), (46, 23), (45, 23), (44, 23), (43, 23),
                                   (42, 22), (41, 22), (40, 21), (39, 21), (38, 20), (37, 20), (36, 19), (35, 18),
                                   (34, 17), (33, 16), (32, 15), (31, 14), (30, 13), (30, 12), (29, 11), (29, 10),
                                   (28, 9), (28, 8), (27, 7), (27, 6), (27, 5), (27, 4), (26, 3), (26, 2), (26, 1),
                                   (26, 0)]
        self.list_turn_up_right = list(reversed(self.list_turn_right_up))

        self.left = 0
        self.top = 0
        self.cell_size = 51
        self.image_map1 = load_image('карта 1.png')
        self.image_map2 = load_image('карта 2.png')
        self.image_map = load_image('карта 1.png')
        self.hub = Hub()
        self.interface_menu = False

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, v1, v2):
        c = self.cell_size
        left = self.left
        top = self.top
        products = []
        s = v1
        screen.blit(self.image_map, (left, top))
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                v1 = s
                pygame.draw.rect(screen, (169, 169, 169), (left + j * c, top + i * c, c, c), 1)
                if not self.board[i][j][1]:
                    v1 = 0
                if self.board[i][j][0] == 5:
                    self.objects.draw_conveyor_turn_down_left(left + j * c, top + i * c, v1)
                elif self.board[i][j][0] == 6:
                    self.objects.draw_conveyor_turn_right_down(left + j * c, top + i * c, v1)
                elif self.board[i][j][0] == 7:
                    self.objects.draw_conveyor_turn_down_right(left + j * c, top + i * c, v1)
                elif self.board[i][j][0] == 8:
                    self.objects.draw_conveyor_turn_left_down(left + j * c, top + i * c, v1)
                elif self.board[i][j][0] == 9:
                    self.objects.draw_conveyor_turn_up_right(left + j * c, top + i * c, v1)
                elif self.board[i][j][0] == 10:
                    self.objects.draw_conveyor_turn_up_left(left + j * c, top + i * c, v1)
                elif self.board[i][j][0] == 11:
                    self.objects.draw_conveyor_turn_left_up(left + j * c, top + i * c, v1)
                elif self.board[i][j][0] == 12:
                    self.objects.draw_conveyor_turn_right_up(left + j * c, top + i * c, v1)
                elif 13 < self.board[i][j][0] < 18:
                    self.board[i][j][2] += 1
                    products.append((i, j))
                elif self.board[i][j][0] == 4:
                    self.objects.draw_conveyor_right_left(left + j * c, top + i * c, v1)
                elif self.board[i][j][0] == 3:
                    self.objects.draw_conveyor_up_down(left + j * c, top + i * c, v1)
                elif self.board[i][j][0] == 2:
                    self.objects.draw_conveyor_left_right(left + j * c, top + i * c, v1)
                elif self.board[i][j][0] == 1:
                    self.objects.draw_conveyor_down_up(left + j * c, top + i * c, v1)
        if products or self.product_of_production:
            self.get_drills_work(products, v1, v2)
        self.objects.draw_hub()

    def get_click(self, mouse_pos, num):
        if num == 1:
           self.cell = self.get_cell(mouse_pos, 1)
           if self.cell:
               self.on_click(mouse_pos)
        elif num == 3:
           self.delete(mouse_pos)

    def get_cell(self, mouse_pos, num):
        if num:
            if self.interface_menu:
                if mouse_pos[0] >= 1071 and 204 <= mouse_pos[1] <= 510:
                    if 1091 <= mouse_pos[0] <= 1214 and 224 <= mouse_pos[1] <= 490 and num == 1:
                        if 1091 <= mouse_pos[0] <= 1142 and 224 <= mouse_pos[1] <= 275:
                            if self.board_menu_buttons[0]:
                                self.board_menu_buttons[0] = False
                            else:
                                self.board_menu_buttons = [False, False, False, False, False, False, False, False]
                                self.board_menu_buttons[0] = True
                        elif 1163 <= mouse_pos[0] <= 1214 and 224 <= mouse_pos[1] <= 275:
                            if self.board_menu_buttons[1]:
                                self.board_menu_buttons[1] = False
                            else:
                                self.board_menu_buttons = [False, False, False, False, False, False, False, False]
                                self.board_menu_buttons[1] = True
                        return None
                    else:
                        if mouse_pos[0] > 1223:
                            mouse_pos = 1199, mouse_pos[1]
                        color = screen.get_at(mouse_pos)
                        if color == (224, 238, 238, 255) or color == (105, 105, 105, 255):
                            return None
                else:
                    if 1046 <= mouse_pos[0] < 1071 and 332 <= mouse_pos[1] <= 383:
                        color = screen.get_at(mouse_pos)
                        if num == 1 and (color == (224, 238, 238, 255) or color == (105, 105, 105, 255)):
                            self.interface_menu = False
                            return None
            else:
                usl3 = mouse_pos[0] >= 1199 and 332 <= mouse_pos[1] <= 383
                if usl3:
                    if num == 3:
                        return None
                    if mouse_pos[0] > 1223:
                        mouse_pos = 1223, mouse_pos[1]
                    color = screen.get_at(mouse_pos)
                    if color == (224, 238, 238, 255) or color == (105, 105, 105, 255):
                        self.interface_menu = True
                        return None
        c = self.cell_size
        usl1 = self.left <= mouse_pos[0] < self.left + c * len(self.board[0])
        usl2 = self.top <= mouse_pos[1] < self.top + c * len(self.board)
        if usl1 and usl2:
            pos_left = int((mouse_pos[0] - self.left) // c)
            pos_top = int((mouse_pos[1] - self.top) // c)
        elif mouse_pos[0] >= self.left + c * len(self.board[0]) and mouse_pos[1] < self.top + c * len(self.board):
            pos_left = 23
            pos_top = int((mouse_pos[1] - self.top) // c)
        elif mouse_pos[0] < self.left + c * len(self.board[0]) and mouse_pos[1] >= self.top + c * len(self.board):
            pos_left = int((mouse_pos[0] - self.left) // c)
            pos_top = 13
        else:
            pos_left = 23
            pos_top = 13
        if self.board[pos_top][pos_left][0] not in [13, 18] or not num:
            return pos_left, pos_top

    def on_click(self, mouse_pos):
        if self.board_menu_buttons[0]:
           self.conveyor_length_argument = []
           self.comparison_original_point(mouse_pos)
        if self.board_menu_buttons[1]:
            self.draw_drill(mouse_pos)

    def comparison_original_point(self, mouse_pos2):
        cell2 = self.get_cell(mouse_pos2, 1)
        if self.cell:
           x, y = self.cell
        if self.cell == cell2 and cell2 and self.cell:
            vector = [1, 2, 3, 4]

            usl1 = x != 0 and self.board[y][x - 1][0] in (2, 7, 9, 15)
            usl2 = x != 23 and self.board[y][x + 1][0] in (4, 5, 10, 17)
            usl3 = y != 13 and self.board[y + 1][x][0] in (1, 11, 12, 14)
            usl4 = y != 0 and self.board[y - 1][x][0] in (3, 6, 8, 16)
            if usl1 or usl2 or usl3 or usl4:
                vector_nearby = {'usl1': [11, 2, 8, 4], 'usl2': [12, 2, 6, 4],
                                 'usl3': [1, 7, 3, 5], 'usl4': [1, 9, 3, 10]}
                if x < 12 and y < 7:
                    vector = vector_nearby['usl1']
                    if usl2:
                        vector = vector_nearby['usl2']
                    elif usl3:
                        vector = vector_nearby['usl3']
                    elif usl4:
                        vector = vector_nearby['usl4']
                elif x >= 12 and y < 7:
                    vector = vector_nearby['usl4']
                    if usl3:
                        vector = vector_nearby['usl3']
                    elif usl2:
                        vector = vector_nearby['usl2']
                    elif usl1:
                        vector = vector_nearby['usl1']
                elif x < 12 and y >= 7:
                    vector = vector_nearby['usl3']
                    if usl4:
                        vector = vector_nearby['usl4']
                    elif usl1:
                        vector = vector_nearby['usl1']
                    elif usl2:
                        vector = vector_nearby['usl2']
                else:
                    vector = vector_nearby['usl2']
                    if usl1:
                        vector = vector_nearby['usl1']
                    elif usl4:
                        vector = vector_nearby['usl4']
                    elif usl3:
                        vector = vector_nearby['usl3']
            x2, y2 = mouse_pos2
            x2 %= 51
            y2 %= 51
            if x2 != y2 and x2 + y2 != 50:
                if y2 > 25:
                    self.board[y][x][:2] = [vector[2], False]
                    if x2 > 25 and y2 % 26 < x2 % 26:
                        self.board[y][x][:2] = [vector[1], False]
                    elif x2 < 25 and y2 % 26 + x2 < 25:
                        self.board[y][x][:2] = [vector[3], False]
                elif y2 < 25:
                    self.board[y][x][:2] = [vector[0], False]
                    if x2 > 25 and y2 + x2 % 26 > 25:
                        self.board[y][x][:2] = [vector[1], False]
                    elif x2 < 25 and y2 > x2:
                        self.board[y][x][:2] = [vector[3], False]
                else:
                    if x2 > 25:
                        self.board[y][x][:2] = [vector[1], False]
                    else:
                        self.board[y][x][:2] = [vector[2], False]
            else:
                if y2 >= 25 and x2 >= 25:
                    self.board[y][x][:2] = [vector[2], False]
                elif y2 >= 25 and x2 < 25:
                    self.board[y][x][:2] = [vector[3], False]
                elif y2 < 25 and x2 >= 25:
                    self.board[y][x][:2] = [vector[1], False]
                else:
                    self.board[y][x][:2] = [vector[0], False]
            if self.conveyor_length_argument:
                for i in self.conveyor_length_argument:
                    self.board[i[0]][i[1]][:2] = [0, True]
            self.conveyor_length_argument = []
        else:
            if cell2 and self.cell:
                st = ()
                if cell2[1] < y and cell2[0] == x and self.board[y][x][0] in (1, 11, 12):
                    st = (cell2[1], x, 1)
                elif cell2[1] > y and cell2[0] == x and self.board[y][x][0] in (3, 6, 8):
                    st = (cell2[1], x, 3)
                elif cell2[1] == y and cell2[0] > x and self.board[y][x][0] in (2, 7, 9):
                    st = (y, cell2[0], 2)
                elif cell2[1] == y and cell2[0] < x and self.board[y][x][0] in (4, 5, 10):
                    st = (y, cell2[0], 4)
                if st:
                    if st not in self.conveyor_length_argument[:-1]:
                        if st[2] == 1 or st[2] == 3:
                            for i in range(min(y, st[0]), max(y, st[0]) + 1):
                                if self.board[i][x][:2] != [st[2], False] and self.board[i][x][0] != self.board[y][x][0]:
                                    if self.board[i][x][0] not in [13, 18]:
                                        self.board[i][x][:2] = [st[2], False]
                                        self.conveyor_length_argument.append((i, x, st[2]))
                        else:
                            for i in range(min(x, st[1]), max(x, st[1]) + 1):
                                if self.board[y][i][:2] != [st[2], False] and self.board[y][i][0] != self.board[y][x][0]:
                                    if self.board[y][i][0] not in [13, 18]:
                                        self.board[y][i][:2] = [st[2], False]
                                        self.conveyor_length_argument.append((y, i, st[2]))
                    else:
                        for i in list(reversed(self.conveyor_length_argument)):
                            if i != st:
                                self.board[i[0]][i[1]][:2] = [0, True]
                            else:
                                s = self.conveyor_length_argument
                                self.conveyor_length_argument = s[:s.index(i) + 1]
                                break

    def get_work_conveyor(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j][0] != 13:
                   self.board[i][j][1] = True

    def draw_drill(self, mouse_pos2):
        cell2 = self.get_cell(mouse_pos2, 1)
        if cell2 and self.cell:
            x, y = self.cell
            if self.cell == cell2:
                vector = [14, 15, 16, 17]
                x2, y2 = mouse_pos2
                x2 %= 51
                y2 %= 51
                if x2 != y2 and x2 + y2 != 50:
                    if y2 > 25:
                        self.board[y][x][:2] = [vector[2], False]
                        if x2 > 25 and y2 % 26 < x2 % 26:
                            self.board[y][x][:2] = [vector[1], False]
                        elif x2 < 25 and y2 % 26 + x2 < 24:
                            self.board[y][x][:2] = [vector[3], False]
                    elif y2 < 25:
                        self.board[y][x][:2] = [vector[0], False]
                        if x2 > 25 and y2 + x2 % 26 > 24:
                            self.board[y][x][:2] = [vector[1], False]
                        elif x2 < 25 and y2 > x2:
                            self.board[y][x][:2] = [vector[3], False]
                    else:
                        if x2 > 25:
                            self.board[y][x][:2] = [vector[1], False]
                        else:
                            self.board[y][x][:2] = [vector[2], False]
                else:
                    if y2 >= 25 and x2 >= 25:
                        self.board[y][x][:2] = [vector[2], False]
                    elif y2 >= 25 and x2 < 25:
                        self.board[y][x][:2] = [vector[3], False]
                    elif y2 < 25 and x2 >= 25:
                        self.board[y][x][:2] = [vector[1], False]
                    else:
                        self.board[y][x][:2] = [vector[0], False]
            else:
                self.board[y][x][0] = 0
                self.cell = cell2[0], cell2[1]

    def get_drills_work(self, drills, pos, r):
        for i in drills:
            if self.board[i[0]][i[1]][2] == 1000 and self.board[i[0]][i[1]][-1] != 'ноль':
                i1 = i[0] * self.cell_size + self.cell_size // 2
                i2 = i[1] * self.cell_size + self.cell_size // 2
                self.product_of_production.append([i2, i1, self.board[i[0]][i[1]][-1]])
                self.board[i[0]][i[1]][2] %= 1000
        del_list = []
        for i in range(len(self.product_of_production)):
            x, y = self.get_cell((int(self.product_of_production[i][0]), int(self.product_of_production[i][1])), 0)
            if self.board[y][x][0] in [1, 14]:
                st1 = self.product_of_production[i][0]
                st2 = self.product_of_production[i][1]
                cell_with_meaning = self.product_of_production[i][2]
                f = True
                for j in self.product_of_production:
                    x1, y1 = self.get_cell((int(j[0]), int(j[1])), 0)
                    if (x1 == x and y1 == y) or (y1 == y - 1 and x1 == x and self.board[y1][x1][0] == 1):
                        if int(j[0]) == int(st1) and int(j[1]) == int(st2) - 24:
                            f = False
                            break
                    else:
                        if y1 == y - 1 and x1 == x and self.board[y1][x1][0] in [7, 5]:
                            ind = 0
                            if (int(j[0]) % 51, int(j[1]) % 51) in self.list_turn_down_right:
                                 ind = self.list_turn_down_right.index((int(j[0]) % 51, int(j[1]) % 51))
                            if (int(j[0]) % 51, int(j[1]) % 51) in self.list_turn_down_left:
                                 ind = self.list_turn_down_left.index((int(j[0]) % 51, int(j[1]) % 51))
                            if ind < 20 and int(j[1]) == int(st2) - 24:
                                f = False
                                break
                            elif 20 <= ind < 22 and int(j[1]) == int(st2) - 23:
                                f = False
                                break
                            elif 22 <= ind < 24 and int(j[1]) == int(st2) - 22:
                                f = False
                                break
                            elif ind == 24 and int(j[1]) == int(st2) - 21:
                                f = False
                                break
                if f:
                    if int(st2 * 10 - 1) % 510 != 1:
                        st2 = int(st2 * 10 - 1) / 10
                    elif y != 0 and self.board[y - 1][x][0] in [1, 13]:
                        st2 = int(st2 * 10 - 1) / 10
                    elif y != 0 and self.board[y - 1][x][0] == 7:
                        st1 = int(st1) // 51 * 51 + self.list_turn_down_right[0][0]
                        st2 = (int(st2) // 51 - 1) * 51 + self.list_turn_down_right[0][1]
                    elif y != 0 and self.board[y - 1][x][0] == 5:
                        st1 = int(st1) // 51 * 51 + self.list_turn_down_left[0][0]
                        st2 = (int(st2) // 51 - 1) * 51 + self.list_turn_down_left[0][1]
                        '''
                        if (y - 1, x) not in self.board2:
                            self.board2[(x, y - 1)] = {(st1, st2)}
                        else:
                            self.board2[(x, y - 1)].add({(st1, st2)})'''
                self.product_of_production[i] = (st1, st2, cell_with_meaning)

            elif self.board[y][x][0] in [7]:
                st1 = self.product_of_production[i][0]
                st2 = self.product_of_production[i][1]
                cell_with_meaning = self.product_of_production[i][2]
                if (int(st1) % 51, int(st2) % 51) not in self.list_turn_down_right:
                    st1 = int(st1) // 51 * 51 + self.list_turn_down_right[0][0]
                    st2 = int(st2) // 51 * 51 + self.list_turn_down_right[0][1]
                else:
                    c1 = self.list_turn_down_right.index((int(st1) % 51, int(st2) % 51))
                    f = True
                    for j in self.product_of_production:
                        x1, y1 = self.get_cell((int(j[0]), int(j[1])), 0)
                        if x1 == x and y1 == y:
                            if (int(j[0]) % 51, int(j[1]) % 51) in self.list_turn_down_right:
                                if self.list_turn_down_right.index((int(j[0]) % 51, int(j[1]) % 51)) - 21 == c1:
                                    f = False
                                    break
                        else:
                            if x1 == x + 1 and y1 == y and self.board[y1][x1][0] == 2:
                                if c1 > 14 and int(j[0]) == int(st1) + 24:
                                    f = False
                                    break
                                elif 12 < c1 <= 14 and int(j[0]) == int(st1) + 23:
                                    f = False
                                    break
                                elif 10 < c1 <= 12 and int(j[0]) == int(st1) + 22:
                                    f = False
                                    break
                                elif c1 == 10 and int(j[0]) == int(st1) + 21:
                                    f = False
                                    break
                            elif x1 == x + 1 and y1 == y and self.board[y1][x1][0] in [8, 11]:
                                ind = 0
                                if (int(j[0]) % 51, int(j[1]) % 51) in self.list_turn_left_down:
                                    ind = self.list_turn_left_down.index((int(j[0]) % 51, int(j[1]) % 51))
                                if (int(j[0]) % 51, int(j[1]) % 51) in self.list_turn_left_up:
                                    ind = self.list_turn_left_up.index((int(j[0]) % 51, int(j[1]) % 51))
                                if ind < 20:
                                    if c1 > 14 and int(j[0]) == int(st1) + 24:
                                        f = False
                                        break
                                    elif 12 < c1 <= 14 and int(j[0]) == int(st1) + 23:
                                        f = False
                                        break
                                    elif 10 < c1 <= 12 and int(j[0]) == int(st1) + 22:
                                        f = False
                                        break
                                    elif c1 == 10 and int(j[0]) == int(st1) + 21:
                                        f = False
                                        break
                                elif 20 <= ind < 22:
                                    if c1 > 14 and int(j[0]) == int(st1) + 23:
                                        f = False
                                        break
                                    elif 12 < c1 <= 14 and int(j[0]) == int(st1) + 22:
                                        f = False
                                        break
                                    elif 10 < c1 <= 12 and int(j[0]) == int(st1) + 21:
                                        f = False
                                        break
                                    elif c1 == 10 and int(j[0]) == int(st1) + 20:
                                        f = False
                                        break
                                elif 22 <= ind < 24:
                                    if c1 > 14 and int(j[0]) == int(st1) + 22:
                                        f = False
                                        break
                                    elif 12 < c1 <= 14 and int(j[0]) == int(st1) + 21:
                                        f = False
                                        break
                                    elif 10 < c1 <= 12 and int(j[0]) == int(st1) + 20:
                                        f = False
                                        break
                                    elif c1 == 10 and int(j[0]) == int(st1) + 19:
                                        f = False
                                        break
                                elif ind == 24:
                                    if c1 > 14 and int(j[0]) == int(st1) + 21:
                                        f = False
                                        break
                                    elif 12 < c1 <= 14 and int(j[0]) == int(st1) + 20:
                                        f = False
                                        break
                                    elif 10 < c1 <= 12 and int(j[0]) == int(st1) + 19:
                                        f = False
                                        break
                                    elif c1 == 10 and int(j[0]) == int(st1) + 18:
                                        f = False
                                        break

                    if f:
                        if int(st1 * 10) % 10 != 9:
                            st1 = (int(st1 * 10) + 1) / 10
                        else:
                            if c1 + 1 != len(self.list_turn_down_right):
                                st1 = int(st1) // 51 * 51 + self.list_turn_down_right[c1 + 1][0]
                                st2 = int(st2) // 51 * 51 + self.list_turn_down_right[c1 + 1][1]
                            else:
                                if x != 13 and self.board[y][x + 1][0] in [2, 13]:
                                    st1 = (int(st1 * 10) + 1) / 10
                                elif x != 23 and self.board[y][x + 1][0] == 8:
                                    st1 = (int(st1) // 51 + 1) * 51 + self.list_turn_left_down[0][0]
                                    st2 = int(st2) // 51 * 51 + self.list_turn_left_down[0][1]
                                elif x != 23 and self.board[y][x + 1][0] == 11:
                                    st1 = (int(st1) // 51 + 1) * 51 + self.list_turn_left_up[0][0]
                                    st2 = int(st2) // 51 * 51 + self.list_turn_left_up[0][1]
                self.product_of_production[i] = (st1, st2, cell_with_meaning)

            elif self.board[y][x][0] in [5]:
                st1 = self.product_of_production[i][0]
                st2 = self.product_of_production[i][1]
                cell_with_meaning = self.product_of_production[i][2]
                if (int(st1) % 51, int(st2) % 51) not in self.list_turn_down_left:
                    st1 = int(st1) // 51 * 51 + self.list_turn_down_left[0][0] + 0.9
                    st2 = int(st2) // 51 * 51 + self.list_turn_down_left[0][1] + 0.9
                else:
                    c1 = self.list_turn_down_left.index((int(st1) % 51, int(st2) % 51))
                    f = True
                    for j in self.product_of_production:
                        x1, y1 = self.get_cell((int(j[0]), int(j[1])), 0)
                        if x1 == x and y1 == y:
                            if (int(j[0]) % 51, int(j[1]) % 51) in self.list_turn_down_left:
                                if self.list_turn_down_left.index((int(j[0]) % 51, int(j[1]) % 51)) - 21 == c1:
                                    f = False
                                    break
                        else:
                            if x1 == x - 1 and y1 == y and self.board[y1][x1][0] == 4:
                                if c1 > 14 and int(j[0]) == int(st1) - 24:
                                    f = False
                                    break
                                elif 12 < c1 <= 14 and int(j[0]) == int(st1) - 23:
                                    f = False
                                    break
                                elif 10 < c1 <= 12 and int(j[0]) == int(st1) - 22:
                                    f = False
                                    break
                                elif c1 == 10 and int(j[0]) == int(st1) - 21:
                                    f = False
                                    break
                            elif x1 == x - 1 and y1 == y and self.board[y1][x1][0] in [6, 12]:
                                ind = 0
                                if (int(j[0]) % 51, int(j[1]) % 51) in self.list_turn_right_down:
                                    ind = self.list_turn_right_down.index((int(j[0]) % 51, int(j[1]) % 51))
                                if (int(j[0]) % 51, int(j[1]) % 51) in self.list_turn_right_up:
                                    ind = self.list_turn_right_up.index((int(j[0]) % 51, int(j[1]) % 51))
                                if ind < 20:
                                    if c1 > 14 and int(j[0]) == int(st1) - 24:
                                        f = False
                                        break
                                    elif 12 < c1 <= 14 and int(j[0]) == int(st1) - 23:
                                        f = False
                                        break
                                    elif 10 < c1 <= 12 and int(j[0]) == int(st1) - 22:
                                        f = False
                                        break
                                    elif c1 == 10 and int(j[0]) == int(st1) - 21:
                                        f = False
                                        break
                                elif 20 <= ind < 22:
                                    if c1 > 14 and int(j[0]) == int(st1) - 23:
                                        f = False
                                        break
                                    elif 12 < c1 <= 14 and int(j[0]) == int(st1) - 22:
                                        f = False
                                        break
                                    elif 10 < c1 <= 12 and int(j[0]) == int(st1) - 21:
                                        f = False
                                        break
                                    elif c1 == 10 and int(j[0]) == int(st1) - 20:
                                        f = False
                                        break
                                elif 22 <= ind < 24:
                                    if c1 > 14 and int(j[0]) == int(st1) - 22:
                                        f = False
                                        break
                                    elif 12 < c1 <= 14 and int(j[0]) == int(st1) - 21:
                                        f = False
                                        break
                                    elif 10 < c1 <= 12 and int(j[0]) == int(st1) - 20:
                                        f = False
                                        break
                                    elif c1 == 10 and int(j[0]) == int(st1) - 19:
                                        f = False
                                        break
                                elif ind == 24:
                                    if c1 > 14 and int(j[0]) == int(st1) - 21:
                                        f = False
                                        break
                                    elif 12 < c1 <= 14 and int(j[0]) == int(st1) - 20:
                                        f = False
                                        break
                                    elif 10 < c1 <= 12 and int(j[0]) == int(st1) - 19:
                                        f = False
                                        break
                                    elif c1 == 10 and int(j[0]) == int(st1) - 18:
                                        f = False
                                        break
                    if f:
                        if int(st1 * 10) % 10 != 0:
                            st1 = (int(st1 * 10) - 1) / 10
                        else:
                            if c1 + 1 != len(self.list_turn_down_left):
                                st1 = int(st1) // 51 * 51 + self.list_turn_down_left[c1 + 1][0] + 0.9
                                st2 = int(st2) // 51 * 51 + self.list_turn_down_left[c1 + 1][1] + 0.9
                            else:
                                if x != 0 and self.board[y][x - 1][0] in [4, 13]:
                                    st1 = (int(st1 * 10) - 1) / 10
                                elif x != 0 and self.board[y][x - 1][0] == 6:
                                    st1 = (int(st1) // 51 - 1) * 51 + self.list_turn_right_down[0][0]
                                    st2 = int(st2) // 51 * 51 + self.list_turn_right_down[0][1]
                                elif x != 0 and self.board[y][x - 1][0] == 12:
                                    st1 = (int(st1) // 51 - 1) * 51 + self.list_turn_right_up[0][0]
                                    st2 = int(st2) // 51 * 51 + self.list_turn_right_up[0][1]
                self.product_of_production[i] = (st1, st2, cell_with_meaning)

            elif self.board[y][x][0] in [2, 15]:
                st1 = self.product_of_production[i][0]
                st2 = self.product_of_production[i][1]
                cell_with_meaning = self.product_of_production[i][2]
                f = True
                for j in self.product_of_production:
                    x1, y1 = self.get_cell((int(j[0]), int(j[1])), 0)
                    if (x1 == x and y1 == y) or (y1 == y and x1 == x + 1 and self.board[y1][x1][0] == 2):
                        if int(j[0]) == int(st1) + 24 and int(j[1]) == int(st2):
                            f = False
                            break
                    else:
                        if x1 == x + 1 and y1 == y and self.board[y1][x1][0] in [8, 11]:
                            ind = 0
                            if (int(j[0]) % 51, int(j[1]) % 51) in self.list_turn_left_down:
                                ind = self.list_turn_left_down.index((int(j[0]) % 51, int(j[1]) % 51))
                            if (int(j[0]) % 51, int(j[1]) % 51) in self.list_turn_left_up:
                                ind = self.list_turn_left_up.index((int(j[0]) % 51, int(j[1]) % 51))
                            if ind < 20 and int(j[0]) == int(st1) + 24:
                                f = False
                                break
                            elif 20 <= ind < 22 and int(j[0]) == int(st1) + 23:
                                f = False
                                break
                            elif 22 <= ind < 24 and int(j[0]) == int(st1) + 22:
                                f = False
                                break
                            elif ind == 24 and int(j[0]) == int(st1) + 21:
                                f = False
                                break
                if f:
                    if int(st1 * 10 + 1) % 510 != 509:
                        st1 = int(st1 * 10 + 1) / 10
                    elif x != 23 and self.board[y][x + 1][0] in [2, 13]:  # int(st2 * 10 - 1) % 500 != self.cell_size // 2
                        st1 = int(st1 * 10 + 1) / 10
                    elif x != 23 and self.board[y][x + 1][0] == 8:
                        st1 = (int(st1) // 51 + 1) * 51 + self.list_turn_left_down[0][0]
                        st2 = int(st2) // 51 * 51 + self.list_turn_left_down[0][1]
                    elif x != 23 and self.board[y][x + 1][0] == 11:
                        st1 = (int(st1) // 51 + 1) * 51 + self.list_turn_left_up[0][0]
                        st2 = int(st2) // 51 * 51 + self.list_turn_left_up[0][1]
                self.product_of_production[i] = (st1, st2, cell_with_meaning)

            elif self.board[y][x][0] in [11]:
                st1 = self.product_of_production[i][0]
                st2 = self.product_of_production[i][1]
                cell_with_meaning = self.product_of_production[i][2]
                if (int(st1) % 51, int(st2) % 51) not in self.list_turn_left_up:
                    st1 = int(st1) // 51 * 51 + self.list_turn_left_up[0][0] + 0.9
                    st2 = int(st2) // 51 * 51 + self.list_turn_left_up[0][1] + 0.9
                else:
                    c1 = self.list_turn_left_up.index((int(st1) % 51, int(st2) % 51))
                    f = True
                    for j in self.product_of_production:
                        x1, y1 = self.get_cell((int(j[0]), int(j[1])), 0)
                        if x1 == x and y1 == y:
                            if (int(j[0]) % 51, int(j[1]) % 51) in self.list_turn_left_up:
                                if self.list_turn_left_up.index((int(j[0]) % 51, int(j[1]) % 51)) - 21 == c1:
                                    f = False
                                    break
                        else:
                            if x1 == x and y1 == y - 1 and self.board[y1][x1][0] == 1:
                                if c1 > 14 and int(j[1]) == int(st2) - 24:
                                    f = False
                                    break
                                elif 12 < c1 <= 14 and int(j[1]) == int(st2) - 23:
                                    f = False
                                    break
                                elif 10 < c1 <= 12 and int(j[1]) == int(st2) - 22:
                                    f = False
                                    break
                                elif c1 == 10 and int(j[1]) == int(st2) - 21:
                                    f = False
                                    break
                            elif y1 == y - 1 and x1 == x and self.board[y1][x1][0] in [7, 5]:
                                ind = 0
                                if (int(j[0]) % 51, int(j[1]) % 51) in self.list_turn_down_right:
                                    ind = self.list_turn_down_right.index((int(j[0]) % 51, int(j[1]) % 51))
                                if (int(j[0]) % 51, int(j[1]) % 51) in self.list_turn_down_left:
                                    ind = self.list_turn_down_left.index((int(j[0]) % 51, int(j[1]) % 51))
                                if ind < 20:
                                    if c1 > 14 and int(j[1]) == int(st2) - 24:
                                        f = False
                                        break
                                    elif 12 < c1 <= 14 and int(j[1]) == int(st2) - 23:
                                        f = False
                                        break
                                    elif 10 < c1 <= 12 and int(j[1]) == int(st2) - 22:
                                        f = False
                                        break
                                    elif c1 == 10 and int(j[1]) == int(st2) - 21:
                                        f = False
                                        break
                                elif 20 <= ind < 22:
                                    if c1 > 14 and int(j[1]) == int(st2) - 23:
                                        f = False
                                        break
                                    elif 12 < c1 <= 14 and int(j[1]) == int(st2) - 22:
                                        f = False
                                        break
                                    elif 10 < c1 <= 12 and int(j[1]) == int(st2) - 21:
                                        f = False
                                        break
                                    elif c1 == 10 and int(j[1]) == int(st2) - 20:
                                        f = False
                                        break
                                elif 22 <= ind < 24:
                                    if c1 > 14 and int(j[1]) == int(st2) - 22:
                                        f = False
                                        break
                                    elif 12 < c1 <= 14 and int(j[1]) == int(st2) - 21:
                                        f = False
                                        break
                                    elif 10 < c1 <= 12 and int(j[1]) == int(st2) - 20:
                                        f = False
                                        break
                                    elif c1 == 10 and int(j[1]) == int(st2) - 19:
                                        f = False
                                        break
                                elif ind == 24:
                                    if c1 > 14 and int(j[1]) == int(st2) - 21:
                                        f = False
                                        break
                                    elif 12 < c1 <= 14 and int(j[1]) == int(st2) - 20:
                                        f = False
                                        break
                                    elif 10 < c1 <= 12 and int(j[1]) == int(st2) - 19:
                                        f = False
                                        break
                                    elif c1 == 10 and int(j[1]) == int(st2) - 18:
                                        f = False
                                        break
                    if f:
                        if int(st2 * 10) % 10 != 0:
                            st2 = (int(st2 * 10) - 1) / 10
                        else:
                            if c1 + 1 != len(self.list_turn_left_up):
                                st1 = int(st1) // 51 * 51 + self.list_turn_left_up[c1 + 1][0] + 0.9
                                st2 = int(st2) // 51 * 51 + self.list_turn_left_up[c1 + 1][1] + 0.9
                            else:
                                if y != 0 and self.board[y - 1][x][0] in [1, 13]:
                                    st2 = (int(st2 * 10) - 1) / 10
                                elif y != 0 and self.board[y - 1][x][0] == 7:
                                    st1 = int(st1) // 51 * 51 + self.list_turn_down_right[0][0]
                                    st2 = (int(st2) // 51 - 1) * 51 + self.list_turn_down_right[0][1]
                                elif y != 0 and self.board[y - 1][x][0] == 5:
                                    st1 = int(st1) // 51 * 51 + self.list_turn_down_left[0][0]
                                    st2 = (int(st2) // 51 - 1) * 51 + self.list_turn_down_left[0][1]
                self.product_of_production[i] = (st1, st2, cell_with_meaning)

            elif self.board[y][x][0] in [8]:
                st1 = self.product_of_production[i][0]
                st2 = self.product_of_production[i][1]
                cell_with_meaning = self.product_of_production[i][2]
                if (int(st1) % 51, int(st2) % 51) not in self.list_turn_left_down:
                    st1 = int(st1) // 51 * 51 + self.list_turn_left_down[0][0]
                    st2 = int(st2) // 51 * 51 + self.list_turn_left_down[0][1]
                else:
                    c1 = self.list_turn_left_down.index((int(st1) % 51, int(st2) % 51))
                    f = True
                    for j in self.product_of_production:
                        x1, y1 = self.get_cell((int(j[0]), int(j[1])), 0)
                        if x1 == x and y1 == y:
                            if (int(j[0]) % 51, int(j[1]) % 51) in self.list_turn_left_down:
                                if self.list_turn_left_down.index((int(j[0]) % 51, int(j[1]) % 51)) - 21 == c1:
                                    f = False
                                    break
                        else:
                            if x1 == x and y1 == y + 1 and self.board[y1][x1][0] == 3:
                                if c1 > 14 and int(j[1]) == int(st2) + 24:
                                    f = False
                                    break
                                elif 12 < c1 <= 14 and int(j[1]) == int(st2) + 23:
                                    f = False
                                    break
                                elif 10 < c1 <= 12 and int(j[1]) == int(st2) + 22:
                                    f = False
                                    break
                                elif c1 == 10 and int(j[1]) == int(st2) + 21:
                                    f = False
                                    break
                            elif y1 == y + 1 and x1 == x and self.board[y1][x1][0] in [9, 10]:
                                ind = 0
                                if (int(j[0]) % 51, int(j[1]) % 51) in self.list_turn_up_right:
                                    ind = self.list_turn_up_right.index((int(j[0]) % 51, int(j[1]) % 51))
                                if (int(j[0]) % 51, int(j[1]) % 51) in self.list_turn_up_left:
                                    ind = self.list_turn_up_left.index((int(j[0]) % 51, int(j[1]) % 51))
                                if ind < 20:
                                    if c1 > 14 and int(j[1]) == int(st2) + 24:
                                        f = False
                                        break
                                    elif 12 < c1 <= 14 and int(j[1]) == int(st2) + 23:
                                        f = False
                                        break
                                    elif 10 < c1 <= 12 and int(j[1]) == int(st2) + 22:
                                        f = False
                                        break
                                    elif c1 == 10 and int(j[1]) == int(st2) + 21:
                                        f = False
                                        break
                                elif 20 <= ind < 22:
                                    if c1 > 14 and int(j[1]) == int(st2) + 23:
                                        f = False
                                        break
                                    elif 12 < c1 <= 14 and int(j[1]) == int(st2) + 22:
                                        f = False
                                        break
                                    elif 10 < c1 <= 12 and int(j[1]) == int(st2) + 21:
                                        f = False
                                        break
                                    elif c1 == 10 and int(j[1]) == int(st2) + 20:
                                        f = False
                                        break
                                elif 22 <= ind < 24:
                                    if c1 > 14 and int(j[1]) == int(st2) + 22:
                                        f = False
                                        break
                                    elif 12 < c1 <= 14 and int(j[1]) == int(st2) + 21:
                                        f = False
                                        break
                                    elif 10 < c1 <= 12 and int(j[1]) == int(st2) + 20:
                                        f = False
                                        break
                                    elif c1 == 10 and int(j[1]) == int(st2) + 19:
                                        f = False
                                        break
                                elif ind == 24:
                                    if c1 > 14 and int(j[1]) == int(st2) + 21:
                                        f = False
                                        break
                                    elif 12 < c1 <= 14 and int(j[1]) == int(st2) + 20:
                                        f = False
                                        break
                                    elif 10 < c1 <= 12 and int(j[1]) == int(st2) + 19:
                                        f = False
                                        break
                                    elif c1 == 10 and int(j[1]) == int(st2) + 18:
                                        f = False
                                        break
                    if f:
                        if int(st1 * 10) % 10 != 9:
                            st1 = (int(st1 * 10) + 1) / 10
                        else:
                            if c1 + 1 != len(self.list_turn_left_down):
                                st1 = int(st1) // 51 * 51 + self.list_turn_left_down[c1 + 1][0]
                                st2 = int(st2) // 51 * 51 + self.list_turn_left_down[c1 + 1][1]
                            else:
                                if y != 13 and self.board[y + 1][x][0] in [3, 13]:
                                    st2 = int(st2 * 10 + 1) / 10
                                elif y != 13 and self.board[y + 1][x][0] == 9:
                                    st1 = int(st1) // 51 * 51 + self.list_turn_up_right[0][0]
                                    st2 = (int(st2) // 51 + 1) * 51 + self.list_turn_up_right[0][1]
                                elif y != 13 and self.board[y + 1][x][0] == 10:
                                    st1 = int(st1) // 51 * 51 + self.list_turn_up_left[0][0]
                                    st2 = (int(st2) // 51 + 1) * 51 + self.list_turn_up_left[0][1]
                self.product_of_production[i] = (st1, st2, cell_with_meaning)

            elif self.board[y][x][0] in [3, 16]:
                st1 = self.product_of_production[i][0]
                st2 = self.product_of_production[i][1]
                cell_with_meaning = self.product_of_production[i][2]
                f = True
                for j in self.product_of_production:
                    x1, y1 = self.get_cell((int(j[0]), int(j[1])), 0)
                    if (x1 == x and y1 == y) or (y1 == y + 1 and x1 == x and self.board[y1][x1][0] == 3):
                        if int(j[0]) == int(st1) and int(j[1]) == int(st2) + 24:
                            f = False
                            break
                    else:
                        if y1 == y + 1 and x1 == x and self.board[y1][x1][0] in [9, 10]:
                            ind = 0
                            if (int(j[0]) % 51, int(j[1]) % 51) in self.list_turn_up_right:
                                ind = self.list_turn_up_right.index((int(j[0]) % 51, int(j[1]) % 51))
                            if (int(j[0]) % 51, int(j[1]) % 51) in self.list_turn_up_left:
                                ind = self.list_turn_up_left.index((int(j[0]) % 51, int(j[1]) % 51))
                            if ind < 20 and int(j[1]) == int(st2) + 24:
                                f = False
                                break
                            elif 20 <= ind < 22 and int(j[1]) == int(st2) + 23:
                                f = False
                                break
                            elif 22 <= ind < 24 and int(j[1]) == int(st2) + 22:
                                f = False
                                break
                            elif ind == 24 and int(j[1]) == int(st2) + 21:
                                f = False
                                break
                if f:
                    if int(st2 * 10 + 1) % 510 != 509: # and int(st2 * 10 - 1) % 500 != self.cell_size // 2
                        st2 = int(st2 * 10 + 1) / 10
                    elif y != 13 and self.board[y + 1][x][0] in [3, 13]:
                        st2 = int(st2 * 10 + 1) / 10
                    elif y != 13 and self.board[y + 1][x][0] == 9:
                        st1 = int(st1) // 51 * 51 + self.list_turn_up_right[0][0]
                        st2 = (int(st2) // 51 + 1) * 51 + self.list_turn_up_right[0][1]
                    elif y != 13 and self.board[y + 1][x][0] == 10:
                        st1 = int(st1) // 51 * 51 + self.list_turn_up_left[0][0]
                        st2 = (int(st2) // 51 + 1) * 51 + self.list_turn_up_left[0][1]
                self.product_of_production[i] = (st1, st2, cell_with_meaning)

            elif self.board[y][x][0] in [9]:
                st1 = self.product_of_production[i][0]
                st2 = self.product_of_production[i][1]
                cell_with_meaning = self.product_of_production[i][2]
                if (int(st1) % 51, int(st2) % 51) not in self.list_turn_up_right:
                    st1 = int(st1) // 51 * 51 + self.list_turn_up_right[0][0]
                    st2 = int(st2) // 51 * 51 + self.list_turn_up_right[0][1]
                else:
                    c1 = self.list_turn_up_right.index((int(st1) % 51, int(st2) % 51))
                    f = True
                    for j in self.product_of_production:
                        x1, y1 = self.get_cell((int(j[0]), int(j[1])), 0)
                        if x1 == x and y1 == y:
                            if (int(j[0]) % 51, int(j[1]) % 51) in self.list_turn_up_right:
                                if self.list_turn_up_right.index((int(j[0]) % 51, int(j[1]) % 51)) - 21 == c1:
                                    f = False
                                    break
                        else:
                            if x1 == x + 1 and y1 == y and self.board[y1][x1][0] == 2:
                                if c1 > 14 and int(j[0]) == int(st1) + 24:
                                    f = False
                                    break
                                elif 12 < c1 <= 14 and int(j[0]) == int(st1) + 23:
                                    f = False
                                    break
                                elif 10 < c1 <= 12 and int(j[0]) == int(st1) + 22:
                                    f = False
                                    break
                                elif c1 == 10 and int(j[0]) == int(st1) + 21:
                                    f = False
                                    break
                            elif x1 == x + 1 and y1 == y and self.board[y1][x1][0] in [8, 11]:
                                ind = 0
                                if (int(j[0]) % 51, int(j[1]) % 51) in self.list_turn_left_down:
                                    ind = self.list_turn_left_down.index((int(j[0]) % 51, int(j[1]) % 51))
                                if (int(j[0]) % 51, int(j[1]) % 51) in self.list_turn_left_up:
                                    ind = self.list_turn_left_up.index((int(j[0]) % 51, int(j[1]) % 51))
                                if ind < 20:
                                    if c1 > 14 and int(j[0]) == int(st1) + 24:
                                        f = False
                                        break
                                    elif 12 < c1 <= 14 and int(j[0]) == int(st1) + 23:
                                        f = False
                                        break
                                    elif 10 < c1 <= 12 and int(j[0]) == int(st1) + 22:
                                        f = False
                                        break
                                    elif c1 == 10 and int(j[0]) == int(st1) + 21:
                                        f = False
                                        break
                                elif 20 <= ind < 22:
                                    if c1 > 14 and int(j[0]) == int(st1) + 23:
                                        f = False
                                        break
                                    elif 12 < c1 <= 14 and int(j[0]) == int(st1) + 22:
                                        f = False
                                        break
                                    elif 10 < c1 <= 12 and int(j[0]) == int(st1) + 21:
                                        f = False
                                        break
                                    elif c1 == 10 and int(j[0]) == int(st1) + 20:
                                        f = False
                                        break
                                elif 22 <= ind < 24:
                                    if c1 > 14 and int(j[0]) == int(st1) + 22:
                                        f = False
                                        break
                                    elif 12 < c1 <= 14 and int(j[0]) == int(st1) + 21:
                                        f = False
                                        break
                                    elif 10 < c1 <= 12 and int(j[0]) == int(st1) + 20:
                                        f = False
                                        break
                                    elif c1 == 10 and int(j[0]) == int(st1) + 19:
                                        f = False
                                        break
                                elif ind == 24:
                                    if c1 > 14 and int(j[0]) == int(st1) + 21:
                                        f = False
                                        break
                                    elif 12 < c1 <= 14 and int(j[0]) == int(st1) + 20:
                                        f = False
                                        break
                                    elif 10 < c1 <= 12 and int(j[0]) == int(st1) + 19:
                                        f = False
                                        break
                                    elif c1 == 10 and int(j[0]) == int(st1) + 18:
                                        f = False
                                        break
                    if f:
                        if int(st1 * 10) % 10 != 9:
                            st1 = (int(st1 * 10) + 1) / 10
                        else:
                            if c1 + 1 != len(self.list_turn_up_right):
                                st1 = int(st1) // 51 * 51 + self.list_turn_up_right[c1 + 1][0]
                                st2 = int(st2) // 51 * 51 + self.list_turn_up_right[c1 + 1][1]
                            else:
                                if x != 13 and self.board[y][x + 1][0] in [2, 13]:
                                    st1 = (int(st1 * 10) + 1) / 10
                                elif x != 23 and self.board[y][x + 1][0] == 8:
                                    st1 = (int(st1) // 51 + 1) * 51 + self.list_turn_left_down[0][0]
                                    st2 = int(st2) // 51 * 51 + self.list_turn_left_down[0][1]
                                elif x != 23 and self.board[y][x + 1][0] == 11:
                                    st1 = (int(st1) // 51 + 1) * 51 + self.list_turn_left_up[0][0]
                                    st2 = int(st2) // 51 * 51 + self.list_turn_left_up[0][1]
                self.product_of_production[i] = (st1, st2, cell_with_meaning)

            elif self.board[y][x][0] in [10]:
                st1 = self.product_of_production[i][0]
                st2 = self.product_of_production[i][1]
                cell_with_meaning = self.product_of_production[i][2]
                if (int(st1) % 51, int(st2) % 51) not in self.list_turn_up_left:
                    st1 = int(st1) // 51 * 51 + self.list_turn_up_left[0][0] + 0.9
                    st2 = int(st2) // 51 * 51 + self.list_turn_up_left[0][1] + 0.9
                else:
                    c1 = self.list_turn_up_left.index((int(st1) % 51, int(st2) % 51))
                    f = True
                    for j in self.product_of_production:
                        x1, y1 = self.get_cell((int(j[0]), int(j[1])), 0)
                        if x1 == x and y1 == y:
                            if (int(j[0]) % 51, int(j[1]) % 51) in self.list_turn_up_left:
                                if self.list_turn_up_left.index((int(j[0]) % 51, int(j[1]) % 51)) - 21 == c1:
                                    f = False
                                    break
                        else:
                            if x1 == x - 1 and y1 == y and self.board[y1][x1][0] == 4:
                                if c1 > 14 and int(j[0]) == int(st1) - 24:
                                    f = False
                                    break
                                elif 12 < c1 <= 14 and int(j[0]) == int(st1) - 23:
                                    f = False
                                    break
                                elif 10 < c1 <= 12 and int(j[0]) == int(st1) - 22:
                                    f = False
                                    break
                                elif c1 == 10 and int(j[0]) == int(st1) - 21:
                                    f = False
                                    break
                            elif x1 == x - 1 and y1 == y and self.board[y1][x1][0] in [6, 12]:
                                ind = 0
                                if (int(j[0]) % 51, int(j[1]) % 51) in self.list_turn_right_down:
                                    ind = self.list_turn_right_down.index((int(j[0]) % 51, int(j[1]) % 51))
                                if (int(j[0]) % 51, int(j[1]) % 51) in self.list_turn_right_up:
                                    ind = self.list_turn_right_up.index((int(j[0]) % 51, int(j[1]) % 51))
                                if ind < 20:
                                    if c1 > 14 and int(j[0]) == int(st1) - 24:
                                        f = False
                                        break
                                    elif 12 < c1 <= 14 and int(j[0]) == int(st1) - 23:
                                        f = False
                                        break
                                    elif 10 < c1 <= 12 and int(j[0]) == int(st1) - 22:
                                        f = False
                                        break
                                    elif c1 == 10 and int(j[0]) == int(st1) - 21:
                                        f = False
                                        break
                                elif 20 <= ind < 22:
                                    if c1 > 14 and int(j[0]) == int(st1) - 23:
                                        f = False
                                        break
                                    elif 12 < c1 <= 14 and int(j[0]) == int(st1) - 22:
                                        f = False
                                        break
                                    elif 10 < c1 <= 12 and int(j[0]) == int(st1) - 21:
                                        f = False
                                        break
                                    elif c1 == 10 and int(j[0]) == int(st1) - 20:
                                        f = False
                                        break
                                elif 22 <= ind < 24:
                                    if c1 > 14 and int(j[0]) == int(st1) - 22:
                                        f = False
                                        break
                                    elif 12 < c1 <= 14 and int(j[0]) == int(st1) - 21:
                                        f = False
                                        break
                                    elif 10 < c1 <= 12 and int(j[0]) == int(st1) - 20:
                                        f = False
                                        break
                                    elif c1 == 10 and int(j[0]) == int(st1) - 19:
                                        f = False
                                        break
                                elif ind == 24:
                                    if c1 > 14 and int(j[0]) == int(st1) - 21:
                                        f = False
                                        break
                                    elif 12 < c1 <= 14 and int(j[0]) == int(st1) - 20:
                                        f = False
                                        break
                                    elif 10 < c1 <= 12 and int(j[0]) == int(st1) - 19:
                                        f = False
                                        break
                                    elif c1 == 10 and int(j[0]) == int(st1) - 18:
                                        f = False
                                        break
                    if f:
                        if int(st1 * 10) % 10 != 0:
                            st1 = (int(st1 * 10) - 1) / 10
                        else:
                            if c1 + 1 != len(self.list_turn_up_left):
                                st1 = int(st1) // 51 * 51 + self.list_turn_up_left[c1 + 1][0] + 0.9
                                st2 = int(st2) // 51 * 51 + self.list_turn_up_left[c1 + 1][1] + 0.9
                            else:
                                if x != 0 and self.board[y][x - 1][0] in [4, 13]:
                                    st1 = (int(st1 * 10) - 1) / 10
                                elif x != 0 and self.board[y][x - 1][0] == 6:
                                    st1 = (int(st1) // 51 - 1) * 51 + self.list_turn_right_down[0][0]
                                    st2 = int(st2) // 51 * 51 + self.list_turn_right_down[0][1]
                                elif x != 0 and self.board[y][x - 1][0] == 12:
                                    st1 = (int(st1) // 51 - 1) * 51 + self.list_turn_right_up[0][0]
                                    st2 = int(st2) // 51 * 51 + self.list_turn_right_up[0][1]
                self.product_of_production[i] = (st1, st2, cell_with_meaning)

            elif self.board[y][x][0] in [4, 17]:
                st1 = self.product_of_production[i][0]
                st2 = self.product_of_production[i][1]
                cell_with_meaning = self.product_of_production[i][2]
                f = True
                for j in self.product_of_production:
                    x1, y1 = self.get_cell((int(j[0]), int(j[1])), 0)
                    if (x1 == x and y1 == y) or (y1 == y and x1 == x - 1 and self.board[y1][x1][0] == 4):
                        if int(j[0]) == int(st1) - 24 and int(j[1]) == int(st2):
                            f = False
                            break
                    else:
                        if x1 == x - 1 and y1 == y and self.board[y1][x1][0] in [6, 12]:
                            ind = 0
                            if (int(j[0]) % 51, int(j[1]) % 51) in self.list_turn_right_down:
                                ind = self.list_turn_right_down.index((int(j[0]) % 51, int(j[1]) % 51))
                            if (int(j[0]) % 51, int(j[1]) % 51) in self.list_turn_right_up:
                                ind = self.list_turn_right_up.index((int(j[0]) % 51, int(j[1]) % 51))
                            if ind < 20 and int(j[0]) == int(st1) - 24:
                                f = False
                                break
                            elif 20 <= ind < 22 and int(j[0]) == int(st1) - 23:
                                f = False
                                break
                            elif 22 <= ind < 24 and int(j[0]) == int(st1) - 22:
                                f = False
                                break
                            elif ind == 24 and int(j[0]) == int(st1) - 21:
                                f = False
                                break
                if f:
                    if int(st1 * 10 - 1) % 510 != 1:
                        st1 = int(st1 * 10 - 1) / 10
                    elif x != 0 and self.board[y][x - 1][0] in [4, 13]:  # int(st2 * 10 - 1) % 500 != self.cell_size // 2
                        st1 = int(st1 * 10 - 1) / 10
                    elif x != 0 and self.board[y][x - 1][0] == 6: # and (st2 * 10 - 1) % 500 != self.cell_size // 2
                        st1 = (int(st1) // 51 - 1) * 51 + self.list_turn_right_down[0][0]
                        st2 = int(st2) // 51 * 51 + self.list_turn_right_down[0][1]
                    elif x != 0 and self.board[y][x - 1][0] == 12:
                        st1 = (int(st1) // 51 - 1) * 51 + self.list_turn_right_up[0][0]
                        st2 = int(st2) // 51 * 51 + self.list_turn_right_up[0][1]
                self.product_of_production[i] = (st1, st2, cell_with_meaning)

            elif self.board[y][x][0] in [12]:
                st1 = self.product_of_production[i][0]
                st2 = self.product_of_production[i][1]
                cell_with_meaning = self.product_of_production[i][2]
                if (int(st1) % 51, int(st2) % 51) not in self.list_turn_right_up:
                    st1 = int(st1) // 51 * 51 + self.list_turn_right_up[0][0] + 0.9
                    st2 = int(st2) // 51 * 51 + self.list_turn_right_up[0][1] + 0.9
                else:
                    c1 = self.list_turn_right_up.index((int(st1) % 51, int(st2) % 51))
                    f = True
                    for j in self.product_of_production:
                        x1, y1 = self.get_cell((int(j[0]), int(j[1])), 0)
                        if x1 == x and y1 == y:
                            if (int(j[0]) % 51, int(j[1]) % 51) in self.list_turn_right_up:
                                if self.list_turn_right_up.index((int(j[0]) % 51, int(j[1]) % 51)) - 21 == c1:
                                    f = False
                                    break
                        else:
                            if x1 == x and y1 == y - 1 and self.board[y1][x1][0] == 1:
                                if c1 > 14 and int(j[1]) == int(st2) - 24:
                                    f = False
                                    break
                                elif 12 < c1 <= 14 and int(j[1]) == int(st2) - 23:
                                    f = False
                                    break
                                elif 10 < c1 <= 12 and int(j[1]) == int(st2) - 22:
                                    f = False
                                    break
                                elif c1 == 10 and int(j[1]) == int(st2) - 21:
                                    f = False
                                    break
                            elif y1 == y - 1 and x1 == x and self.board[y1][x1][0] in [7, 5]:
                                ind = 0
                                if (int(j[0]) % 51, int(j[1]) % 51) in self.list_turn_down_right:
                                    ind = self.list_turn_down_right.index((int(j[0]) % 51, int(j[1]) % 51))
                                if (int(j[0]) % 51, int(j[1]) % 51) in self.list_turn_down_left:
                                    ind = self.list_turn_down_left.index((int(j[0]) % 51, int(j[1]) % 51))
                                if ind < 20:
                                    if c1 > 14 and int(j[1]) == int(st2) - 24:
                                        f = False
                                        break
                                    elif 12 < c1 <= 14 and int(j[1]) == int(st2) - 23:
                                        f = False
                                        break
                                    elif 10 < c1 <= 12 and int(j[1]) == int(st2) - 22:
                                        f = False
                                        break
                                    elif c1 == 10 and int(j[1]) == int(st2) - 21:
                                        f = False
                                        break
                                elif 20 <= ind < 22:
                                    if c1 > 14 and int(j[1]) == int(st2) - 23:
                                        f = False
                                        break
                                    elif 12 < c1 <= 14 and int(j[1]) == int(st2) - 22:
                                        f = False
                                        break
                                    elif 10 < c1 <= 12 and int(j[1]) == int(st2) - 21:
                                        f = False
                                        break
                                    elif c1 == 10 and int(j[1]) == int(st2) - 20:
                                        f = False
                                        break
                                elif 22 <= ind < 24:
                                    if c1 > 14 and int(j[1]) == int(st2) - 22:
                                        f = False
                                        break
                                    elif 12 < c1 <= 14 and int(j[1]) == int(st2) - 21:
                                        f = False
                                        break
                                    elif 10 < c1 <= 12 and int(j[1]) == int(st2) - 20:
                                        f = False
                                        break
                                    elif c1 == 10 and int(j[1]) == int(st2) - 19:
                                        f = False
                                        break
                                elif ind == 24:
                                    if c1 > 14 and int(j[1]) == int(st2) - 21:
                                        f = False
                                        break
                                    elif 12 < c1 <= 14 and int(j[1]) == int(st2) - 20:
                                        f = False
                                        break
                                    elif 10 < c1 <= 12 and int(j[1]) == int(st2) - 19:
                                        f = False
                                        break
                                    elif c1 == 10 and int(j[1]) == int(st2) - 18:
                                        f = False
                                        break
                    if f:
                        if int(st2 * 10) % 10 != 0:
                            st2 = (int(st2 * 10) - 1) / 10
                        else:
                            if c1 + 1 != len(self.list_turn_right_up):
                                st1 = int(st1) // 51 * 51 + self.list_turn_right_up[c1 + 1][0] + 0.9
                                st2 = int(st2) // 51 * 51 + self.list_turn_right_up[c1 + 1][1] + 0.9
                            else:
                                if y != 0 and self.board[y - 1][x][0] in [1, 13]:
                                    st2 = (int(st2 * 10) - 1) / 10
                                elif y != 0 and self.board[y - 1][x][0] == 7:
                                    st1 = int(st1) // 51 * 51 + self.list_turn_down_right[0][0]
                                    st2 = (int(st2) // 51 - 1) * 51 + self.list_turn_down_right[0][1]
                                elif y != 0 and self.board[y - 1][x][0] == 5:
                                    st1 = int(st1) // 51 * 51 + self.list_turn_down_left[0][0]
                                    st2 = (int(st2) // 51 - 1) * 51 + self.list_turn_down_left[0][1]
                self.product_of_production[i] = (st1, st2, cell_with_meaning)

            elif self.board[y][x][0] in [6]:
                st1 = self.product_of_production[i][0]
                st2 = self.product_of_production[i][1]
                cell_with_meaning = self.product_of_production[i][2]
                if (int(st1) % 51, int(st2) % 51) not in self.list_turn_right_down:
                    st1 = int(st1) // 51 * 51 + self.list_turn_right_down[0][0]
                    st2 = int(st2) // 51 * 51 + self.list_turn_right_down[0][1]
                else:
                    c1 = self.list_turn_right_down.index((int(st1) % 51, int(st2) % 51))
                    f = True
                    for j in self.product_of_production:
                        x1, y1 = self.get_cell((int(j[0]), int(j[1])), 0)
                        if x1 == x and y1 == y:
                            if (int(j[0]) % 51, int(j[1]) % 51) in self.list_turn_right_down:
                                if self.list_turn_right_down.index((int(j[0]) % 51, int(j[1]) % 51)) - 21 == c1:
                                    f = False
                                    break
                        else:
                            if x1 == x and y1 == y + 1 and self.board[y1][x1][0] == 3:
                                if c1 > 14 and int(j[1]) == int(st2) + 24:
                                    f = False
                                    break
                                elif 12 < c1 <= 14 and int(j[1]) == int(st2) + 23:
                                    f = False
                                    break
                                elif 10 < c1 <= 12 and int(j[1]) == int(st2) + 22:
                                    f = False
                                    break
                                elif c1 == 10 and int(j[1]) == int(st2) + 21:
                                    f = False
                                    break
                            elif y1 == y + 1 and x1 == x and self.board[y1][x1][0] in [9, 10]:
                                ind = 0
                                if (int(j[0]) % 51, int(j[1]) % 51) in self.list_turn_up_right:
                                    ind = self.list_turn_up_right.index((int(j[0]) % 51, int(j[1]) % 51))
                                if (int(j[0]) % 51, int(j[1]) % 51) in self.list_turn_up_left:
                                    ind = self.list_turn_up_left.index((int(j[0]) % 51, int(j[1]) % 51))
                                if ind < 20:
                                    if c1 > 14 and int(j[1]) == int(st2) + 24:
                                        f = False
                                        break
                                    elif 12 < c1 <= 14 and int(j[1]) == int(st2) + 23:
                                        f = False
                                        break
                                    elif 10 < c1 <= 12 and int(j[1]) == int(st2) + 22:
                                        f = False
                                        break
                                    elif c1 == 10 and int(j[1]) == int(st2) + 21:
                                        f = False
                                        break
                                elif 20 <= ind < 22:
                                    if c1 > 14 and int(j[1]) == int(st2) + 23:
                                        f = False
                                        break
                                    elif 12 < c1 <= 14 and int(j[1]) == int(st2) + 22:
                                        f = False
                                        break
                                    elif 10 < c1 <= 12 and int(j[1]) == int(st2) + 21:
                                        f = False
                                        break
                                    elif c1 == 10 and int(j[1]) == int(st2) + 20:
                                        f = False
                                        break
                                elif 22 <= ind < 24:
                                    if c1 > 14 and int(j[1]) == int(st2) + 22:
                                        f = False
                                        break
                                    elif 12 < c1 <= 14 and int(j[1]) == int(st2) + 21:
                                        f = False
                                        break
                                    elif 10 < c1 <= 12 and int(j[1]) == int(st2) + 20:
                                        f = False
                                        break
                                    elif c1 == 10 and int(j[1]) == int(st2) + 19:
                                        f = False
                                        break
                                elif ind == 24:
                                    if c1 > 14 and int(j[1]) == int(st2) + 21:
                                        f = False
                                        break
                                    elif 12 < c1 <= 14 and int(j[1]) == int(st2) + 20:
                                        f = False
                                        break
                                    elif 10 < c1 <= 12 and int(j[1]) == int(st2) + 19:
                                        f = False
                                        break
                                    elif c1 == 10 and int(j[1]) == int(st2) + 18:
                                        f = False
                                        break
                    if f:
                        if int(st1 * 10) % 10 != 9:
                            st1 = (int(st1 * 10) + 1) / 10
                        else:
                            if c1 + 1 != len(self.list_turn_right_down):
                                st1 = int(st1) // 51 * 51 + self.list_turn_right_down[c1 + 1][0]
                                st2 = int(st2) // 51 * 51 + self.list_turn_right_down[c1 + 1][1]
                            else:
                                if y != 13 and self.board[y + 1][x][0] in [3, 13]:
                                    st2 = int(st2 * 10 + 1) / 10
                                elif y != 13 and self.board[y + 1][x][0] == 9:
                                    st1 = int(st1) // 51 * 51 + self.list_turn_up_right[0][0]
                                    st2 = (int(st2) // 51 + 1) * 51 + self.list_turn_up_right[0][1]
                                elif y != 13 and self.board[y + 1][x][0] == 10:
                                    st1 = int(st1) // 51 * 51 + self.list_turn_up_left[0][0]
                                    st2 = (int(st2) // 51 + 1) * 51 + self.list_turn_up_left[0][1]
                self.product_of_production[i] = (st1, st2, cell_with_meaning)

            elif self.board[y][x][0] in [13]:
                st1 = self.product_of_production[i][0]
                st2 = self.product_of_production[i][1]
                cell_with_meaning = self.product_of_production[i][2]
                if y in [5] and x in [11, 12]:
                    st2 = (int(st2 * 10) + 1) / 10
                elif y in [8] and x in [11, 12]:
                    st2 = (int(st2 * 10) - 1) / 10
                elif y in [6, 7] and x in [10]:
                    st1 = (int(st1 * 10) + 1) / 10
                elif y in [6, 7] and x in [13]:
                    st1 = (int(st1 * 10) - 1) / 10
                else:
                    if y in [5, 8] and x in [10, 13]:
                        if 689 < st1:
                            st1 = (int(st1 * 10) - 1) / 10
                        elif 434 < st2:
                            st2 = (int(st2 * 10) - 1) / 10
                        elif 535 > st1:
                            st1 = (int(st1 * 10) + 1) / 10
                        elif 280 > st2:
                            st2 = (int(st2 * 10) + 1) / 10
                if 533 < st1 < 690 and 279 < st2 < 435:
                    self.hub.delivery_calculation()
                    del_list.append(i)
                self.product_of_production[i] = (st1, st2, cell_with_meaning)
            if self.board[y][x][0] in [0, 18] or not self.board[y][x][1]:
                del_list.append(i)
            if 13 < self.board[y][x][0] < 18:
                self.board[y][x][2] = 0
            st1 = int(self.product_of_production[i][0])
            st2 = int(self.product_of_production[i][1])
            cell_with_meaning = self.product_of_production[i][2]
            if cell_with_meaning == 'круг':
                pygame.draw.circle(screen, (221, 255, 255), [st1, st2], 12)
        for i in list(reversed(del_list)):
            del self.product_of_production[i]
        #print(len(self.product_of_production))
        for i in drills:
            self.objects.draw_drill(i[1] * self.cell_size, i[0] * self.cell_size, self.board[i[0]][i[1]][0] % 14, pos, r)

    def delete(self, mouse_pos):
        cell = self.get_cell(mouse_pos, 3)
        if not cell is None and self.board[cell[1]][cell[0]][:2] != [0, True]:
           self.board[cell[1]][cell[0]][:2] = [0, True]

    def interface(self):
        if self.interface_menu:
            self.objects.menu_icon_for_objects_active()
        else:
            self.objects.menu_icon_for_objects_not_active()


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Shapez')
    board = Board(24, 14)
    size = width, height = 1224, 714
    screen = pygame.display.set_mode(size)
    screen2 = pygame.Surface(screen.get_size())
    running = True
    fps = 1000
    c = 0
    r = 0
    draw_conveyors = False
    draw_drill = False
    drawing2 = False
    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                board.get_click(event.pos, 1)
                if board.board_menu_buttons[0]:
                    draw_conveyors = True
                if  board.board_menu_buttons[1]:
                    draw_drill = True
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                board.get_work_conveyor()
                draw_conveyors = False
                draw_drill = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                board.get_click(event.pos, 3)
                drawing2 = True
            if event.type == pygame.MOUSEBUTTONUP and event.button == 3:
                drawing2 = False
            if event.type == pygame.MOUSEMOTION:
                if draw_conveyors:
                    board.comparison_original_point(event.pos)
                elif draw_drill:
                    board.draw_drill(event.pos)
                elif drawing2:
                    board.delete(event.pos)
        c += 1
        if c == 170:
            c %= 170
            r += 1
            r %= 2
        board.render(int(c) // 10, r)
        board.interface()
        clock.tick(fps)
        pygame.display.flip()