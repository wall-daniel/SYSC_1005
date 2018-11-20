"""
SYSC 1005 Fall 2018 Lab 9, Parts 2 and 3
"""
FILENAME = 'data.txt'

def read_points(filename):
    """
    (String) --> list of tuples
    
    Returns a list of points read from the file specified
    """
    infile = open(filename, 'r')
    
    points = []
    for line in infile:
        points.append((float(line.split()[0]), float(line.split()[1])))
    
    return points

def get_points():
    """ (None) -> set of 2-tuples of float
    
    Return a set of (x, y) points, with each point stored in a tuple.
    
    >>> get_points()
    """
    return {(1.0, 5.0), (2.0, 8.0), (3.5, 12.5)}

def fit_line_to_points(points):
    """
    (list of tuples) --> float
    
    Fits the best line to the set of points
    """
    # Pos 1 - sum of x coords
    # Pos 2 - sum of y coord
    # Pos 3 - sum of xy
    # Pos 4 - sum of xx
    # Pos 5 - sum of yy
    sums = [0,0,0,0,0]
    for point in points:
        sums[0] += point[0]
        sums[1] += point[1]
        sums[2] += point[0] * point[1]
        sums[3] += point[0] * point[0]
        sums[4] += point[1] ** 2
        
    slope = ((sums[0] * sums[1]) - (len(points) * sums[2])) / ((sums[0] * sums[0]) - (len(points) * sums[3]))
    y_intercept = (sums[0] * sums[2] - sums[3] * sums[1]) / (sums[0] * sums[0] - len(points) * sums[3])
    
    return (slope, y_intercept)

if __name__ == "__main__":
    values = fit_line_to_points(read_points(FILENAME))
    
    print('The best line of fit for the points is: y = ' + str(values[0]) + 'x + ' + str(values[1]))
