from homework9.task2.task import Suppressor, suppressor


class TestClassSuppressException:
    def test_context_manager_without_error(self):
        """Testing that class context manager returns result"""
        with Suppressor(Exception):
            result = []
            assert result == []

    def test_context_manager_with_error(self):
        """Testing that class context manager suppresses passed error"""
        with Suppressor(IndexError):
            result = [][2]
            assert result


class TestGeneratorSuppressException:
    def test_context_manager_without_error(self):
        """Testing that function context manager returns result"""
        with suppressor(Exception):
            result = []
            assert result == []

    def test_context_manager_with_error(self):
        """Testing that function
        context manager suppresses passed error"""
        with suppressor(NameError):
            print(a)
            assert True
