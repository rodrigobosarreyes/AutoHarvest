import time

from autoharvest import AutoHarvest
# from autoharvest import screen_utils


# screen_utils.MINECRAFT_VERSION = '1.12.2'
# screen_utils.show_window_background()
# screen_utils.check_window_size()

bot = AutoHarvest.AutoHarvest(blocks_forward=14)
time.sleep(5)
try:
    while True:
        # screen_utils.show_window_background()
        # bot.close_inventory()
        bot.start()
        time.sleep(60 * 3)
except KeyboardInterrupt as e:
    pass