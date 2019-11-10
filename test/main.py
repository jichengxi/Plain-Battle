import pygame
from sprites import *

# 初始化pygame
pygame.init()

# 创建游戏主窗口480*700
screen = pygame.display.set_mode((480, 700))

# 绘制背景图像
# 1. 加载图像
bg = pygame.image.load("./images/background.png")
hero = pygame.image.load("./images/me1.png")
# 2. blit绘制图像
screen.blit(bg, (0, 0))
screen.blit(hero, (150, 500))
# 3. update更新屏幕显示
pygame.display.update()

# 1) 定义rect记录飞机的初始位置
hero_rect = pygame.Rect(150, 500, 102, 126)
# 创建时钟对象
clock = pygame.time.Clock()

# 创建敌机的精灵
enemy = GameSprite("./images/enemy1.png")

# 创建敌机的精灵组
enemy_group = pygame.sprite.Group(enemy)

# 游戏循环 -> 游戏正式开始
while True:
    # 指定循环体内部代码执行的频率
    clock.tick(60)

    # 监听事件
    for event in pygame.event.get():
        # 判断事件类型是不是退出事件
        if event.type == pygame.QUIT:
            print("游戏退出...")
            # quit 卸载所有模块
            pygame.quit()
            # exit()
            exit()

    # 2) 修改飞机的位置
    hero_rect.y -= 1
    # 判断飞机的位置
    if hero_rect.y + 126 <= 0:
        hero_rect.y = 700

    # 3) 调用blit方法绘制图像
    screen.blit(bg, (0, 0))
    screen.blit(hero, hero_rect)

    # 让精灵组调用两个方法
    # update
    enemy_group.update()
    # draw
    enemy_group.draw(screen)

    # 4) 更新屏幕显示
    pygame.display.update()
    pass

# 退出pygame
pygame.quit()
