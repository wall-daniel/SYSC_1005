from Cimpl import *
import random

def red_channel(image):
    return modify_brightness(image, 1, 0, 0)

def green_channel(image):
    return modify_brightness(image, 0, 1, 0)    

def blue_channel(image):
    return modify_brightness(image, 0, 0, 1) 

def modify_brightness(image, red_brightness, green_brightness, blue_brightness):
    """
    (image) - > image
    
    Modifies the brightness of every pixel by the amounts specified.
    The values should be in between 0.0 and 1.0.
    """
    new_image = copy(image)
    
    for x, y, (r, g, b) in image:
        new_color = create_color(r * red_brightness, g * green_brightness, b * blue_brightness)
        set_color(new_image, x, y, new_color)
        
    return new_image

def swap_red_blue(image):
    new_image = copy(image)
    
    for x, y, (r, g, b) in image:
        new_color = create_color(b, g, r)
        set_color(new_image, x, y, new_color)
        
    return new_image    

def hide_image(image):
    new_image = copy(image)
    
    for x, y, (r, g, b) in image:
        new_red = (r + g + b) / 30
        new_color = create_color(new_red, random.randint(0, 255), random.randint(0, 255))
        set_color(new_image, x, y, new_color)
        
    return new_image      

def recover_image(image):
    new_image = copy(image)
    
    for x, y, (r, g, b) in image:
        new_color = create_color(r * 30, r * 30, r * 30)
        set_color(new_image, x, y, new_color)
        
    return new_image      

def main():
    file = choose_file()
    image = load_image(file)
    
    # Show the original image
    #show(image)
    
    # Recover the image
    show(recover_image(hide_image(image)))
    
    # Hiding the image
    #show(hide_image(image))
    
    # Swap the red and blue
    #show(swap_red_blue(image))
    
    # Modify brightness of the photo
    #show(modify_brightness(image, 2, 2, 2))
    #show(modify_brightness(image, 0.5, 0.5, 0.5))
    
    # Show the channel of the colours
    #show(red_channel(image))
    #show(green_channel(image))
    #show(blue_channel(image))

if __name__ == "__main__":
    main()