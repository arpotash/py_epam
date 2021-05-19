def instances_counter(cls):
    count = 0

    def __new__(cls):
        nonlocal count
        count += 1
        return super(cls, cls).__new__(cls)

    def get_created_instances(*args, **kwargs):
        return count

    def reset_instances_counter(*args, **kwargs):
        nonlocal count
        try:
            return count
        finally:
            count = 0

    setattr(cls, "get_created_instances", get_created_instances)
    setattr(cls, "__new__", __new__)
    setattr(cls, "reset_instances_counter", reset_instances_counter)
    return cls


@instances_counter
class User:
    pass
