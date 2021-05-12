import utime

class PlankState:
    def __init__(self):
        self.left_state = False
        self.right_state = False
        self.current_time = utime.ticks_ms()

    def set_state(self, state, position):
        if position == "left":
            self.left_state = state
        if position == "right":
            self.right_state = state

    def get_state(self):
        if self.left_state and self.right_state:
            diff =\
            utime.ticks_diff(utime.ticks_ms(), self.current_time)
            if diff > 3000:
                return "green"
            elif diff > 1000:
                return "yellow"
            else:
                return "blue"
        self.current_time = utime.ticks_ms()
        if self.left_state or self.right_state:
            return "red"
        return "blank"




