import statistics 
FOLDER = "Swimmeranalysis/swimdata/"

def get_swim_data(fn):
    #Given the name of a swimmer's file, extract all the required data, then return it to the caller as a tuple.
    swimmer, age_group, distance, stroke= fn.removesuffix(".txt").split("-")

    print(f"Swimmer: {swimmer}")
    print(f"Age group: Under {age_group}")
    print(f"Distance: {distance}")
    print(f"Stroke: {stroke}")


    with open(FOLDER + fn) as df:
        data = df.readlines()
    times = data[0].strip().split(",")

    #Converts the times to hundredths of seconds
    converts = []
    for time in times:
        if time > "59.99":
            minutes, rest = time.split(":")
            seconds, hundredths = rest.split(".")
            converted_time = int(minutes)*60*100 + int(seconds)*100 + int(hundredths)
            converts.append(converted_time)
            print(time, "->", converted_time)
        else: 
            seconds, hundredths = time.split(".")
            converted_time = int(seconds)*100 + int(hundredths)
            converts.append(converted_time)
            print(time, "->", converted_time)
   
    #Calculate the average time and convert it back to minutes, seconds, and hundredths of seconds
    
    average =statistics.mean(converts)
    mins_secs, hundredths= str(round(average/ 100,2)).split(".")
    mins_secs = int(mins_secs)
    minutes = mins_secs // 60
    seconds = mins_secs - minutes*60
    average = str(minutes) + ":" + str(seconds) + "." + hundredths
    print(f"Average time: {average}")

print(get_swim_data("Abi-10-50m-Back.txt"))