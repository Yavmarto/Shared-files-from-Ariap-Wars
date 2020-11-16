import random
import lava_tiles
import general_map_methods
import ground_road_grass_tiles
from enum import Enum


class Left_Tile(Enum):
    canyon_right = 1
    canyonT_emptyB_right = 2
    canyonB_emptyT_right = 3
    empty_right = 4


class Bottom_Tile(Enum):
    canyon_bottom = 1
    canyonR_emptyL_bottom = 2
    canyonL_emptyR_bottom = 3
    empty_bottom = 4


# Check the tile above
def check_tile_above(top_tile):
    if top_tile in lava_tiles.black_empty_bottom_canyon.values():
        return Bottom_Tile.empty_bottom
    elif top_tile in lava_tiles.black_ground_bottom_canyon.values():
        return Bottom_Tile.canyon_bottom
    elif top_tile in lava_tiles.blackL_emptyR_bottom_canyon.values():
        return Bottom_Tile.canyonL_emptyR_bottom
    elif top_tile in lava_tiles.blackR_emptyL_bottom_canyon.values():
        return Bottom_Tile.canyonR_emptyL_bottom

# Check the left tile
def check_tile_left(left_tile):
    if left_tile in lava_tiles.black_empty_right_canyon.values():
        return Left_Tile.empty_right
    elif left_tile in lava_tiles.black_ground_right_canyon.values():
        return Left_Tile.canyon_right
    elif left_tile in lava_tiles.blackT_emptyB_right_canyon.values():
        return Left_Tile.canyonT_emptyB_right
    elif left_tile in lava_tiles.blackB_emptyT_right_canyon.values():
        return Left_Tile.canyonB_emptyT_right

# get a tile based on the top 
def get_top(bottom, pos):
    if bottom == Bottom_Tile.empty_bottom:
            return general_map_methods.get_random_tile(lava_tiles.black_empty_top_canyon, pos)
    elif bottom == Bottom_Tile.canyon_bottom:
        return general_map_methods.get_random_tile(lava_tiles.black_ground_top_canyon, pos)
    elif bottom == Bottom_Tile.canyonR_emptyL_bottom:
        return general_map_methods.get_random_tile(lava_tiles.blackR_emptyL_top_canyon, pos)
    elif bottom == Bottom_Tile.canyonL_emptyR_bottom:
        return general_map_methods.get_random_tile(lava_tiles.blackL_emptyR_top_canyon, pos)

# Check whether the left side of the tile fits
def get_left(left, tile):
    if tile == None:
        return False
    tile.pop(0)

    if left == Left_Tile.empty_right:
        return tile in lava_tiles.black_empty_left.values() or tile in lava_tiles.black_empty_left_canyon.values()
    elif left == Left_Tile.canyon_right:
        return tile in lava_tiles.black_ground_left_canyon.values()
    elif left == Left_Tile.canyonB_emptyT_right:
        return tile in lava_tiles.blackB_emptyT_left_canyon.values()
    elif left == Left_Tile.canyonT_emptyB_right:
        return tile in lava_tiles.blackT_emptyB_left_canyon.values()
    return False


# Create the whole tilemap
def create_tile_map(width, height):
    for i in range(height):
        for j in range(width):
            pos = (GD_STEP_SIZE * i) + j
            if i == 0 or pos % GD_STEP_SIZE == 0:
                # get random value from
                tile = general_map_methods.get_random_tile(lava_tiles.black_canyon_border, pos)

                final_map.append(tile)
            elif i > 0 and j > 0:
                # only check the tile to the left and to the above

                # left tile
                left_tile = []
                left_tile.append(final_map[-1][1])
                left_tile.append(final_map[-1][2])

                # above tile
                above_tile = []
                above_tile.append(final_map[-map_size_x][1])
                above_tile.append(final_map[-map_size_x][2])

                success = False

                top = check_tile_above(above_tile)
                left = check_tile_left(left_tile)
                fetched_tile = []

                tries = 0
                while success == False:
                    fetched_tile = get_top(top, pos)
                    if get_left(left, fetched_tile) == True:
                            success = True
                    else:
                        tries += 1

                if success:
                    new_tile = []
                    new_tile.append(pos)
                    new_tile.append(fetched_tile[0])
                    new_tile.append(fetched_tile[1])
                    final_map.append(new_tile)


    return final_map

