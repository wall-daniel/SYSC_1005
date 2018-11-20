import math

def distance(pt1, pt2):
    """
    (number, number) --> float
    
    Returns the distance between two points on a cartesian plain
    """
    return math.sqrt((pt2[0] - pt1[0]) ** 2 + (pt2[1] - pt1[1]) ** 2)
        
        
def read_and_print_lines():
    infile = open('data.txt', 'r')
    for line in infile:
        print(line)
    infile.close()
    
    
#print(distance((0,2), (1,3)))