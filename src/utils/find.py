def find(list, property, value):
    for item in list:
        if item[property] == value:
            return item
    return None
