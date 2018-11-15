import numpy as np
import math

def zero_crossing_detector(x):
    """
    A function to count the number of times a list of floats crosses the
    value x = 0
    :param x: A list of floats representing movement in 1-D space
    :return: An integer representing the number of times the trajectory
    has crossed x = 0
    """

    # This holds information about the positivity of the current trajectory
    pos = True

    # This holds information about the number of times a crossing event has occurred
    count = 0

    if x.pop(0) >= 0:
        pos = True

    # Loop through x and note the number of times the sign has changed
    for i in x:
        if i < 0 and pos:
            count += 1
            pos = False
        elif i > 0 and not pos:
            count += 1
            pos = True

    return count


def zero_crossing_detector_2d(v):
    """
    A function to count the number of times a list of (x,y) tuples of floats crosses the
    plane y = 0. This is nothing but checking whether the y coordinate has crossed 0
    :param v: A list of (x,y) tuples of floats representing movement in 2-D space
    :return: An integer representing the number of times the trajectory
    has crossed y = 0
    """

    # This holds information about the positivity of the current trajectory
    pos = True

    # This holds information about the number of times a crossing event has occurred
    count = 0

    # Get the y coordinates
    x = [j for (i, j) in v]

    if x.pop(0) >= 0:
        pos = True

    # Loop through z and note the number of times the sign has changed
    for i in x:
        if i < 0 and pos:
            count += 1
            pos = False
        elif i > 0 and not pos:
            count += 1
            pos = True

    return count


def value_crossing_detector(x, a):
    """
    A function to count the number of times a list of floats crosses
    the value x = a where a is a user defined value
    :param x: A list of floats representing movement in 1-D space
    :param a: A user specified value to check whether it is crossed by
    the trajectory
    :return: An integer representing the number of times the trajectory
    has crossed x = a
    """

    return zero_crossing_detector(list(map(lambda i: i-a, x)))


def value_crossing_detector_2d(v, a):
    """
    A function to count the number of times a list of (x,y) tuples of floats crosses
    the line defined by the two user given tuples (x1,y1) and (x2,y2)
    :param v: A list of (x,y) tuples of floats representing movement in 2-D space
    :param a: A user specified list of two (x,y) tuples check whether it is crossed by
    the trajectory
    :return: An integer representing the number of times the trajectory
    has crossed y = a
    """

    # Step 1: Shift both v and a so that the user defined line passes through the origin
    #         Let a = [(x1,y1),(x2,y2)]. Then user defined line is
    #         y = ((y2-y1)/(x2-x1)) * x1 + (y1*x2-y2*x1)/(x2-x1)
    #         So we need to shift along the y coordinate by -(y1*(1+x1) - y2*x1)/(x2-x1)
    y_shift = -(a[0][1]*a[1][0] - a[1][1]*a[0][0])/(a[1][0]-a[0][0])
    y_shifted = [[i, j + y_shift] for (i, j) in v]
    a_shifted = [[a[0][0], a[0][1] + y_shift], [a[1][0], a[1][1] + y_shift]]

    # Step 2: Calculate the angle between the shifted user defined line and the x-axis
    #         Cos(angle) = (u.w)/(|u||w|) for two general vectors u, v passing through the origin
    #         Here, u is the x-axis so u = [0,1] and |u| = 1.
    #         w is the user defined vector but since we shifted it to pass through (0,0) we only need one of the lists
    #         in v. So w = v[0] unless this is the list [0,0] in which case w = v[1]
    #         Also, u.w = [1,0].w = w[0]
    u = [0, 1]
    if (a_shifted[0][0] == 0) and (a_shifted[0][1] == 0):
        w = [a_shifted[1][0], a_shifted[1][1]]
    else:
        w = [a_shifted[0][0], a_shifted[0][1]]

    norm = np.linalg.norm(w)

    angle = math.acos(w[0]/norm)

    # Step 3: Rotate both v and a so that the shifted user defined line is the y = 0 line
    #         (u',v') = (u cos(angle) - v sin(angle), u sin(angle) + v cos(angle))
    y_shifted_rotated = []
    for i in y_shifted:
        y_shifted_rotated.append(((i[0] * math.cos(angle) + i[1] * math.sin(angle)),
                                 (-i[0] * math.sin(angle) + i[1] * math.cos(angle))))

    a_shifted_rotated = []
    for i in a_shifted:
        a_shifted_rotated.append(((i[0] * math.cos(angle) + i[1] * math.sin(angle)),
                                 (-i[0] * math.sin(angle) + i[1] * math.cos(angle))))

    # Step 4: Use the already existing zero crossing detector to check for crossing the x-axis
    return zero_crossing_detector_2d(y_shifted_rotated)


z = [(0, 0), (1, 0), (1, -2), (2, -2), (3, -2), (3, -1), (4, -1), (5, -2), (6, -1), (6, 3), (8, 3), (10, 1), (7, 1),
     (3, 4)]
a = [(0, -2), (10, 3)]

print(value_crossing_detector_2d(z, a))
