from typing import List


def check_horizontal_combination(board):
    """
    Function check possible horizontally combination x or o

    :param board: line's sequence of the game board
    :return: tuple (boolean value, winner if boolean value is True)
    """
    result = check_win_x(board) or check_win_o(board)
    return result


def check_vertical_combination(board):
    """
    Function check possible vertically combination x or o

    :param board: line's sequence of the game board
    :return: tuple (boolean value, winner if boolean value is True)
    """
    top, middle, bottom = board
    board = list(zip(top, middle, bottom))
    result = check_win_x(board) or check_win_o(board)
    return result


def check_diagonal_combination(board):
    """
    Function check possible diagonally combination x or o

    :param board: line's sequence of the game board
    :return: tuple (boolean value, winner if boolean value is True)
    """
    length = len(board[0])
    left_diagonal = [board[i][i] for i in range(length)]
    right_diagonal = [board[length - 1 - i][i] for i in range(length - 1, -1, -1)]
    board = [left_diagonal, right_diagonal]
    result = check_win_x(board) or check_win_o(board)
    return result


def check_draw(board):
    """
    Function check possible draw combination

    :param board: line's sequence of the game board
    :return: tuple (boolean value, winner if boolean value is True)
    """
    return list(filter(lambda line: "-" in line, board)) == []


def check_win_x(board):
    """
    Function check possible horizontally winning x

    :param board: line's sequence of the game board
    :return: tuple (boolean value, winner if boolean value is True)
    """
    result = any(map(lambda line: len(set(line)) == 1 and line[0] == "x", board))
    if result:
        return result, "x"
    return False


def check_win_o(board):
    """
    Function check possible horizontally winning o

    :param board: line's sequence of the game board
    :return: boolean value
    """
    result = any(map(lambda line: len(set(line)) == 1 and line[0] == "o", board))
    if result:
        return result, "o"
    return False


def tic_tac_toe_checker(board: List[List]) -> str:
    """
    Function for determining the result of the game
    'tic-tac-toe'

    :param board: line's sequence of the game board
    :return: result message as string
    """
    if check_horizontal_combination(board):
        return f"{check_horizontal_combination(board)[1]} is winner"
    elif check_vertical_combination(board):
        return f"{check_vertical_combination(board)[1]} is winner"
    elif check_diagonal_combination(board):
        return f"{check_diagonal_combination(board)[1]} is winner"
    elif check_draw(board):
        return f"draw!"
    else:
        return f"unfinished!"
