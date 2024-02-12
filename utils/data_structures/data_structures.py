# ****************************** 2D LISTS ****************************************
import copy


def generate_empty_2D_list(n_rows=9, n_columns=9):
    """
    Creates and return an "empty" bidimensional list of n_rows x n_columns cells.
    :return: An "empty" bidimensional list = [[None * n_columns]*n_rows]
    """
    return [[None for _ in range(0, n_columns, 1)] for _ in range(0, n_rows, 1)]


def insert_values_in_2D_list_giving_coordinates(_2D_list, values_list, coordinates):
    """
    Returns a list with the values found in the values_list inserted in the coordinates indicated as a parameter.
    Initially, the list to be returned will be a deep copy of the parameter _2D_list (bidimensional list).\n
    In that deep copy, the function will insert in the indicated coordinates the values found in values_list.
    :param _2D_list: the base list
    :param values_list: the list of values to insert
    :param coordinates: the coordinates where the values will be inserted
    :return: a deep copy of the _2D_list(input param) in which the function has inserted in the indicated
    coordinates(input param) the values found in the values_list(input param).
    """
    _2D_list_copy = copy.deepcopy(_2D_list)

    for index, value in enumerate(values_list):
        row = coordinates[index][0]
        column = coordinates[index][1]
        _2D_list_copy[row][column] = value

    return _2D_list_copy


def get_coordinates_in_2D_list_of(_2D_list, empty_cells=False):
    """
    Returns a list of tuples (row,column). Each tuple (row,column) is the coordinate of an empty cell (contains None)
    in the _2D_list if the empty_cells parameter is True or the coordinate of a non-empty cell otherwise.
    :param _2D_list: The list (bidimensional) where to look for the empty or non-empty cells.
    :param empty_cells: If True the function will look for empty cells.
    If false the function will look for non-empty cells.
    :return: A list of tuples (row,column) with the coordinates of the empty or non-empty cells found.
    """
    coordinates_list = list()
    n_rows = len(_2D_list)
    n_columns = len(_2D_list[0])
    for row in range(0, n_rows, 1):
        for column in range(0, n_columns, 1):
            if _2D_list[row][column] is None:
                if empty_cells:
                    coordinates_list.append((row, column))
            else:
                if not empty_cells:
                    coordinates_list.append((row, column))

    return coordinates_list


def get_values_in_2D_list(_2D_list, zone, *args):
    """
    Return a list of values found in the zone of the _2D_list (bibimensional list).
    :param _2D_list: The list (bidimensional) where to look for the values.
    :param zone: Can be:\n  zone = 'row' or zone = 'column' or zone = 'coordinates'.
    :param args: If zone = 'row' args[0] will be the number or row (zero included)\n
    If zone = 'column' args[0] will be the number or column (zero included)\n
    If zone = 'coordinates' args[0] will be a list of coordinates (tuples) where to find the values to return\n
    :return: A list with the values found in the giving zone.
    """
    values = []
    if zone == 'row':
        row_number = args[0]
        for value in _2D_list[row_number]:
            values.append(value)
    elif zone == 'column':
        column_number = args[0]
        for value in [row[column_number] for row in _2D_list]:
            values.append(value)
    elif zone == 'coordinates':
        coordinates_list = args[0]
        for coordinate in coordinates_list:
            values.append(_2D_list[coordinate[0]][coordinate[1]])
    else:
        pass
    return values


def value_appearances_in(_2D_list, coordinates_list, matching_value):
    number_appearances = 0
    for coordinate in coordinates_list:
        try:
            if int(_2D_list[coordinate[0]][coordinate[1]]) == int(matching_value):
                number_appearances = number_appearances + 1
        except TypeError:
            # if you are here is because value is None. Nothing to do then
            pass
    return number_appearances


def get_2D_list_position_coordinates(_2D_list, actual_position, next_or_previous='next_position'):
    """
    Given a _2D_list is implemented as double list array like this:
    [[None for _ in range(0, n_columns, 1)] for _ in range(0, n_rows, 1)].
    Based on that _2D_list implementation, the function use get_2D_list_previous_coordinates or
    get_2D_list_next_coordinates functions to return (based on the next_or_previous parameter) the values of
    row and column for the previous or the next cell.
    :param _2D_list: The double list array implementation.
    :param actual_position: A list or tuple with the row and the column of the actual position.
    :param next_or_previous: String that tells to the function which cell return, the previous or the next.
    :return: The values of row and column for the previous or the next cell based on the next_or_previous parameter.
    """
    if next_or_previous == 'next_position':
        return _get_2D_list_next_coordinates(_2D_list, actual_position[0], actual_position[1])
    else:
        return _get_2D_list_previous_coordinates(_2D_list, actual_position[0], actual_position[1])


def _get_2D_list_previous_coordinates(_2D_list, actual_row_index, actual_column_index):
    """
    Given a _2D_list is implemented as double list array like this:
    [[None for _ in range(0, n_columns, 1)] for _ in range(0, n_rows, 1)].
    Based on that _2D_list implementation, the function will return the previous cell coordinates
    (values of the row and the column for the previous position) given the actual position
    (actual_row_index, actual_column_index):
    :param _2D_list: The double list array implementation.
    :param actual_row_index: The row of the actual position.
    :param actual_column_index: The column of the actual position.
    :return: The values of row and column for the previous cell or 0,0 if actual_row_index, actual_column_index
    are the coordinates of the first cell (the upper-left) of the _2D_list.
    """
    n_columns = len(_2D_list[0])

    if actual_column_index == 0 and actual_row_index == 0:
        return actual_row_index, actual_column_index
    elif ((actual_column_index > 0 and actual_row_index == 0) or
          (actual_column_index > 0 and actual_row_index > 0)):
        return actual_row_index, actual_column_index - 1
    else:
        return actual_row_index - 1, n_columns - 1


