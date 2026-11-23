from constants.drivers import DRIVERS
import random
from collections import OrderedDict

#Selected options
userDriver: int = None
userTrack: str = None
userDifficulty: str = None

positions = {
        1: {
            "p": "1",
            "team": None,
            "driver": None,
            "time": None,
            "time difference": None,
            "formatted time": None
        },
        2: {
            "p": "2",
            "team": None,
            "driver": None,
            "time": None,
            "time difference": None,
            "formatted time": None
        },
        3: {
            "p": "3",
            "team": None,
            "driver": None,
            "time": None,
            "time difference": None,
            "formatted time": None
        }, 
        4: {
            "p": "4",
            "team": None,
            "driver": None,
            "time": None,
            "time difference": None,
            "formatted time": None
        }, 
        5: {
            "p": "5",
            "team": None,
            "driver": None,
            "time": None,
            "time difference": None,
            "formatted time": None
        },
        6: {
            "p": "6",
            "team": None,
            "driver": None,
            "time": None,
            "time difference": None,
            "formatted time": None
        },
        7: {
            "p": "7",
            "team": None,
            "driver": None,
            "time": None,
            "time difference": None,
            "formatted time": None
        },
        8: {
            "p": "8",
            "team": None,
            "driver": None,
            "time": None,
            "time difference": None,
            "formatted time": None
        },
        9: {
            "p": "9",
            "team": None,
            "driver": None,
            "time": None,
            "time difference": None,
            "formatted time": None
        }, 
        10: {
            "p": "10",
            "team": None,
            "driver": None,
            "time": None,
            "time difference": None,
            "formatted time": None
        },
        11: {
            "p": "11",
            "team": None,
            "driver": None,
            "time": None,
            "time difference": None,
            "formatted time": None
        }, 
        12: {
            "p": "12",
            "team": None,
            "driver": None,
            "time": None,
            "time difference": None,
            "formatted time": None
        },
        13: {
            "p": "13",
            "team": None,
            "driver": None,
            "time": None,
            "time difference": None,
            "formatted time": None
        },
        14: {
            "p": "14",
            "team": None,
            "driver": None,
            "time": None,
            "time difference": None,
            "formatted time": None
        },
        15: {
            "p": "15",
            "team": None,
            "driver": None,
            "time": None,
            "time difference": None,
            "formatted time": None
        },
        16: {
            "p": "16",
            "team": None,
            "driver": None,
            "time": None,
            "time difference": None,
            "formatted time": None
        },
        17: {
            "p": "17",
            "team": None,
            "driver": None,
            "time": None,
            "time difference": None,
            "formatted time": None
        },
        18: {
            "p": "18",
            "team": None,
            "driver": None,
            "time": None,
            "time difference": None,
            "formatted time": None
        }, 
        19: {
            "p": "19",
            "team": None,
            "driver": None,
            "time": None,
            "time difference": None,
            "formatted time": None
        },
        20: {
            "p": "20",
            "team": None,
            "driver": None,
            "time": None,
            "time difference": None,
            "formatted time": None
        },
        21: {
            "p": "21",
            "team": None,
            "driver": None,
            "time": None,
            "time difference": None,
            "formatted time": None
        },
        22: {
            "p": "22",
            "team": None,
            "driver": None,
            "time": None,
            "time difference": None,
            "formatted time": None
        },
    }

#Clears the dictionary to allow restarting the simulation
def clear_positions():
    for place in positions.values():
        place["team"] = None
        place["driver"] = None
        place["time"] = None
        place["time difference"] = None
        place["formatted time"] = None

def clear_selections():
    global userDriver, userTrack, userDifficulty
    userDriver = None
    userTrack = None
    userDifficulty = None

#Placeholder function to generate random quali times to allow front end implementation
def hot_laps():

    #Stores the generated lap times and the corresponding driver
    lapTimes = {}

    #Generates random qualifying times
    for driver in DRIVERS:
        mins = 1
        secs = random.randrange(60)
        ms = random.randrange(1000)
        time = (mins * 60000) + (secs * 1000) + ms
        lapTimes[driver] = time
    
    #Ordering the result pairs in ascending order
    orderedLapTimes = OrderedDict(sorted(lapTimes.items(), key=lambda item: item[1]))

    #Adding each driver and their time, in order, to the position table
    for driver, time in orderedLapTimes.items():
        for results in positions.values():
            if results["time"] is None:
                results["team"] = DRIVERS[driver]["team"]
                results["driver"] = driver
                results["time"] = time
                break
    
    #Working out the formatted times
    for place in positions.values():
        timeLeft = place["time"]

        #Calculating minutes, removing them from the total and making string versions
        mins = timeLeft // 60000
        stringMins = str(mins)
        timeLeft -= (mins * 60000)

        #Calculating seconds, removing them from the total and making string versions
        secs = timeLeft // 1000
        if secs >= 10:
            stringSecs = str(secs)
        else:
            stringSecs = f"0{str(secs)}"
        timeLeft -= (secs * 1000)

        #Calculating milliseconds and making string versions
        ms = timeLeft
        if ms >= 100:
            stringMs = str(ms)
        elif ms >= 10:
            stringMs = f"0{str(ms)}"
        else:
            stringMs = f"00{str(ms)}"
        
        #Saving the formatted time
        place["formatted time"] = f"{stringMins}:{stringSecs}:{stringMs}"
    
    #Recording the position of the user driver
    userDriverPos = None
    for place in positions.values():
        if place["driver"] == userDriver:
            userDriverPos = int(place["p"])
            break

    #Working out the time differences
    for place in positions.values():

        #Time difference not needed for user driver so will display formatted time
        if place["driver"] == userDriver:
            place["time difference"] = place["formatted time"]
            continue
        
        negative = False

        #Calculating the difference between the user driver and other driver
        delta = place["time"] - positions[userDriverPos]["time"]

        #Recording if difference is negative and if so, making iot positive
        if delta < 0:
            negative = True
            delta = abs(delta)

        #Calculating seconds, removing them from the total and making string versions
        secs = delta // 1000
        stringSecs = str(secs)
        delta -= (secs * 1000)

        #Calculating milliseconds and making string versions
        ms = delta
        if ms >= 100:
            stringMs = str(ms)
        elif ms >= 10:
            stringMs = f"0{str(ms)}"
        else:
            stringMs = f"00{str(ms)}"
        
        #Saving the time difference
        if negative is False:
            place["time difference"] = f"+{stringSecs}.{stringMs}"
        else:
            place["time difference"] = f"-{stringSecs}.{stringMs}"