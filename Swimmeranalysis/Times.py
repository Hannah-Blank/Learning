FN = "Darius-13-100m-Fly.txt"
FOLDER = "swimdata/"


swimmer, age_group, distance, stroke= FN.removesuffix(".txt").split("-")


with open(FOLDER + FN) as df:
    data= df.readlines()
times = data[0].strip().split(",")


converts = []
for time in times:
    minutes, rest = time.split(":")
    seconds, hundredths = rest.split(".")
    converted_time = int(minutes)*60*100 + int(seconds)*100 + int(hundredths)
    converts.append(converted_time)
    print(time, "->", converted_time)
average_time = sum(converts)/ len(converts)


import statistics

average =statistics.mean(converts)
mins_secs, hundredths= str(round(average/ 100,2)).split(".")
mins_secs = int(mins_secs)
minutes = mins_secs // 60
seconds = mins_secs - minutes*60
average = str(minutes) + ":" + str(seconds) + "." + hundredths

print(f"Average time: {average}", swimmer, age_group, distance, stroke, times )