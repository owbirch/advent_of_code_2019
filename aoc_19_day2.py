#Advent of code 2019: Day 2

f = open("day_2.txt", "r")
program_code = [int(x) for x in f.read().split(',')]

#PART 1
P = program_code.copy()
start_pos = 0
P[1] = 12
P[2] = 2
while start_pos < len(P):
    opcode = P[start_pos]
    int1, int2, int3 = P[start_pos + 1], P[start_pos + 2], P[start_pos + 3]
    if opcode == 1:
        P[int3] = P[int1] + P[int2]
    elif opcode == 2:
        P[int3] = P[int1] * P[int2]
    else:
        assert opcode == 99
        break
    start_pos += 4
    
print(P[0])

#PART 2
for noun in range(100):
    for verb in range(100):
        P = program_code.copy()
        start_pos = 0
        P[1] = noun
        P[2] = verb
        while start_pos < len(P):
            opcode = P[start_pos]
            int1, int2, int3 = P[start_pos + 1], P[start_pos + 2], P[start_pos + 3]
            if opcode == 1:
                P[int3] = P[int1] + P[int2]
            elif opcode == 2:
                P[int3] = P[int1] * P[int2]
            else:
                assert opcode == 99
                break
            start_pos += 4
        if P[0] == 19690720:
            print((100 * noun) + verb)