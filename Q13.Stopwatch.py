"""
@Author: Akshay Palande
@Date: 2022-05-17 07:00:00
@Last Modified by: Akshay palande
@Last Modified time: 2022-05-17 07:00:00
@Title : Program Aim is to Stimulate a Stopwatch. 
"""


"""
    
    13. Simulate Stopwatch Program
a. Desc -> Write a Stopwatch Program for measuring the time that elapses between
the start and end clicks
b. I/P -> Start the Stopwatch and End the Stopwatch
c. Logic -> Measure the elapsed time between start and end
d. O/P -> Print the elapsed time.
    
"""

import time

def time_convert(sec):
  mins = sec // 60
  sec = sec % 60
  hours = mins // 60
  mins = mins % 60
  print("Time Lapsed = {0}:{1}:{2}".format(int(hours),int(mins),sec))

input("Press Enter to start")
start_time = time.time()

input("Press Enter to stop")
end_time = time.time()

time_lapsed = end_time - start_time
time_convert(time_lapsed)
