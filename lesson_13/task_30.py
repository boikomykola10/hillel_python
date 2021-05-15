class Counter:
    def __init__(self, current_value, min_value=0, max_value=100):
        self.current_value = current_value
        self.min_value = min_value
        self.max_value = max_value

    def increase(self):
        self.current_value += 1

    def print_value(self):
        print('Текущее значение счетчика: ', self.current_value)


