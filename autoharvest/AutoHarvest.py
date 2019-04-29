from enum import Enum
import threading

import pyautogui
import time

class Direction(Enum):
    FORWARD = 'w'
    BACKWARD = 's'
    RIGHT = 'd'
    LEFT = 'a'


class AutoHarvest(object):
    def __init__(self, blocks_forward=10, blocks_side=20):
        self.blocks_forward = blocks_forward
        self.blocks_side = blocks_side
        self.sec_per_block = .415

    def move(self, direction: Direction):
        pyautogui.keyDown(direction.value)
        if direction is Direction.FORWARD or direction is Direction.BACKWARD:
            time.sleep(self.sec_per_block * self.blocks_forward)
        else:
            time.sleep(.35)
        pyautogui.keyUp(direction.value)
        
    def move_forward(self):
        self.move(Direction.FORWARD)
        
    def move_backward(self):
        self.move(Direction.BACKWARD)
        
    def move_left(self):
        self.move(Direction.LEFT)
        
    def move_right(self):
        self.move(Direction.RIGHT)
        
    def click(self, button='left'):
        pyautogui.mouseDown(button=button)
        time.sleep(self.sec_per_block * self.blocks_forward)
        pyautogui.mouseUp(button=button)
        
    def back_to_start(self):
        pyautogui.keyDown('d')
        time.sleep(0.5 * self.blocks_side)
        pyautogui.keyUp('d')
        pyautogui.keyDown('s')
        time.sleep(0.5)
        pyautogui.keyUp('s')
        
    def harvest_forward(self):
        # Change to pickaxe with fortune
        pyautogui.press('1')
        
        forward = threading.Thread(target=self.move_forward)
        click = threading.Thread(target=self.click, args=('left', ))
        
        forward.start()
        click.start()
        forward.join()
        click.join()
        
    def replant(self):
        pyautogui.press('2')
        
        backward = threading.Thread(target=self.move_backward)
        click = threading.Thread(target=self.click, args=('right', ))
        
        backward.start()
        click.start()
         
        backward.join()
        click.join()
        
    def close_inventory(self ):
        pyautogui.press('e')
        
    def start(self):
        # x = threading.Thread(target=self.move_forward, args=())
        # y = threading.Thread(target=self.move_forward, args=())
        for i in range(self.blocks_side):
            self.harvest_forward()
            self.replant()
            if i == self.blocks_side - 1:
                self.back_to_start()
            else:
                self.move_left()
    