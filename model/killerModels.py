import time

class ConfirmType:
    def __init__(self, value):
        self.value = value

    def confirm_HHMM(self):
        try:
            time.strptime(self.value, '%H:%M')
            return True
        except ValueError:
            return False