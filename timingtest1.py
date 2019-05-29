import requests
import time
import csv
import json

# setting amount of tests
count = 0
max_allowed = 10

#setting header
header = ['Time']



#performing speed test
while __name__ == "__main__":
    count += 1
    before = time.time()
    params = {"lat": 40.71, "lon": -74}
    r = requests.get("http://api.open-notify.org/iss-pass.json", params=params)
    timetaken = time.time()-before
    print(timetaken)




    #finishing speed test
    if count == max_allowed:
        print("max reached")
        break

