with open("mixmilk.in", "r") as f:
    b1, b2, b3 = [tuple(int(x) for x in bucket.strip().split()) for bucket in f.readlines()]

buckets = ()

for i in range(1,100):
    if i % 3 == 0:
        buckets = [b3, b1]
    if i % 2 == 0:
        buckets = [b2, b3]
    else:
        buckets = [b1, b2]

    total = buckets[0][1] + buckets[1][1]
    overflow = total - buckets[1][0] 

    if (overflow) >= 0:
        buckets[0] = [overflow, buckets[0][0]]
        buckets[1] = [buckets[1][1], buckets[1][0]]
    else:
        buckets[0] = [0, buckets[0][0]]
        buckets[1] = [total, buckets[1][0]]

with open("mixmilk.out", "w") as f:
    f.write(f"{b1}, {b2}, {b3}")