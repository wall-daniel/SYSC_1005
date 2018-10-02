import math

def area_of_circle(radius):
    """ (number) -> float
    Return the area of a ring with the specified non-negative radius.
    
    Example
    >>> area_of_disk(2.0)
    12.57
    """
    return math.pi * radius ** 2
    
def area_of_ring(outer, inner):
    """ (number, number) -> float, float
    
    Returns the area of a ring with radius outer.
    The radius of the hole is inner.
    
    This function requires outer > inner >= 0
    
    >>> area_of_ring(4.0, 2.0)
    37.7
    """
    return area_of_circle(outer) - area_of_circle(inner)

def volume_of_sphere(radius):
    """ (number) -> float
    Return the volume of a sphere with the specified
    non-negative radius.
    
    >>> volume_of_sphere(1)
    4.1887902047863905
    """
    return 4 / 3 * math.pi * radius ** 3

def area_of_cone(height, radius):
    """ (number, number) -> float
    Return the lateral surface area of a right circular
    cone with the specified non-negative height and radius.
    
    >>> area_of_cone(5, 10)
    665.4000019110156
    """
    return area_of_circle(radius) + (math.pi * radius * math.sqrt(radius ** 2 + height ** 2))