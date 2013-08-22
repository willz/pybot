
# cast dictionary's value to integer.
# e.x. {'num': '3'} --> {'num': 3}
def int_dict(d):
    for key in d:
        if isinstance(d[key], str) and d[key].isdigit():
            d[key] = int(d[key])

