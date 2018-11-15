def zero_crossing_detector(x):
    """
    A function to count the number of times a list of floats crosses the
    line y = 0
    :param x: A list of floats representing movement in 2-D space
    :return: An integer representing the number of times the trajectory
    has crossed y = 0
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


def value_crossing_detector(x, a):
    """
    A function to count the number of times a list of floats crosses
    the line y = a where a is a user defined value
    :param x: A list of floats representing movement in 2-D space
    :return: An integer representing the number of times the trajectory
    has crossed y = a
    """

    return zero_crossing_detector(list(map(lambda i: i-a, x)))


print(zero_crossing_detector([5, 1, 2, -3, 4, 5, 0, 0, 0, -1, 0]))

print(value_crossing_detector([5, 1, 2, -3, 4, 5, 0, 0, 0, -1, 0], -2))
