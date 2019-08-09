import pygame

class Ship(object):
    """船的类"""
    def __init__(self, ai_settings, screen):
        # 初始化飞船并设置其初始位置
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载飞船图像并获取其外形矩形
        self.image = pygame.image.load('images/ship.bmp')
        print(self.image)
        # 表示飞船的矩形
        self.rect = self.image.get_rect()
        # 表示屏幕的矩形
        self.screen_rect = screen.get_rect()

        # 将屏幕矩形的中央坐标属性给到飞船的矩形对象上
        self.rect.centerx = self.screen_rect.centerx
        # 将屏幕矩形的底部坐标属性给到飞船的矩形对象上
        self.rect.bottom = self.screen_rect.bottom

        #在飞船属性center中存储小数值
        self.center = float(self.rect.centerx)

        # 移动标志
        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
            
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        
        # 根据self.center更新飞船的矩形中心坐标
        self.rect.centerx = self.center

    def blitme(self):
        # 将飞船图形绘制到屏幕上
        self.screen.blit(self.image, self.rect)



