'''
Build Your Own 2D Platformer Game using Arcade Library
Part 1 : Install and Open a Window
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


## classes
class JGame(arcade.Window):
    def __init__(self):
        super().__init__(WIDTH, HEIGHT, TITLE)
        arcade.set_background_color(BLUE)
        
    def setup(self):
       pass

    def on_draw(self):
        ''' Render the screen'''
        arcade.start_render()

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