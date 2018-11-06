# SYSC 1005 A Fall 2018 Lab 7

import sys  # get_image calls exit
from Cimpl import *
from lab_7_filters import *

def get_image():
    """
    Interactively select an image file and return a Cimpl Image object
    containing the image loaded from the file.
    """

    # Pop up a dialogue box to select a file
    file = choose_file()

    # Exit the program if the Cancel button is clicked.
    if file == "":
        sys.exit("File Open cancelled, exiting program")

    # Open the file containing the image and load it
    img = load_image(file)

    return img

# A bit of code to demonstrate how to use get_image().

def main():
    print('What do you want to do?:')
    print('L)oad image')
    print('N)egative')
    print('Q)uit')
    
    user = input('What do you choose son?:')
    
    if user == 'L' or user == 'l':
        show(get_image())
    elif user == 'N' or user == 'n':
        show(negative(get_image))
    elif user == 'Q' or user == 'q':
        print('Quitting the program')
    else:
        print('That not right, woops')


if __name__ == "__main__":
    main()
