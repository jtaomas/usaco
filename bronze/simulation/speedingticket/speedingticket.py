with open("speeding.in","r") as f:
    n, m = [int(x) for x in f.readline().split()]
    roads = [[int(num) for num in f.readline().split()] for road in range(n)]
    segments = [[int(num) for num in f.readline().split()] for segment in range(m)]

max_recorded = 0 
i = 0
j = 0

while m != m+1 and n != n+1:
    if remainder > 0:
        j += 1

    elif remainder < 0:
        i += 1

    remainder = roads[i][0] - segments[j][0]
    above = segments[j][1] - roads[i][1] 
    if above > max_recorded:
        max_recorded = above


