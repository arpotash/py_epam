from homework1.task3.task import find_maximum_and_minimum


class TestFindMaxMin:
    def test_find_values(self):
        """Testing that provided that the file exists and there are integers inside function return right answer"""
        test_data = ["1\n", "2\n", "3\n", "4\n", "5\n", "6\n", "7\n"]
        with open("test_file.txt", "w") as f_o:
            f_o.writelines(test_data)
        assert find_maximum_and_minimum("test_file.txt") == (1, 7)
