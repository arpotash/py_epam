from homework12.task1.task import ColorsEnum, SizesEnum


class TestEnumClasses:
    def test_colors_enum(self):
        """
        Testing that
        """
        assert ColorsEnum.RED == "RED"

    def test_sizes_enum(self):
        assert SizesEnum.L == "L"
