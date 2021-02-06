"""
Skyscrapers game
https://github.com/kkulykk/skyscrapers
"""


def read_input(path: str):
    """
    Read game board file from path.
    Return list of str.

    >>> read_input("check.txt")
    ['***21**', '412453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***']
    """
    file = open(path, 'r')
    result = []
    for line in file.readlines():
        result.append(line.rstrip('\n'))
    return result


def left_to_right_check(input_line: str, pivot: int):
    """
    Check row-wise visibility from left to right.
    Return True if number of building from the left-most hint is visible
    looking to the right,
    False otherwise.

    input_line - representing board row.
    pivot - number on the left-most hint of the input_line.

    >>> left_to_right_check("412453*", 4)
    True
    >>> left_to_right_check("452453*", 5)
    False
    """
    no_hints = input_line[1:-1]
    if len(no_hints) < pivot:
        return False
    counter = 0
    maximum = 0
    for i in no_hints:
        if int(i) > maximum:
            maximum = int(i)
            counter += 1
        if counter == pivot:
            return True
    return False


def check_not_finished_board(board: list):
    """
    Check if skyscraper board is not finished, i.e., '?' present on the game board.

    Return True if finished, False otherwise.

    >>> check_not_finished_board(['***21**', '4?????*', '4?????*', '*?????5',\
         '*?????*', '*?????*', '*2*1***'])
    False
    >>> check_not_finished_board(['***21**', '412453*', '423145*', '*543215',\
         '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_not_finished_board(['***21**', '412453*', '423145*', '*5?3215',\
         '*35214*', '*41532*', '*2*1***'])
    False
    """
    for i in board:
        for k in i:
            if k == "?":
                return False
    return True


def check_uniqueness_in_rows(board: list):
    """
    Check buildings of unique height in each row.

    Return True if buildings in a row have unique length, False otherwise.

    >>> check_uniqueness_in_rows(['***21**', '412453*', '423145*', '*543215',\
         '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_uniqueness_in_rows(['***21**', '452453*', '423145*', '*543215',\
         '*35214*', '*41532*', '*2*1***'])
    False
    >>> check_uniqueness_in_rows(['***21**', '412453*', '423145*', '*553215',\
         '*35214*', '*41532*', '*2*1***'])
    False
    """
    no_vertical_hints = board[1:-1]
    for i in no_vertical_hints:
        no_hints = i[1:-1]
        number = "".join(i for i in no_hints if i in "0123456789")
        if len(number) != len(set(number)):
            return False
    return True


def check_horizontal_visibility(board: list):
    """
    Check row-wise visibility (left-right and vice versa)

    Return True if all horizontal hints are satisfiable,
     i.e., for line 412453* , hint is 4, and 1245 are the four buildings
      that could be observed from the hint looking to the right.

    >>> check_horizontal_visibility(['***21**', '412453*', '423145*',\
         '*543215', '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_horizontal_visibility(['***21**', '452453*', '423145*',\
         '*543215', '*35214*', '*41532*', '*2*1***'])
    False
    >>> check_horizontal_visibility(['***21**', '452413*', '423145*',\
         '*543215', '*35214*', '*41532*', '*2*1***'])
    False
    """
    no_hints_board = board[1:-1]
    for i in no_hints_board:
        hint_1 = i[0]
        if hint_1 != "*" and not left_to_right_check(i, int(i[0])):
            return False
        hint_2 = i[-1]
        if hint_2 != "*" and not left_to_right_check(i[::-1], int(i[-1])):
            return False
    return True


def check_columns(board: list):
    """
    Check column-wise compliance of the board for uniqueness (buildings of
    unique height) and visibility (top-bottom and vice versa).

    Same as for horizontal cases, but aggregated in one function for vertical
    case, i.e. columns.

    >>> check_columns(['***21**', '412453*', '423145*', '*543215', '*35214*',\
         '*41532*', '*2*1***'])
    True
    >>> check_columns(['***21**', '412453*', '423145*', '*543215', '*35214*',\
         '*41232*', '*2*1***'])
    False
    >>> check_columns(['***21**', '412553*', '423145*', '*543215', '*35214*',\
         '*41532*', '*2*1***'])
    False
    """
    columns = []
    length_of_board = len(board)
    for i in range(length_of_board):
        column = ""
        for k in range(length_of_board):
            column += board[k][i]
        columns.append(column)
    return check_uniqueness_in_rows(columns) and check_horizontal_visibility(columns)


def check_skyscrapers(input_path: str):
    """
    Main function to check the status of skyscraper game board.
    Return True if the board status is compliant with the rules,
    False otherwise.

    >>> check_skyscrapers("check.txt")
    True
    """
    board = read_input(input_path)
    return check_not_finished_board(board) and check_uniqueness_in_rows(board)\
        and check_horizontal_visibility(board) and check_columns(board)


if __name__ == "__main__":
    print(check_skyscrapers("check.txt"))
