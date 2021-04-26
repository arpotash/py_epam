from homework1.task4.task import check_sum_of_four


def test_positive_calculate_count_tuple_by_4_lists():
    """Testing hom many tuple combinations (i,j,k,l) return
    that a[i]+b[j]+c[k]+d[l] == 0
    """
    assert check_sum_of_four([1, 2], [-2, -1], [-1, 2], [0, 2]) == 2


def test_negative_calculate_count_tuple_by_4_lists():
    """Testing hom many tuple combinations (i,j,k,l) return
        that a[i]+b[j]+c[k]+d[l] == 0 (negative case)
    """
    assert not check_sum_of_four([1, -2], [2, -1], [1, 2], [-4, 1]) == 3
