with open("speeding.in","r") as f:
    n, m = [int(x) for x in f.readline().split()]
    roads = [f.readline().split() for road in range(n)]
    segments = [f.readline().split() for segment in range(m)]

max_recorded = 0 

print(roads, journeys)