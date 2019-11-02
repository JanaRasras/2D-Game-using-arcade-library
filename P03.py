'''
Build Your Own 2D Platformer Game using Arcade Library
P03: Add keyboard control
Jana Rasras
Nov.2019
'''

## libraries
import arcade


## constants
WIDTH = 1000
HEIGHT = 650
TITLE = 'A game'
BLUE =[100,149,237]

CHARACTER_SCALING = 1
TILE_SCALING = 0.5
COIN_SCALING = 0.5

PLAYER_MOVEMENT_SPEED = 5


## classes
class JGame(arcade.Window):
    def __init__(self):
        super().__init__(WIDTH, HEIGHT, TITLE)
        arcade.set_background_color(BLUE)
        
        # Our physics engine
        self.physics_engine = None
         
    def setup(self):
        #  for scrolling
        self.view_bottom = 0
        self.view_left = 0

        # Keep track of the score
        self.score = 0

        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()

        self.player_sprite = arcade.Sprite('images/player_1/player_stand.png',CHARACTER_SCALING)
        self.player_sprite.center_x = 64
        self.player_sprite.center_y = 120
        # self.player_sprite.position = [64, 120]
        self.player_list.append(self.player_sprite)

        for x in range(0,1250,64):
            wall = arcade.Sprite('images/tiles/grassMid.png',TILE_SCALING)
            wall.center_x = x
            wall.center_y = 32
            self.wall_list.append(wall)

        coordinate_list = [[512, 96],
                        [256, 96],
                        [768, 96]]

        for coordinate in coordinate_list:
                wall = arcade.Sprite('images/tiles/boxCrate_double.png', TILE_SCALING)
                wall.position = coordinate
                self.wall_list.append(wall)

        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player_sprite, self.wall_list, GRAVITY)

    def on_draw(self):
        ''' Render the screen'''
        arcade.start_render()

        self.wall_list.draw()
        self.coin_list.draw()
        self.player_list.draw()

        # Draw  score and scroll it
        score_text = f"Score: {self.score}"
        arcade.draw_text(score_text, 10 + self.view_left, 10 + self.view_bottom, [255, 255, 255], 18)
        
    def on_key_press(self, key, modifiers):
        ''' 
        '''
        if key == arcade.key.UP:
            if self.physics_engine.can_jump():
                self.player_sprite.change_y = PLAYER_JUMP_SPEED
                arcade.play_sound(self.jump_sound)
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = - PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = - PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED       
        
    def on_key_release(self, key, modifiers):
        ''' '''
        if key == arcade.key.LEFT:
            self.player_sprite.change_x = 0
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0

    def on_update(self, delta_time):
        """ Movement and game logic (Call update on all sprites)"""
        self.physics_engine.update()

    

## functions
def main():
    '''
    Create an Empty game
    '''
    window = JGame()
    window.setup()
    arcade.run()


## The End ..
if __name__ =='__main__':
    main()    