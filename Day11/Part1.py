from sys import argv
stones = [int(s) for s in open(argv[1], 'r').read().split()]

def blink(stones):
    inserts = []
    for i, stone in enumerate(stones):
        if stone == 0:
            stones[i] = 1
            continue
        s = list(str(stone))
        if len(s) % 2 == 0:
            new = s[:int(len(s)/2)]
            stone = s[int(len(s)/2):]
            new = int(''.join(new))
            stone = int(''.join(stone))
            stones[i] = stone
            inserts.append((i, new))
            continue
        stones[i] *= 2024
    for stone in reversed(inserts):
        stones.insert(*stone)

#print(stones)
for i in range(25):
    blink(stones)
    #print()
    #print(f"After {i} blinks:")
    #print(stones)
print(len(stones))