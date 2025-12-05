import numpy as np

def get_canvas_buffer (canvas):
    try:
        return canvas.buffer_rgba()
    except AttributeError:
        return canvas.tostring_rgb()