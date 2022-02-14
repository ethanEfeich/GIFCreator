import window
from PIL import ImageGrab
from pynput.mouse import Listener, Button, Controller


if __name__ == '__main__':
    window.create_window()

# including these methods here for now
# should probably move to another py file later :/
def get_screen_shot(x, y, x2, y2):
    bbox = (x, y, x2, y2)
    im = ImageGrab.grab(bbox)
    im.save('test.png')
    im.close()


def is_clicked(x, y, button, pressed):
    mouse = Controller()
    current_mouse_position = mouse.position
    int_pos = list(current_mouse_position)
    int_ext_pos = [int_pos[0] + 112, int_pos[1] + 112]
    if pressed:
        print(int_pos)
        print(int_ext_pos)
        get_screen_shot(int_pos[0], int_pos[1], int_ext_pos[0], int_ext_pos[1])
        return False # to stop the thread after click#


with Listener(on_click=is_clicked) as listener:
    listener.join()