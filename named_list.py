class named_list(list):
    def __getitem__(self, key):
        return next(item for item in self if item.name == key)

    
