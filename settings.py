class Settings():

    def __init__(self):
        # screen settings
        self.screen_width = 400
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # ship
        self.ship_speed_factor = 1

        # bullet
        self.bullet_speed_factor = 1.2
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3


        # alien
        self.alien_speed_factor = 0.2
        self.fleet_drop_speed = 5
        self.fleet_direction = 1
