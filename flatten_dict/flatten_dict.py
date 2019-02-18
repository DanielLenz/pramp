from collections import deque


def flatten_dictionary_queue(mydict):
    # Init queue
    queue = deque()
    for key, value in mydict.items():
        queue.append({key: value})

    # Init flat dict
    flat_dict = dict()

    while queue:
        item = queue.popleft()
        key = list(item.keys())[0]
        value = item[key]

        if isinstance(value, dict):
            for key_child, value_child in value.items():
                if not key_child:
                    queue.appendleft({key: value_child})
                else:
                    queue.appendleft({".".join([key, key_child]): value_child})

        else:
            flat_dict[key] = value

    return flat_dict


def flatten_dictionary_recursive(mydict):
    dict_flat = dict()
    construct_dict("", mydict, dict_flat)

    return dict_flat


def construct_dict(initial_key, dic, dict_flat):
    for key, value in dic.items():

        # Value is not a dict
        if not isinstance(value, dict):
            # Key is empty
            if (initial_key is None) or (initial_key == ""):
                dict_flat[key] = value
            # Else append key
            else:
                dict_flat[initial_key + "." + key] = value
        # Value is a dict
        else:
            # Key is empty
            if (initial_key is None) or (initial_key == ""):
                construct_dict(key, value, dict_flat)
            else:
                construct_dict(initial_key + "." + key, value, dict_flat)


if __name__ == "__main__":
    test_dict = {
        "Key1": "1",
        "Key2": {"a": "2", "b": "3", "c": {"d": "3", "e": {"": "1"}}},
    }
    print("Input", test_dict)
    print("Output", flatten_dictionary_recursive(test_dict))

