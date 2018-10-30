""" SYSC 1005 A Fall 2018.

Filters for a photo-editing application.
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

file = choose_file()
image = load_image(file)

show(grayscale(image))
show(weighted_grayscale(image))
show(extreme_contrast(image))
show(sepia_tint(image))
show(posterize(image))