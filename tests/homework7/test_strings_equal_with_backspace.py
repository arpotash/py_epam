from homework7.task2.task import backspace_compare


class TestStringEqual:
    def test_strings_without_backspace(self):
        """Testing comparison two strings without backspaces"""
        assert not backspace_compare("abc", "bcd")

    def test_strings_first_with_backspace_second_not(self):
        """Testing comparison two strings, the first string has backspace after letter,
        the other doesn't"""
        assert backspace_compare("ab#c", "ac")

    def test_strings_with_backspace(self):
        """Testing comparison two strings, when both strings have a backspace after letter"""
        assert backspace_compare("ab#c", "ac#c")

    def test_strings_start_with_backspace(self):
        """Testing comparison two strings, when the first string starts with backspace"""
        assert backspace_compare("#aca", "aca")

    def test_strings_with_some_backspaces(self):
        """Testing comparison two strings, when both strings have more than one backspace"""
        assert backspace_compare("a##c", "#a#c")