# Add ground tiles to the empty canyon tiles
def add_ground_tiles(map):
    temp_ground_map = []
    index_to_delete = []
    for i in range(len(map)):
        ground_tile = []
        ground_tile.append(map[i][1])
        ground_tile.append(map[i][2])

        if ground_tile in lava_tiles.black_ground_border_tiles.values():
            ground_tile.insert(0, map[i][0])
            temp_ground_map.append(ground_tile)
            index_to_delete.append(i)
        elif ground_tile in lava_tiles.black_canyon_not_full.values():
            new_tile = [map[i][0]]
            new_tile.append(lava_tiles.black_cave_ground["full_1"][0])
            new_tile.append(lava_tiles.black_cave_ground["full_1"][1])

            temp_ground_map.append(new_tile)

    # Delete tiles that were moved
    index_to_delete.reverse()
    for i in index_to_delete:
        map.pop(i)

    # Convert ground tiles
    for tile in temp_ground_map:
        for i in tile:
            ground_map.append(i)

    # Convert fly tiles
    for tile in map:
        for i in tile:
            fly_map.append(i)

    return [ground_map, fly_map]


# Create lava
def create_lava(height, width, start):
    complete_lava = []
    for i in range(height):
        for j in range(width):
            chosen_lava_tile = []
            pos = (GD_STEP_SIZE * i) + j + (GD_STEP_SIZE * start[1]) + start[0]

            # set overlap tiles
            chosen_lava_tile.append(pos)
            if i == 0 and j == 0:
                # left top tile
                chosen_lava_tile.append(
                    lava_tiles.lava_canyon["rbq"][0])
                chosen_lava_tile.append(
                    lava_tiles.lava_canyon["rbq"][1])
            elif i == height-1 and j == width-1:
                # right bottom tile
                chosen_lava_tile.append(
                    lava_tiles.lava_canyon["ltq"][0])
                chosen_lava_tile.append(
                    lava_tiles.lava_canyon["ltq"][1])
            elif i == height-1 and j == 0:
                # left bottom tile
                chosen_lava_tile.append(
                    lava_tiles.lava_canyon["rtq"][0])
                chosen_lava_tile.append(
                    lava_tiles.lava_canyon["rtq"][1])
            elif i == 0 and j == width-1:
                # right top tile
                chosen_lava_tile.append(
                    lava_tiles.lava_canyon["lbq"][0])
                chosen_lava_tile.append(
                    lava_tiles.lava_canyon["lbq"][1])
            elif i == 0:
                chosen_lava_tile.append(
                    lava_tiles.lava_canyon["bh"][0])
                chosen_lava_tile.append(
                    lava_tiles.lava_canyon["bh"][1])
            elif j == 0:
                chosen_lava_tile.append(
                    lava_tiles.lava_canyon["rh"][0])
                chosen_lava_tile.append(
                    lava_tiles.lava_canyon["rh"][1])
            elif i == height-1:    
                chosen_lava_tile.append(
                    lava_tiles.lava_canyon["th"][0])
                chosen_lava_tile.append(
                    lava_tiles.lava_canyon["th"][1])
            elif j == width-1:
                chosen_lava_tile.append(
                    lava_tiles.lava_canyon["lh"][0])
                chosen_lava_tile.append(
                    lava_tiles.lava_canyon["lh"][1])
                
            else:
                chosen_lava_tile.append(lava_tiles.lava_canyon["full_1"][0])
                chosen_lava_tile.append(lava_tiles.lava_canyon["full_1"][1])

            if len(chosen_lava_tile) > 0:
                for part in chosen_lava_tile:
                    complete_lava.append(part)

    return complete_lava


# Map variables
GD_STEP_SIZE = 65536

# -----------------------
# ---- User Variables----
# -----------------------
map_size_x = 24
map_size_y = 14

lava_y = 3
lava_x = 5
lava_start = [1,1]

# Map variables

final_map = []
converted_map = []

ground_map = []
lava_map = []
fly_map = []

# tilemaps creation
complete_tilemap = create_tile_map(map_size_x, map_size_y)
add_ground_tiles(complete_tilemap)

# Optional
lava_map = create_lava(lava_x, lava_y, lava_start) # goes into impassable


# Optional
print("-------------")
print("lava start")
print("-------------")
print(lava_map)

print("-------------")
print("Ground start")
print("-------------")
print(ground_map)

print("-------------")
print("Fly map End")
print("-------------")
print(fly_map)


# ---- Explanation ----


# General generation will be done like the dark and light caves 
# Lava tiles will not be incorperated in the generation
# instead it will be done like the grass_road generation:
# you insert them and place them in the right position so 
# that you have to fix it afterwards with the incomplete ground tiles

# ---- How to use ----
# Under user variables, you set the size of the whole map
# If you don't use lava, you only need the ground_map and the fly_map
# Comment out Everything optional to print, and all road and water map creation
# and the fusing calls
# Afterwards you don't HAVE TO edit anything, the map should be fine
# However, it's advisable to edit the map in a way that there are more ground tiles
# and less flying tiles.

# Optionally you set the size and starting position of the lava and 
# let the optional things run. After running the program. 
# Copy the arrays to Level Afterwards you need to fix everytime 
# surrounding the lava
