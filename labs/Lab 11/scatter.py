from Cimpl import *
import random

def scatter(image):
    """ (Cimpl.image) -> Cimpl.image
    
    Return a new image that looks like a copy of an image in which the pixels
    have been randomly scattered. 
    
    >>> original = load_image(choose_file())
    >>> scattered = scatter(original)
    >>> show(scattered)    
    """
    # Create an image that is a copy of the original.
    
    new_image = copy(image)
    
    # Visit all the pixels in new_image.
    
    for x, y, (r, g, b) in image:
        
        # Generate the row and column coordinates of a random pixel
        # in the original image. Repeat this step if either coordinate
        # is out of bounds.
        
        row_and_column_are_in_bounds = False
        while not row_and_column_are_in_bounds:
            
            # Generate two random numbers between -10 and 10, inclusive.
            
            rand1 = random.randint(-10, 10)
            rand2 = random.randint(-10, 10)
            
            # Calculate the column and row coordinates of a
            # randomly-selected pixel in image.

            random_column = x + rand1
            random_row = y + rand2  
            
            # Determine if the random coordinates are in bounds.

            if (random_column >= 0 and random_column < image.get_width()) and (random_row >= 0 and random_row < image.get_height()):
                #print(str(random_column) + ' ' + str(random_row))
                row_and_column_are_in_bounds = True
                    
        # Get the color of the randomly-selected pixel.
        
        new_colour = get_color(image, random_column, random_row)
        
        # Use that color to replace the color of the pixel we're visiting.
        
        set_color(new_image, x, y, new_colour)
                    
    # Return the scattered image.
    return new_image

def change_img(image):
    new_image = copy(image)
    
    for x, y, (r,g ,b) in image:
        if r > 128:
            r = 255
        else:
            r = 0
        if g > 128:
            g = 255
        else:
            g = 0
        if b > 128:
            b = 255
        else:
            b = 0
            
        set_color(new_image, x, y, create_color(r, g, b))
        
    return new_image

image = load_image(choose_file())
show(change_img(image))