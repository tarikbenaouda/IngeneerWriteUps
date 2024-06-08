def fight(survivorCounts, positions , i1,i2):
    if i1 == i2:
        print("Invalid fight")
        raise ValueError
    if survivorCounts[i1] > survivorCounts[i2]:
        survivorCounts[i1] = survivorCounts[i1] // 2
        survivorCounts[i2] = 0
    elif survivorCounts[i1] < survivorCounts[i2]:
        survivorCounts[i2] = survivorCounts[i2] // 2
        survivorCounts[i1] = 0
    else:
        if positions[i1] < positions[i2]:
            survivorCounts[i2] = survivorCounts[i2] // 2
            survivorCounts[i1] = 0
        elif positions[i1] > positions[i2]:
            survivorCounts[i1] = survivorCounts[i1] // 2
            survivorCounts[i2] = 0
    return True
def done(survivorCounts, directions):
    dir = 1
    for i in range(len(survivorCounts)):
        if survivorCounts[i] > 0 :
            dir = directions[i]
    for i in range(len(survivorCounts)):
        if survivorCounts[i] > 0 and directions[i] != dir:
            return False
    return True
    
def formation(survivorCounts, positions, directions):
    survivorCounts_map = {}
    for index, value in enumerate(survivorCounts):
        survivorCounts_map[index] = value
    positions_map = {}
    for index, value in enumerate(positions):
        positions_map[index] = value
    directions_map = {}
    for index, value in enumerate(directions):
        directions_map[index] = value
    sorted_direction_zero = sorted([key for key in directions_map if directions_map[key] == 0])
    sorted_direction_one = sorted([key for key in directions_map if directions_map[key] == 1])
    
    
    


survivorCounts = [321, 97, 71, 442, 116, 362, 391, 55, 474, 298]
positions = [7, 1, 3, 4, 2, 9, 8, 0, 6, 5]
directions = [1, 1, 1, 1, 1, 1, 1, 1, 1, 0]
formation(survivorCounts, positions, directions)