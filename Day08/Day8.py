from itertools import combinations, product



input_file = 'Day08/input.txt'


with open(input_file) as file:
    list_of_list = [[*line] for line in file.read().strip().splitlines()]

size = len(list_of_list)
all_coords = set(product(range(size), repeat=2))
antennas = {}

for y, x in all_coords:
    val = list_of_list[y][x]
    if val != '.':
        antennas.setdefault(val, []).append((y, x))
    

def task_one():
    antinodes = set()
    for coords in antennas.values():
        for a, b in combinations(coords, 2):
            dif_Y = a[0] - b[0]
            dif_X = a[1] - b[1]

            aa = (a[0] + dif_Y, a[1] + dif_X) # Antinode One
            bb = (b[0] - dif_Y, b[1] - dif_X) # Antinode Two

            if aa in all_coords:    # Is it in the Grid?
                antinodes.add(aa)
            if bb in all_coords:
                antinodes.add(bb)

    return len(antinodes)

def task_two():
    antinodes = set()

    for coords in antennas.values():
        for a, b in combinations(coords, 2):
            dif_Y = a[0] - b[0]
            dif_X = a[1] - b[1]
            
            i = 0
            while True:
                aa = (a[0] + dif_Y * i, a[1] + dif_X * i) # All Antinodes in one direction

                if aa in all_coords:    # Is it in the Grid?
                    antinodes.add(aa)
                    i += 1
                else:
                    break

            i = 0
            while True:
                bb = (b[0] - dif_Y * i, b[1] - dif_X * i) # All Antinode in other direction

                if bb in all_coords:    # Is it in the Grid?
                    antinodes.add(bb)
                    i += 1
                else:
                    break

    return len(antinodes)



print(task_one(),' | ',task_two())