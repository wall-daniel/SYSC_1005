# SYSC 1005 Fall 2018

from Cimpl import *

def blur(image):
    """ (Cimpl.Image) -> Cimpl.Image
    
    Return a new image that is a blurred copy of image.
    
    original = load_image(choose_file())
    blurred = blur(original)
    show(blurred)    
    """  
    target = copy(image)
    
    # Recall that the x coordinates of an image's pixels range from 0 to
    # get_width() - 1, inclusive, and the y coordinates range from 0 to
    # get_height() - 1.
    #
    # To blur the pixel at location (x, y), we use that pixel's RGB components,
    # as well as the components from the four neighbouring pixels located at
    # coordinates (x - 1, y), (x + 1, y), (x, y - 1) and (x, y + 1).
    #
    # When generating the pixel coordinates, we have to ensure that (x, y)
    # is never the location of pixel on the top, bottom, left or right edges
    # of the image, because those pixels don't have four neighbours.
    #
    # As such, we can't use this loop to generate the x and y coordinates:
    #
    # for y in range(0, get_height(image)):
    #     for x in range(0, get_width(image)):
    #
    # With this loop, when x or y is 0, subtracting 1 from x or y yields -1, 
    # which is not a valid coordinate. Similarly, when x equals get_width() - 1 
    # or y equals get_height() - 1, adding 1 to x or y yields a coordinate that
    # is too large.
    
    for y in range(1, get_height(image) - 1):
        for x in range(1, get_width(image) - 1):

            # Grab the pixel @ (x, y) and its four neighbours

            top_red, top_green, top_blue = get_color(image, x, y - 1)
            left_red, left_green, left_blue = get_color(image, x - 1, y)
            bottom_red, bottom_green, bottom_blue = get_color(image, x, y + 1)
            right_red, right_green, right_blue = get_color(image, x + 1, y)
            center_red, center_green, center_blue = get_color(image, x, y)
            top_left_red, top_left_green, top_left_blue = get_color(image, x - 1, y - 1)
            top_right_red, top_right_green, top_right_blue = get_color(image, x + 1, y - 1)   
            bottom_left_red, bottom_left_green, bottom_left_blue = get_color(image, x - 1, y + 1)
            bottom_right_red, bottom_right_green, bottom_right_blue = get_color(image, x + 1, y + 1)         

            # Average the red components of the five pixels
            new_red = (top_red + left_red + bottom_red +
                       right_red + center_red + top_left_red
                       + top_right_red + bottom_left_red + bottom_right_red) // 9

            # Average the green components of the five pixels
            new_green = (top_green + left_green + bottom_green +
                        right_green + center_green  + top_left_green
                       + top_right_green + bottom_left_green + bottom_right_green) // 9

            # Average the blue components of the five pixels
            new_blue = (top_blue + left_blue + bottom_blue +
                        right_blue + center_blue + top_left_blue
                       + top_right_blue + bottom_left_blue + bottom_right_blue) // 9

            new_color = create_color(new_red, new_green, new_blue)
            
            # Modify the pixel @ (x, y) in the copy of the image
            set_color(target, x, y, new_color)

    return target


def test_blur():
    original = load_image(choose_file())
    blurred = blur(original)
    show(blurred)
    
    
def make_very_blurry(number_of_blurs):
    image = load_image(choose_file())
    
    for i in range(number_of_blurs):
        image = blur(image)  # Blur the image repeatedly

    show(image)  
    
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

def weighted_grayscale(image):
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
        
        brightness = r * 0.299 + g * 0.587 + b * 0.114
        
        # or, brightness = (r + g + b) / 3
        # create_color will convert an argument of type float to an int
        
        gray = create_color(brightness, brightness, brightness)
        set_color(new_image, x, y, gray)
        
    return new_image

def extreme_contrast(image):     
    """ 
    (Cimpl.Image) -> Cimpl.Image 
 
    Return a copy of image, maximizing the contrast between
    the light and dark pixels. 
 
    >>> image = load_image(choose_file())
    >>> new_image = extreme_contrast(image)
    >>> show(new_image)     
    """
    new_image = copy(image)
    
    for x, y, (r, g, b) in image:
        if r < 128:
            r = 0
        else:
            r = 255
        if g < 128:
            g = 0
        else:
            g = 255
        if b < 128:
            b = 0
        else:
            b = 255
            
        set_color(new_image, x, y, create_color(r, g, b))
    
    return new_image

