with open("shell.in","r") as f:
    length, *commands = f.readlines()
    
count = 0
highest = 0

for i in range(0,3):
    count = 0
    shells = [False]*3
    shells[i] = True
    for index, command in enumerate(commands):
        a, b, g = [int(x)-1 for x in command.strip().split()]
        
        temp = shells[a]
        shells[a] = shells[b]
        shells[b] = temp

        if shells[g]:
            count += 1

    if count > highest:
        highest = count

with open("shell.out", "w") as f:
    f.write(str(highest))
 