import win32gui
import win32con


MINECRAFT_CLASS_NAME = 'LWJGL'
MINECRAFT_VERSION = '1.12.2'
MINECRAFT_TITLE = 'Minecraft '

def check_window_size():
    """ Checks if window's size is appropriate, if not resize"""
    
    wight = 870
    height = 519
    
    window = win32gui.FindWindow(MINECRAFT_CLASS_NAME, MINECRAFT_TITLE + MINECRAFT_VERSION)
    x0, y0, x1, y1 = win32gui.GetWindowRect(window)
    # x0 and y0 are initial points, upper left corner and lower left corner
    # then we need the difference between upper left corner and upper right corner to get the wight and
    # the difference between lower left corner and lower right corner to get the height
    
    w = x1 - x0
    h = y1 - y0
    
    if w is not wight or h is not height:
        win32gui.MoveWindow(window, x0, y0, wight, height, True)
   
        
def maximize_window():
    """ Maximize the window """
    
    window = win32gui.FindWindow(MINECRAFT_CLASS_NAME, MINECRAFT_TITLE + MINECRAFT_VERSION)
    
    win32gui.ShowWindow(window, win32con.SW_MAXIMIZE)
    
    
def minimize_window():
    """ Minimize the window """
    
    window = win32gui.FindWindow(MINECRAFT_CLASS_NAME, MINECRAFT_TITLE + MINECRAFT_VERSION)
    
    win32gui.ShowWindow(window, win32con.SW_MINIMIZE)
   
    
def show_window_background():
    """ Show the window in background, not minimized """
    
    window = win32gui.FindWindow(MINECRAFT_CLASS_NAME, MINECRAFT_TITLE + MINECRAFT_VERSION)
    win32gui.SetForegroundWindow(window)
    win32gui.BringWindowToTop(window)
    

def restore_window():
    window = win32gui.FindWindow(MINECRAFT_CLASS_NAME, MINECRAFT_TITLE + MINECRAFT_VERSION)
    
    win32gui.ShowWindow(window, win32con.SW_RESTORE)