def sepia_tint(image):     
    """ (Cimpl.Image) -> Cimpl.Image 
 
    Return a copy of image in which the colours have been
    converted to sepia tones. 
 
    >>> image = load_image(choose_file())
    >>> new_image = sepia_tint(image)
    >>> show(new_image)
    """ 
    new_image = copy(image)
    
    for x, y, (r, g, b) in weighted_grayscale(image):
        if r < 63:
            set_color(new_image, x, y, create_color(r * 1.1, g, b * 0.9))
        elif r <= 191:
            set_color(new_image, x, y, create_color(r * 1.15, g, b * 0.85))
        else:
            set_color(new_image, x, y, create_color(r * 1.08, g, b * 0.93))
        
    return new_image

def _adjust_component(amount):     
    """ (int) -> int 
 
    Divide the range 0..255 into 4 equal-size quadrants,
    and return the midpoint of the quadrant in which the
    specified amount lies. 
 
    >>> _adjust_component(10)
    31
    >>> _adjust_component(85)
    95
    >>> _adjust_component(142)
    159
    >>> _adjust_component(230)
    223
    """

    if amount > 191:
        return 223
    if amount > 127:
        return 159
    if amount > 63:
        return 95
    return 31

def posterize(img):
    """ (Cimpl.Image) -> Cimpl.Image 
 
    Return a "posterized" copy of image. 
 
    >>> image = load_image(choose_file())
    >>> new_image = posterize(image)
    >>> show(new_image) 
    """ 
    new_image = copy(image)
    
    for x, y, (r, g, b) in image:
        set_color(new_image, x, y, create_color(_adjust_component(r), _adjust_component(g), _adjust_component(b)))
    
    return new_image

# Exercise: This filter doesn't blur the pixels along the image's edges.
# Here is one way we could extend the filter to do this:
#
# Visit the four corner pixels, blurring each one by averaging the pixel's
# components with those of its two neightbours; e.g., blur the pixel
# @ (0, 0) by using the components @ (0, 0), (1, 0) and (0, 1).
#
# Next, visit all the pixels on the edges except for the corner pixels.
# Blur each pixel by averaging the pixel's components with those of its
# three neigbours; e.g., blur the pixel @ (1, 0) by using the components
# @ (1, 0), (0, 0), (1, 1) and (2, 0).
#
# Make this change to the filter.

# Exercise 1
white = create_color(256, 256, 256)
black = create_color(0, 0, 0)

def detect_edges(image, threshold):
    """ (Cimpl.Image, float) -> Cimpl.Image       
    Return a new image that contains a copy of the original image     
    that has been modified using edge detection. 
     
    >>> image = load_image(choose_file())     
    >>> filtered = detect_edges(image, 10.0)     
    >>> show(filtered)    
    """
    new_image = copy(image)
    
    for x in range(1, get_width(image)):
        for y in range(1, get_height(image) - 1):
            r, g, b = get_color(image, x, y)
            tr, tg, tb = get_color(image, x, y + 1)
            
            if abs((r + g + b) // 3 - (tr + tg + tb) // 3) > threshold:
                set_color(new_image, x, y, white)
            else:
                set_color(new_image, x, y, black)
    
    return new_image

def detect_edges_better(image, threshold):
    """ (Cimpl.Image, float) -> Cimpl.Image       
    Return a new image that contains a copy of the original image     
    that has been modified using edge detection. 
     
    >>> image = load_image(choose_file())     
    >>> filtered = detect_edges(image, 10.0)     
    >>> show(filtered)    
    """
    new_image = copy(image)
    
    for x in range(1, get_width(image) - 1):
        for y in range(1, get_height(image) - 1):
            r, g, b = get_color(image, x, y)
            tr, tg, tb = get_color(image, x, y + 1)
            rr, rg, rb = get_color(image, x + 1, y)
            
            if abs((r + g + b) // 3 - (tr + tg + tb) // 3) > threshold or abs((r + g + b) // 3 - (rr + rg + rb) // 3) > threshold:
                set_color(new_image, x, y, white)
            else:
                set_color(new_image, x, y, black)
    
    return new_image

image = load_image(choose_file())
show(detect_edges(image, 12))
show(detect_edges_better(image, 12))
show(blur(image))