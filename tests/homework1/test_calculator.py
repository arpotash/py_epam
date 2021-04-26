from homework1.sample_project.calculator.calc import check_power_of_2


def test_positive_case():
    """Testing that actual powers of 2 give True"""
    assert check_power_of_2(128)


def test_negative_case():
    """Testing that positive non-powers of 2 value give False"""
    assert not check_power_of_2(0)


def test_with_negative_value():
    """Testing that negative value give False"""
    assert not check_power_of_2(-2)
