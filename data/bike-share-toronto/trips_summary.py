tripsfile = "data/bike-share-toronto/trips.csv"
infile = open(tripsfile)
header = infile.readline()
durations = []
for line in infile:
    line = line.removesuffix('\n')
    row = line.split(',')
    durations.append(int(row[0]))
infile.close()

Number_of_trips = len(durations)
Shortest_time = min(durations)
Longest_time = max(durations)
Average_time = sum(durations)/len(durations)
Ordered = sorted(durations)

Three_Longest_time = []
for time in Ordered[-3:]:
    Three_Longest_time.append(round(time/60, 1))


print("Trips:", Number_of_trips)
print("Shortest Time (Minutes):", round(int(Shortest_time)/60, 1))
print("Longest Time (Minutes):", round(int(Longest_time)/60, 1))
print("Average Time (Minutes):", round(int(Average_time)/60, 1))
print("Three Longest Times (Minutes):", Three_Longest_time)