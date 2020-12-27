class Key:
    def __init__(self):
        pass

    def create_dict(self, key, x_position, y_position):
        return {
            "key": key,
            "x_position": x_position,
            "y_position": y_position
        }

    def check_key_press(self, key, value, key_arr):
        return value == key

    def set_key_value(self, key, value, input_data, key_arr):
        index = len(key_arr) - 1
        for dictionary in key_arr:
            if key in dictionary:
                index = key_arr.index(dictionary)
        x_position = key_arr[index]["x_position"]
        y_position = key_arr[index]["y_position"]
        input_data.set_input(x_position, y_position, value)
