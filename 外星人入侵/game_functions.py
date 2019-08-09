import sys
import pygame

def check_keydown_events(event, ship):
    '''响应按键'''
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_q:
        pygame.quit()
        sys.exit(0)

def check_keyup_events(event, ship):
    '''响应按键松开'''
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ship):
    # 响应鼠标和按键事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # 触发退出事件
            pygame.quit()
            sys.exit(0)
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def update_screen(ai_settings, screen, ship, alien):
    # 更新屏幕上的图像，并切换到新屏幕
    # 设置背景色
    screen.fill(ai_settings.bg_color)
    
    # 重绘飞船
    ship.blitme()

    #重绘外星人
    alien.blitme()

    # 刷新整体背景
    pygame.display.flip()