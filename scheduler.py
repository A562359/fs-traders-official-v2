import schedule
import time
import os

def run_script():
    os.system("python fo_live_feed.py")

schedule.every(3).minutes.do(run_script)

while True:
    schedule.run_pending()
    time.sleep(1)
