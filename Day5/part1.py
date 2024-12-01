from sys import argv
chunks = open(argv[1]).read().split('\n\n')
seeds = [int(i) for i in chunks[0].split(': ')[1].split()]

mappings = [[]]
for chunk in chunks[1:]:
    chunkMaps = [[]]
    for map in chunk.split('\n')[1:]:
        map = [int(m) for m in map.split()]
        chunkMaps.append(map)
    mappings.append(chunkMaps[1:])
mappings = mappings[1:]

print(seeds)
for mapping in mappings:
    newSeeds = []

    for map in mapping:
        #print(map)
        #print(map[1], map[1]+map[2])
        for index, seed in enumerate(seeds):
            if seed >= map[1] and seed < (map[1]+map[2]):
                #print(seed, (seed+(map[0]-map[1])))
                #newSeeds.append((index, (seed+(map[0]-map[1]))))
                newSeeds.append((index, (seed-map[1]+map[0])))
                #print(seed, (map[1], map[1]+map[2]), (map[0], map[0]+map[2]), seed-map[1]+map[0])
    for seed in newSeeds:
        seeds[seed[0]] = seed[1]
    print(seeds)
print(min(seeds))



'''
    m = [[int(j) for j in i.split()] for i in chunk.split('\n')[1:]]
    maps += m

print(maps)

#for s in range(len(seeds)):
#    for tS in toSoil:
for mapping in maps:
    for map in mapping:
        for s in range(len(seeds)):
            if (seeds[s] >= map[1]) and (seeds[s] < (map[1] + map[2])):
                seeds[s] -= (map[2] - map[1])
print(seeds)
'''