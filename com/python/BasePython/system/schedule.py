import time
import os
import sched
schedule = sched.scheduler(time.time,time.sleep)
def execute_task(cmd, inc):
    os.system(cmd)
    schedule.enter(inc, 0., execute_task, (cmd, inc))
def main(cmd, inc=60):
    schedule.enter(0, 0, execute_task, (cmd, inc))
    schedule.run()
main("dir",60)