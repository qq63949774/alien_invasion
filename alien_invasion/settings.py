class Settings:
    """存储游戏《外星人入侵》中所有设置的类
       用于初始化控制游戏外观和飞船速度的属性。
    """

    def __init__(self):
        """初始化游戏设置"""
        # 屏幕设置
        self.bg_color = (230, 230, 230)
        self.ship_limit = 1
        # 子弹设置。
        self.bullet_speed = 3.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 5
        # 外星人设置
        self.fleet_drop_speed = 10
        # 加快游戏节奏。
        self.speedup_scale = 1.1
        self.initialize_dynamic_settings()
        # 外星人分数的提高速度。
        self.score_scale = 1.5

    def initialize_dynamic_settings(self):
        """初始化随游戏进行而变化的设置。 """
        self.ship_speed = 3.0
        self.bullet_speed = 0.5
        self.alien_speed = 0.2
        # fleet_direction为1表示向右，为-1表示向左。
        self.fleet_direction = 1
        self.alien_points = 50

    def increase_speed(self):
        """提高速度设置。"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)