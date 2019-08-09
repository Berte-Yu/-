import pygame
import time
from settings import Settings
from ship import Ship
import game_functions as gf
from alien import Alien

def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()

    ai_settings = Settings()

    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 创建一个飞船
    ship = Ship(ai_settings, screen)
    
    # 创建一个外星人
    alien = Alien(ai_settings, screen)

    while True:
        # 监视键盘和鼠标事件
        gf.check_events(ship)

        # 更新飞船的位置
        ship.update()

        # 屏幕刷新
        gf.update_screen(ai_settings, screen, ship, alien)

        # 延时10ms
        time.sleep(0.005)


if __name__ == "__main__":
    run_game()
