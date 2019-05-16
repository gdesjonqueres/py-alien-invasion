class GameStats():
    """Track statics for Alien Invsation"""

    def __init__(self, ai_settings):
        """Initialize statics"""
        self.ai_settings = ai_settings
        self.reset_stats()
        # Start alien Invasion in an inactive state
        self.game_active = False

    def reset_stats(self):
        """Init stats that can change during the game"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
