# Boxenstopp-Zähler mit einer while-Schleife

fahrer = input("Gib den Namen des Fahrers ein: ")
pitstops = 0
while pitstops < 6:
    runde = input(f"In welcher Runde hat {fahrer} gestoppt? (Oder 'stop' zum Beenden):")
    if runde == 'stop':
        break 
    pitstops += 1

print(f"{fahrer} hat {pitstops} Mal gestoppt, und zwar in den Runden: {runde}.")