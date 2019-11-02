'''
Build Your Own 2D Platformer Game using Arcade Library
Jana Rasras
P02: Add Sprites
Nov.2019
'''

# libraries
import arcade

# constants
WIDTH = 1000
HEIGHT = 650
TITLE = 'A game'
BLUE =[100,149,237]

# sprites size
CHARACTER_SCALING = 1
TILE_SCALING = 0.5
COIN_SCALING = 0.5


# classes
class JGame(arcade.Window):
    def __init__(self):
        ''' variables '''
        # window
        super().__init__(WIDTH,HEIGHT,TITLE)
        arcade.set_background_color(BLUE)

        # lists
        self.coin_list = None
        self.wall_list = None
        self.player_list = None

        # player
        self.player_sprite = None

    def setup(self):
        ''' reset game '''
        # empty lists
        self.player_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.wall_list()

        # add sprites
        # 1. player
        self.player_sprite = arcade.Sprite('',CHARACTER_SCALING)
        self.player_sprite.center_x = 0
        self.player_sprite.center_y = 0
        self.player_list.append(self.player_sprite)
    
        # 2. walls
        # TODO

        # 3. coins
        # TODO 

    def on_draw(self):
        arcade.start_render()
        # Draw our sprites
        self.wall_list.draw()
        self.coin_list.draw()
        self.player_list.draw()


def main ():
    ''' '''
    window = JGame()
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()