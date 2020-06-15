from datetime import datetime
from time import sleep
from subprocess import call as send_command


def killing_time_request():
    #killing_time_HH = input("Please enter hour in 24-hour format(HH) >")
    #killing_time_MM = input("Please enter minute in 24-hour format(MM) >")
    confirmation = input(
        "Magic will happen at {0}:{1}, Is that correct? Y/N >".format(killing_time_HH, killing_time_MM)).upper()
    killing_time_RAW = ("{0}:{1}").format(killing_time_HH, killing_time_MM)
    killing_time_HHMM = datetime.strptime(
        killing_time_RAW, "%H:%M")
    if confirmation == "Y":
        print("GOOD!")
        return(killing_time_HHMM).time()
    killing_time_request()


# def kill_all_fun(killing_time):
#     while True:
#         sleep(15)
#         current_time = datetime.now().time()
#         if current_time >= killing_time:
#             print("TIME TO DIE!")
#             send_command('pkill -f Steam', shell=True)
#             exit()