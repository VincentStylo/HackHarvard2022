class Settings:

    def __init__(self):

        # Screen settings
        self.screen_width = 800
        self.screen_height = 600

        # Bullet settings
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = (225, 215, 0)
        self.bullets_allowed = 4

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.bullet_speed = 8.0

    def increase_speed(self):
        self.player_speed = 1.5
        self.bullet_speed *= self.speedup_scale
