from homework12.task1.task import ColorsEnum, SimplifiedEnum, SizesEnum


class TestEnumClasses:
    def test_colors_enum(self):
        assert ColorsEnum.RED == "RED"

    def test_sizes_enum(self):
        assert SizesEnum.L == "L"
