from homework6.task2.task import User, instances_counter


class TestDecoratorAddMethods:
    def test_get_count_instances(self):
        """Testing that the decorator add the method get_created_instances
        which can be called and will return count of the class instances"""
        decorated_class = instances_counter(User)
        assert User.get_created_instances() == 0
        user, _ = User(), User()
        assert User.get_created_instances() == 2

    def test_reset_count_instances(self):
        """Testing that the decorator add the method reset_instances_counter
        which can be called and will return count of the class instances after that
        set to zero count"""
        decorated_class = instances_counter(User)
        user, _ = User(), User()
        assert User.get_created_instances() == 2
        assert User.reset_instances_counter() == 2
        assert User.get_created_instances() == 0
