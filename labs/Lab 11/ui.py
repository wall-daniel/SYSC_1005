# SYSC 1005 A Fall 2018 Lab 7

import sys  # get_image calls exit
from Cimpl import *
from filters import *

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
    done = False
    img = None
    while not done:
        print('\nWhat do you want to do?:')
        print('L)oad image')
        print('B)lur', end=' ')
        print('E)dge detect', end=' ')
        print('P)osturize', end=' ')
        print('S)catter', end=' ')
        print('T)int sepia', end=' ')
        print('W)eighted grayscale', end=' ')
        print('X)treme contrast')
        print('Q)uit')
        
        command = input('Which option bud?:')
        
        if command == 'L' or command == 'l':
            img = get_image()
        elif command == 'Q' or command == 'q':
            done = True        
        elif command in ['B', 'b', 'E', 'e', 'P', 'p', 'S', 's', 'T', 't', 'W', 'w', 'X', 'x']:
            if img != None:
                if command == 'B' or command == 'b':
                    img = blur(img)
                elif command == 'E' or command == 'e':
                    # Need to get threshold first
                    threshold = int(input('Please enter a threshold value: '))
                    img = detect_edges_better(img, threshold)
                elif command == 'P' or command == 'p':
                    img = posterize(img)
                elif command == 'S' or command == 's':
                    # First get threshold of how much scatter
                    threshold = int(input('What threshold to use?: '))
                    img = scatter(img, threshold)
                elif command == 'T' or command == 't':
                    img = sepia_tint(img)
                elif command == 'W' or command == 'w':
                    img = weighted_grayscale(img)
                elif command == 'X' or command == 'x':
                    img = extreme_contrast(img)
                
                # Show image after running whatever filter wanted
                show(img)
            else:
                print('Can\'t run that without an image loaded, try again man')
        else:
            print('That\'s not a correct command')
            
    print('Have a nice day')


if __name__ == "__main__":
    main()
