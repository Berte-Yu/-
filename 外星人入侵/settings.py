class Settings(object):
    """存储<外星人入侵的所有设置的类>"""
    def __init__(self):
        # 初始化屏幕的设置
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230,230,230)

        # 飞船的设置
        self.ship_speed_factor = 1.5


