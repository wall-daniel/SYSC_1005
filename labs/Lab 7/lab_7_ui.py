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
    done = False
    img = None
    while not done:
        print('\nWhat do you want to do?:')
        print('L)oad image')
        print('N)egative', end=' ')
        print('G)rayscale', end=' ')
        print('S)olarize', end=' ')
        print('2)-tone', end=' ')
        print('3)-tone')
        print('Q)uit')
        
        command = input('What do you choose son?:')
        
        if command == 'L' or command == 'l':
            img = get_image()
        elif command == 'Q' or command == 'q':
            done = True        
        elif command in ['N', 'n', 'G', 'g', 'S', 's', '2', '3']:
            if img != None:
                if command == 'N' or command == 'n':
                    img = negative(img)
                elif command == 'G' or command == 'g':
                    img = grayscale(img)
                elif command == 'S' or command == 's':
                    # Need to get what threshold first
                    command = input('What threshold to use?: ')
                    img = solarize(img, int(command))
                elif command == '2':
                    img = black_and_white(img)
                elif command == '3':
                    img = black_and_white_and_gray(img)
                
                # Show image after running whatever filter wanted
                show(img)
            else:
                print('Can\'t run that without an image loaded, try again m8')
        else:
            print('That\'s not a correct command')


if __name__ == "__main__":
    main()
