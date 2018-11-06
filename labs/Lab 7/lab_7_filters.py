"""
SYSC 1005 Fall 2018

Filters for Lab 7. All of these filters were presented during lectures.
"""

from Cimpl import *

def grayscale(image):
    """ (Cimpl.Image) -> Cimpl.Image
    
    Return a grayscale copy of image.
   
    >>> image = load_image(choose_file())
    >>> gray_image = grayscale(image)
    >>> show(gray_image)
    """
    new_image = copy(image)
    for x, y, (r, g, b) in image:

        # Use the pixel's brightness as the value of RGB components for the 
        # shade of gray. These means that the pixel's original colour and the
        # corresponding gray shade will have approximately the same brightness.
        
        brightness = (r + g + b) // 3
        
        # or, brightness = (r + g + b) / 3
        # create_color will convert an argument of type float to an int
        
        gray = create_color(brightness, brightness, brightness)
        set_color(new_image, x, y, gray)
        
    return new_image


# The negative filter inverts every component of every pixel.
# The solarizing filter invert only those components that have intensities
# below a specified value.

def negative(image):
    """ (Cimpl.Image) -> Cimpl.Image
    
    Return an inverted copy of image; that is, an image that is a colour 
    negative of the original image.
    
    >>> image = load_image(choose_file())
    >>> filtered = negative(image)
    >>> show(filtered)
    """
    new_image = copy(image)
    
    # Invert the intensities of every component in every pixel.
    for  x, y, (r, g, b) in image:
        inverted = create_color(255 - r, 255 - g, 255 - b)
        set_color(new_image, x, y, inverted)

    return new_image


def solarize(image, threshold):
    """ (Cimpl.Image, int) -> Cimpl.Image
    
    Return a "solarized" copy of image. RGB components that have
    intensities less than threshold are modified.
    
    Parameter threshold is in the range 0 to 256, inclusive.
    
    >>> image = load_image(choose_file()) 
    >>> filtered = solarize(image)
    >>> show(filtered)
    """
    new_image = copy(image)
    for x, y, (red, green, blue) in image:

        # Invert the intensities of all RGB components that are less than 
        # threshold.

        if red < threshold:
            red = 255 - red

        if green < threshold:
            green = 255 - green

        if blue < threshold:
            blue = 255 - blue

        col = create_color(red, green, blue)
        set_color(new_image, x, y, col)
        
    return new_image


def black_and_white(image):
    """ (Cimpl.Image) -> Cimpl.Image
    
    Return a black-and-white (two-tone) copy of image.
    
    >>> image = load_image(choose_file()) 
    >>> filtered = black_and_white(image)
    >>> show(filtered)
    """
    new_image = copy(image)
    black = create_color(0, 0, 0)
    white = create_color(255, 255, 255)

    # Brightness levels range from 0 to 255.
    # Change the colour of each pixel to black or white, depending on
    # whether its brightness is in the lower or upper half of this range.

    for x, y, (red, green, blue) in image:
        brightness = (red + green + blue) // 3
        
        if brightness < 128:  # brightness is between 0 and 127, inclusive
            set_color(new_image, x, y, black)
        else:     # brightness is between 128 and 255, inclusive
            set_color(new_image, x, y, white)
            
    return new_image


def black_and_white_and_gray(image):
    """ (Cimpl.Image) -> Cimpl.Image
    
    Return a black-and-white-and gray (three-tone) copy of image.

    >>> image = load_image(choose_file()) 
    >>> filtered = black_and_white_and_gray(image)
    >>> show(filtered)
    """
    new_image = copy(image)
    black = create_color(0, 0, 0)
    gray = create_color(128, 128, 128)
    white = create_color(255, 255, 255)

    # Brightness levels range from 0 to 255. Change the colours of every
    # pixel whose brightness is in the lower third of this range to black,
    # in the upper third to white, and in the middle third to medium-gray.

    for x, y, (red, green, blue) in image:
        brightness = (red + green + blue) // 3

        if brightness < 85:    # brightness is between 0 and 84, inclusive
            set_color(new_image, x, y, black)
        elif brightness < 171: # brightness is between 85 and 170, inclusive
            set_color(new_image, x, y, gray)
        else:                  # brightness is between 171 and 255, inclusive
            set_color(new_image, x, y, white)

    return new_image


#-------------------------------------
# A few functions to test the filters.

def test_grayscale(image):
    gray_image = grayscale(image)
    show(gray_image)

def test_negative(image):
    inverted_image = negative(image)
    show(inverted_image)
    
def test_solarize(image):
    solarized_image = solarize(image, 64)
    show(solarized_image)

    solarized_image = solarize(image, 128)
    show(solarized_image)

    solarized_image = solarize(image, 192)
    show(solarized_image)
    
    solarized_image = solarize(image, 256)
    show(solarized_image)    
    
def test_black_and_white(image):
    b_w_image = black_and_white(image)
    show(b_w_image)

def test_black_and_white_and_gray(image):
    b_w_g_image = black_and_white_and_gray(image)
    show(b_w_g_image)

# print(__name__)
if __name__ == "__main__":
    original = load_image(choose_file())
    show(original)
    
    test_grayscale(original)
    test_negative(original)
    test_solarize(original)
    test_black_and_white(original)
    test_black_and_white_and_gray(original)
