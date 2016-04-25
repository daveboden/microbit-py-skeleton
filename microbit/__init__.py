__all__ = [
    "sleep", "running_time", "panic", "reset", "temperature",
    "pin0", "pin1", "pin2", "pin3", "pin4", "pin5", "pin6",
    "pin7", "pin8", "pin9", "pin10", "pin11", "pin12", "pin13",
    "pin14", "pin15", "pin16", "pin19", "pin20",
    "display", "button_a", "button_b", "Image", "accelerometer"
]


def sleep(ms):
    """sleep for the given number of milliseconds.
    """
    pass


def running_time():
    """returns the number of milliseconds since the micro:bit was last switched on."""
    pass


def panic(error_code):
    """makes the micro:bit enter panic mode (this usually happens when the DAL runs
    out of memory, and causes a sad face to be drawn on the display). The error
    code can be any arbitrary integer value.
    """
    pass


def temperature():
    """Return the temperature of the micro:bit in degrees Celcius."""
    pass


def reset():
    """resets the micro:bit."""
    pass


class _MicroBitDigitalPin:
    def write_digital(self, value):
        """value can be 0, 1, False, True"""
        pass

    def read_digital(self):
        """returns either 1 or 0"""
        pass


class _MicroBitAnalogDigitalPin(_MicroBitDigitalPin):
    def write_analog(self, value):
        """value is between 0 and 1023"""
        pass

    def read_analog(self):
        """returns an integer between 0 and 1023"""
        pass

    def set_analog_period(self, int):
        """sets the period of the PWM output of the pin in milliseconds
        (see https://en.wikipedia.org/wiki/Pulse-width_modulation)
        """
        pass

    def set_analog_period_microseconds(self, int):
        """sets the period of the PWM output of the pin in microseconds
        (see https://en.wikipedia.org/wiki/Pulse-width_modulation)
        """
        pass


class _MicroBitTouchPin(_MicroBitAnalogDigitalPin):
    def is_touched(self):
        """returns boolean"""
        pass


pin0 = _MicroBitTouchPin()
pin1 = _MicroBitTouchPin()
pin2 = _MicroBitTouchPin()
pin3 = _MicroBitAnalogDigitalPin()
pin4 = _MicroBitAnalogDigitalPin()
pin5 = _MicroBitDigitalPin()
pin6 = _MicroBitDigitalPin()
pin7 = _MicroBitDigitalPin()
pin8 = _MicroBitDigitalPin()
pin9 = _MicroBitDigitalPin()
pin10 = _MicroBitAnalogDigitalPin()
pin11 = _MicroBitDigitalPin()
pin12 = _MicroBitDigitalPin()
pin13 = _MicroBitDigitalPin()
pin14 = _MicroBitDigitalPin()
pin15 = _MicroBitDigitalPin()
pin16 = _MicroBitDigitalPin()
pin19 = _MicroBitDigitalPin()
pin20 = _MicroBitDigitalPin()


class _Button:
    """Represents a button."""

    def is_pressed(self):
        """Returns True if the specified button button is pressed, and False otherwise."""
        pass

    def was_pressed(self):
        """Returns True or False to indicate if the button was pressed since the device
        started or the last time this method was called.
        """
        pass

    def get_presses(self):
        """Returns the running total of button presses."""
        pass

    def reset_presses(self):
        """Resets the running total of button presses to zero."""


button_a = _Button()
button_b = _Button()


