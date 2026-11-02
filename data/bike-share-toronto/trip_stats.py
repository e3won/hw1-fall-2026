filename = "data/bike-share-toronto/mini-trips4.csv"
infile = open(filename)
header = infile.readline()
durations = []
for line in infile:
    line = line.removesuffix('\n')
    row = line.split(',')
    duration = int(row[0])
    durations.append(duration)
infile.close()

ordered = sorted(durations)
middle2 = ordered[len(ordered)//2]
middle1 = ordered[len(ordered)//2 - 1]
median  = int(middle1 + middle2)/2
print("Trips:", len(durations))
print("Shortest Time:", min(durations))
print("Longest Time:", max(durations))
print("Average Time:", sum(durations)/len(durations))
print("Median Time:", median)
