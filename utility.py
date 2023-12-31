def tup_list_to_dict(tup_list):
    result_dict = {}
    for k, v in tup_list:
        result_dict[k] = v
    return result_dict


def is_under_func(pos, points):
    y_val = points.get(pos[0])
    if y_val is None:
        return True
    if pos[1] < y_val:
        return True
    return False
