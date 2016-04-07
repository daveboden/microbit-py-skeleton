def get_pixel(x, y):
    """gets the brightness of the pixel (x,y). Brightness can be from 0 (the pixel
    is off) to 9 (the pixel is at maximum brightness).
    """
    pass


def set_pixel(x, y, val):
    """sets the brightness of the pixel (x,y) to val (between 0 [off] and 9 [max
    brightness], inclusive).
    """
    pass


def clear():
    """clears the display."""
    pass


def show(image, delay=0, wait=True, loop=False, clear=False):
    """shows the image."""
    pass


def show(iterable, delay=400, wait=True, loop=False, clear=False):
    """shows each image or letter in the iterable, with delay ms. in between each."""
    pass


def scroll(string, delay=400):
    """scrolls a string across the display (more exciting than display.show for
    written messages).
    """
    pass
