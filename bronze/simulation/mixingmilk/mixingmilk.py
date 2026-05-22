with open("mixmilk.in", "r") as f:
    b1, b2, b3 = [[int(x) for x in bucket.strip().split()] for bucket in f.readlines()]

buckets = []

for i in range(1,101):
    if i % 3 == 1:
        buckets = [b1, b2]
    elif i % 3 == 2:
        buckets = [b2, b3]
    else:
        buckets = [b3, b1]

    capacity = buckets[1][0]
    milk = buckets[0][1] + buckets[1][1]
    overflow = milk - capacity 

    if overflow > 0:
        buckets[1][1] = buckets[1][0]
        buckets[0][1] = overflow
    else:  
        buckets[1][1] = milk
        buckets[0][1] = 0


with open("mixmilk.out", "w") as f:
    f.write(f"{b1[1]}\n{b2[1]}\n{b3[1]}")