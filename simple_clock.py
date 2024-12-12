import time

duration = int(input("Duration(in seconds): "))

for i in range(duration, 0, -1):
    seconds = i%60
    minutes = int(i/60)%60
    hours = int(i/3600)

    print(f"\r{hours:02}:{minutes:02}:{seconds:02}", end="")
    time.sleep(1)