class Image:

    def __init__(self, string=None, width=None, height=None, buffer=None):
        """If string is used, it has to consist of digits 0-9 arranged into lines, describing the image, for example:

        image = Image("90009:"
                      "09090:"
                      "00900:"
                      "09090:"
                      "90009")
        will create a 5×5 image of an X. The end of a line is indicated by a colon.
        It’s also possible to use a newline (n) to indicate the end of a line like this:

        image = Image("90009\n"
                      "09090\n"
                      "00900\n"
                      "09090\n"
                      "90009")
        The other form creates an empty image with width columns and height rows.
        Optionally buffer can be an array of width``×``height integers in range 0-9 to initialize the image.
        """
        pass

    def width(self):
        """Return the number of columns in the image."""
        pass

    def height(self):
        """Return the numbers of rows in the image."""
        pass

    def set_pixel(self, x, y, value):
        """Set the brightness of the pixel at column x and row y to the value,
        which has to be between 0 (dark) and 9 (bright).

        This method will raise an exception when called on any of the build-in read-only images, like Image.HEART.
        """
        pass

    def get_pixel(self, x, y):
        """Return the brightness of pixel at column x and row y as an integer between 0 and 9."""
        pass

    def shift_left(self, n):
        """Return a new image created by shifting the picture left by n columns."""
        pass

    def shift_right(self, n):
        """Same as image.shift_left(-n)."""
        pass

    def shift_up(self, n):
        """Return a new image created by shifting the picture up by n rows."""
        pass

    def shift_down(self, n):
        """Same as image.shift_up(-n)."""
        pass


Image.HEART = Image()
Image.HEART_SMALL = Image()
Image.HAPPY = Image()
Image.SMILE = Image()
Image.SAD = Image()
Image.CONFUSED = Image()
Image.ANGRY = Image()
Image.ASLEEP = Image()
Image.SURPRISED = Image()
Image.SILLY = Image()
Image.FABULOUS = Image()
Image.MEH = Image()
Image.YES = Image()
Image.NO = Image()

Image.CLOCK12 = Image()
Image.CLOCK11 = Image()
Image.CLOCK10 = Image()
Image.CLOCK9 = Image()
Image.CLOCK8 = Image()
Image.CLOCK7 = Image()
Image.CLOCK6 = Image()
Image.CLOCK5 = Image()
Image.CLOCK4 = Image()
Image.CLOCK3 = Image()
Image.CLOCK2 = Image()
Image.CLOCK1 = Image()
Image.ALL_CLOCKS = {Image.CLOCK1, Image.CLOCK2, Image.CLOCK3, Image.CLOCK4, Image.CLOCK5, Image.CLOCK6,
                    Image.CLOCK7, Image.CLOCK8, Image.CLOCK9, Image.CLOCK10, Image.CLOCK11, Image.CLOCK12}

Image.ARROW_N = Image()
Image.ARROW_NE = Image()
Image.ARROW_E = Image()
Image.ARROW_SE = Image()
Image.ARROW_S = Image()
Image.ARROW_SW = Image()
Image.ARROW_W = Image()
Image.ARROW_NW = Image()
Image.ALL_ARROWS = {Image.ARROW_N, Image.ARROW_NE, Image.ARROW_E, Image.ARROW_SE,
                    Image.ARROW_S, Image.ARROW_SW, Image.ARROW_W, Image.ARROW_NW}

Image.TRIANGLE = Image()
Image.TRIANGLE_LEFT = Image()
Image.CHESSBOARD = Image()
Image.DIAMOND = Image()
Image.DIAMOND_SMALL = Image()
Image.SQUARE = Image()
Image.SQUARE_SMALL = Image()
Image.RABBIT = Image()
Image.COW = Image()
Image.MUSIC_CROTCHET = Image()
Image.MUSIC_QUAVER = Image()
Image.MUSIC_QUAVERS = Image()
Image.PITCHFORK = Image()
Image.XMAS = Image()
Image.PACMAN = Image()
Image.TARGET = Image()
Image.TSHIRT = Image()
Image.ROLLERSKATE = Image()
Image.DUCK = Image()
Image.HOUSE = Image()
Image.TORTOISE = Image()
Image.BUTTERFLY = Image()
Image.STICKFIGURE = Image()
Image.GHOST = Image()
Image.SWORD = Image()
Image.GIRAFFE = Image()
Image.SKULL = Image()
Image.UMBRELLA = Image()
Image.SNAKE = Image()
