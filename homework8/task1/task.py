import string


class KeyValueStorage:
    def __init__(self, file_name):
        try:
            self.content = open(file_name)
        except OSError as f:
            raise FileExistsError("ERROR:", f)
        self.attr_dict_from_file = self.get_attribute_from_file()

    def get_attribute_from_file(self):
        dict_attr_from_file = {}
        for line in self.content.readlines():
            key, value = line.rstrip().split("=")
            dict_attr_from_file[key] = value
        return dict_attr_from_file

    def __getitem__(self, item):
        if item not in self.attr_dict_from_file:
            raise KeyError("Wrong key")
        return self.attr_dict_from_file[item]

    def __getattr__(self, item):
        try:
            setattr(self, self.attr_dict_from_file[item], item)
            return self.attr_dict_from_file[item]
        except KeyError:
            raise AttributeError(item)

    def __del__(self):
        self.content.close()
