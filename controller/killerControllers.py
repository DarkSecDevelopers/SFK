from datetime import datetime
from subprocess import call
from time import sleep
from model.killerModels import ConfirmType

class ProcessKiller:
    def __init__(self, kill_time, target):
        self.kill_time = kill_time
        self.current_time = datetime.now().time()
        self.target = target

    def kill_all_fun(self):
        if ConfirmType.confirm_HHMM(self.kill_time):
            while True:
                sleep(15)
                if self.current_time >= self.kill_time:
                    print("Here i am, killing again...")
                    call(['pkill', '-f', '{}'.format(self.target)])
                    break
