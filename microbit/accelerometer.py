def get_x():
    """Get the acceleration measurement in the x axis, as a positive or negative integer, depending on the direction."""
    pass


def get_y():
    """Get the acceleration measurement in the y axis, as a positive or negative integer, depending on the direction."""
    pass


def get_z():
    """Get the acceleration measurement in the z axis, as a positive or negative integer, depending on the direction."""
    pass


def get_values():
    """Get the acceleration measurements in all axes at once,
    as a three-element tuple of integers ordered as X, Y, Z.
    """
    pass


def current_gesture():
    """Return the name of the current gesture.

    MicroPython understands the following gesture names:
    "up", "down", "left", "right", "face up", "face down", "freefall", "3g", "6g", "8g", "shake".
    Gestures are always represented as strings.
    """
    pass


def is_gesture(name):
    """Return True or False to indicate if the named gesture is currently active."""
    pass


def was_gesture(name):
    """Return True or False to indicate if the named gesture was active since the last call."""
    pass


def get_gestures():
    """Return a tuple of the gesture history. The most recent is listed last."""
    pass


def reset_gestures():
    """Clears the gesture history."""
    pass
