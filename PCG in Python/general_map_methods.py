import random
import ground_road_grass_tiles
# -------------------
# Map fusing and replacing methods
# -------------------

# Fuse 2 maps, in general the road and other tilemap
def fuse_map(target_map, source_map):
    for i in range(len(source_map)):
        if i == 0 or i % 3 == 0:
            for j in range(len(target_map)):
                if (j == 0 or j % 3 == 0) and source_map[i] == target_map[j]:
                    target_map[j] = source_map[i]
                    target_map[j+1] = source_map[i+1]
                    target_map[j+2] = source_map[i+2]

    return target_map

# Remove the position from a lower map if a position exists in a higher map
def replace_pos_dif_lvl(lower_map, upper_map):
    list_to_remove = []

    for i in range(len(upper_map)):
        if i == 0 or i % 3 == 0:
            for j in range(len(lower_map)):
                if (j == 0 or j % 3 == 0) and upper_map[i] == lower_map[j]:
                    list_to_remove.append(j)
    
    list_to_remove.reverse()


    if len(list_to_remove) > 0:
        for i in list_to_remove:
            for j in range(3):
                lower_map.pop(i)

    return lower_map

# Append 2 maps, who don't overlap
def append_maps(target_map, source_map):
    for i in source_map:
        target_map.append(i)

    return target_map


# get a random tile from a given group


def get_random_tile(tile_group, pos):
    key, value = random.choice(list(tile_group.items()))

    test_tile = [pos]
    test_tile.append(value[0])
    test_tile.append(value[1])

    return test_tile

def get_road_tile():

    road_int = random.randrange(15)
    chosen_road_tile = []

    if road_int == 7:
        # crack 1
        chosen_road_tile.append(ground_road_grass_tiles.road_tiles["cracked_road1"][0])
        chosen_road_tile.append(ground_road_grass_tiles.road_tiles["cracked_road1"][1])
    elif road_int == 8:
        # crack 2
        chosen_road_tile.append(ground_road_grass_tiles.road_tiles["cracked_road2"][0])
        chosen_road_tile.append(ground_road_grass_tiles.road_tiles["cracked_road2"][1])
    elif road_int == 9:
        # crack 3
        chosen_road_tile.append(ground_road_grass_tiles.road_tiles["cracked_road3"][0])
        chosen_road_tile.append(ground_road_grass_tiles.road_tiles["cracked_road3"][1])
    else:
        # clean
        chosen_road_tile.append(ground_road_grass_tiles.road_tiles["clean_road"][0])
        chosen_road_tile.append(ground_road_grass_tiles.road_tiles["clean_road"][1])

    return chosen_road_tile