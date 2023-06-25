import pygame
import time
import random

# 初始化 Pygame
pygame.init()

# 设置游戏窗口尺寸
window_width = 400
window_height = 400

# 设置蛇的大小
block_size = 20

# 创建游戏窗口
window = pygame.display.set_mode((window_width, window_height))

# 设置游戏标题
pygame.display.set_caption("贪吃蛇")

# 设置颜色
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# 设置字体
font_style = pygame.font.SysFont(None, 30)


# 定义函数，用于在游戏窗口中绘制蛇和食物
def draw_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(window, black, [x[0], x[1], snake_block, snake_block])


def message(msg, color):
    message = font_style.render(msg, True, color)
    window.blit(message, [window_width / 6, window_height / 3])


# 设置游戏主循环
def game_loop():
    game_over = False
    game_close = False

    # 初始蛇的位置和长度
    x1 = window_width / 2
    y1 = window_height / 2
    x1_change = 0
    y1_change = 0

    # 初始食物的位置
    foodx = round(random.randrange(0, window_width - block_size) / 20.0) * 20.0
    foody = round(random.randrange(0, window_height - block_size) / 20.0) * 20.0

    # 初始蛇的长度为 1
    snake_List = []
    Length_of_snake = 1

    # 游戏循环
    while not game_over:

        while game_close == True:
            window.fill(white)
            message("你输了，按 Q 退出，按 C 重新开始", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        # 处理键盘事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -block_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = block_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -block_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = block_size
                    x1_change = 0

        # 判断蛇是否超出边界
        if x1 >= window_width or x1 < 0 or y1 >= window_height or y1 < 0:
            game_close = True

        # 更新蛇的位置
        x1 += x1_change
        y1 += y1_change

        # 清除窗口
        window.fill(white)

        # 绘制食物
        pygame.draw.rect(window, red, [foodx, foody, block_size, block_size])

        # 将蛇的头添加到蛇的列表中
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)

        # 如果蛇的长度超过了 Length_of_snake，删除蛇尾
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        # 判断蛇是否吃到了食物
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        # 绘制蛇
        draw_snake(block_size, snake_List)
        pygame.display.update()

        # 如果蛇吃到了食物，更新食物的位置，增加蛇的长度
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, window_width - block_size) / 20.0) * 20.0
            foody = round(random.randrange(0, window_height - block_size) / 20.0) * 20.0
            Length_of_snake += 1

        # 设置游戏速度
        clock = pygame.time.Clock()
        clock.tick(10)

    # 退出 Pygame
    pygame.quit()

    # 退出 Python
    quit()


# 开始游戏
game_loop()