def _get_2D_list_next_coordinates(_2D_list, actual_row_index, actual_column_index):
    """Given a _2D_list is implemented as double list array like this:
    [[None for _ in range(0, n_columns, 1)] for _ in range(0, n_rows, 1)].
    Based on that _2D_list implementation, the function will return the next cell coordinates
    (values of the row and the column for the next position) given the actual position
    (actual_row_index, actual_column_index):
    :param _2D_list: The double list array implementation.
    :param actual_row_index: The row of the actual position.
    :param actual_column_index: The column of the actual position.
    :return: The values of row and column for the next cell or len(_2D_list), len(_2D_list[0])
    if actual_row_index, actual_column_index are the coordinates of the last cell (the bottom-right) of the _2D_list.
    """
    n_rows = len(_2D_list)
    n_columns = len(_2D_list[0])

    if actual_column_index == n_columns - 1 and actual_row_index == n_rows - 1:
        return actual_row_index, actual_column_index
    elif ((actual_column_index < n_columns - 1 and actual_row_index == n_rows - 1) or
          (actual_column_index < n_columns - 1 and actual_row_index < n_rows - 1)):
        return actual_row_index, actual_column_index + 1
    else:
        return actual_row_index + 1, 0


def get_nonet_coordinates(row, column):
    """
    Get the Nonet Coordinates of a cell (row and column of the cell is passed as input parameters).
    In a 2D list 9x9 cells, A Nonet is a sub 2D List of 3x3 inside the parent 2D List (the biggest). So,
    a 2D list of 9x9 cells has got 9 Nonets (3x3).
    :param row: The row of the cell, which we want to know which Nonet belong to.
    :param column: The column of the cell, which we want to know which Nonet belong to.
    :return: Pair of integers (row, column) that indicates the coordinates of the nonet that contains the cell.
    """
    nonet_row = nonet_column = None
    if 2 >= row >= 0:
        nonet_row = 0
    elif 5 >= row >= 3:
        nonet_row = 1
    elif 8 >= row >= 6:
        nonet_row = 2
    if 2 >= column >= 0:
        nonet_column = 0
    elif 5 >= column >= 3:
        nonet_column = 1
    elif 8 >= column >= 6:
        nonet_column = 2
    return nonet_row, nonet_column


def _get_2D_list_sublist_coordinates(initial_coordinates, final_coordinates):
    """
    Return a list of coordinates of a bidiminensional sublist (an Area) given the initial coordinates (x0,y0) and
    the final coordinates (x1, y1). Zero counts and last numbers of the coordinates also counts.
    :param initial_coordinates: Initial coordinates (x0,y0) or (row, column)
    :param final_coordinates: Final coordinates (x1,y1) or (row, column)
    :return: List of coordinates of the bidiminensional sublist [[]*n_rows]*n_culumns that represent the area defined
    by the initial_coordinates and final_coordinates.
    """
    coordinates = []
    for row in range(initial_coordinates[0], final_coordinates[0] + 1):
        for column in range(initial_coordinates[1], final_coordinates[1] + 1):
            coordinates.append((row, column))
    return coordinates


if __name__ == "__main__":
    dd_list = generate_empty_2D_list()
    print(dd_list)
    dd_list = [[-1, 3, 4, -5, 8, 9, 8, 9, 9],  # 0
               [1, 3, 4, -5, 8, 9, 8, 9, 9],  # 1
               [1, 3, 4, -5, 4, 9, 8, 9, 9],  # 2
               [1, 3, 4, -5, 8, 9, 8, 9, 9],  # 3
               [1, 3, 4, -5, 20, 9, 8, 9, 9],  # 4
               [2, 3, 4, -5, 8, 4, 8, 8, 8],  # 5
               [1, -3, 4, -5, 8, 9, 8, 9, 9],  # 6
               [1, 3, 4, -5, 8, 9, 8, 9, 9],  # 7
               [1, 3, 4, -5, -8, 6, 8, 9, 9]]  # 8
    # dd_list = insert_values_in_2D_list_giving_coordinates(dd_list, [1, 3, 4, 5], [[0, 2], [1, 1], [3, 3], [0, 3]])
    # print(value_appearances_in(dd_list, 'column', 8, 8))

    # print(get_values_in_2D_list(dd_list, 'coordinates', [(0, 0), (0, 3), (2, 2), (8, 4), (6, 1), (4, 4)]))
    # nonet_coordinates = get_nonet_coordinates(5, 3)
    # print('nonet_coords', nonet_coordinates)
    # nonet_len = 3
    # initial_coordinates = nonet_coordinates[0] * nonet_len, nonet_coordinates[1] * nonet_len
    initial_coordinates = 0, 0
    # final_coordinates = (initial_coordinates[0] + nonet_len, initial_coordinates[1] + nonet_len)
    final_coordinates = 0, 3

    print('initial_coords', initial_coordinates)
    print('final_coords', final_coordinates)
    l = [(0, c) for c in range(3)]
    print(l)
    print(_get_2D_list_sublist_coordinates(initial_coordinates, final_coordinates))
