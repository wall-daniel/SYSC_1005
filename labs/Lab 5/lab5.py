from Cimpl import *

def grayscale(image):
    new_image = copy(image)
    
    for x, y, (r, g, b) in image:
        grey = r * 0.299 + g * 0.587 + b * 0.114
        set_color(new_image, x, y, create_color(grey, grey, grey))
        
    return new_image

file = choose_file()
image = load_image(file)

show(grayscale(image))