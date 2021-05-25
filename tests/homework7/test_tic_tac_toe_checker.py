import pytest

from homework7.task3.task import tic_tac_toe_checker


class TestTicTacToeChecker:
    @pytest.mark.parametrize(
        "list_input, expected_result",
        [
            ([["-", "-", "o"], ["-", "x", "o"], ["x", "x", "x"]], "x is winner"),
            ([["x", "-", "-"], ["x", "x", "o"], ["x", "o", "-"]], "x is winner"),
            ([["x", "-", "o"], ["x", "x", "o"], ["-", "o", "x"]], "x is winner"),
        ],
    )
    def test_combination_x_win(self, list_input, expected_result):
        """Testing winning combination for x.
        3x horizontally, 3x vertically, 3x diagonally"""
        assert tic_tac_toe_checker(list_input) == expected_result

    @pytest.mark.parametrize(
        "list_input, expected_result",
        [
            ([["o", "-", "o"], ["o", "o", "o"], ["-", "o", "x"]], "o is winner"),
            ([["x", "o", "-"], ["-", "o", "o"], ["x", "o", "x"]], "o is winner"),
            ([["x", "-", "o"], ["x", "o", "o"], ["o", "o", "x"]], "o is winner"),
        ],
    )
    def test_combination_o_win(self, list_input, expected_result):
        """Testing winning combination for o.
        3o horizontally, 3o vertically, 3o diagonally"""
        assert tic_tac_toe_checker(list_input) == expected_result

    def test_draw_combination(self):
        """Testing draw combination, when no cells with '-'"""
        assert (
            tic_tac_toe_checker([["o", "x", "o"], ["x", "o", "x"], ["x", "o", "x"]])
            == "draw!"
        )

    def test_unfinished_combination(self):
        """Testing unfinished combination, when no winner and there are some empty cells"""
        assert (
            tic_tac_toe_checker([["o", "x", "-"], ["x", "o", "-"], ["-", "o", "x"]])
            == "unfinished!"
        )
