import random
import island_tiles
import general_map_methods
from enum import Enum


class Left_Tile(Enum):
    water_right = 1
    waterT_sandB_right = 2
    waterB_sandT_right = 3
    sand_right = 4


class Bottom_Tile(Enum):
    water_bottom = 1
    waterL_sandR_bottom = 2
    waterR_sandL_bottom = 3
    sand_bottom = 4


# -------------------
# Tilemap creation methods
# -------------------

# check what type the above tile is


def get_water_tile():
    fly_int = random.randrange(20)
    chosen_water_tile = []

    # get random tile
    key, value = random.choice(list(island_tiles.ywater_top.items()))
    chosen_water_tile.append(value[0])
    chosen_water_tile.append(value[1])

    # fly 1
    fly_1 = []
    fly_1.append(island_tiles.ywater_top["water_s_ysand"][0])
    fly_1.append(island_tiles.ywater_top["water_s_ysand"][1])

    # fly 2
    fly_2 = []
    fly_2.append(island_tiles.ywater_top["water_l_ysand"][0])
    fly_2.append(island_tiles.ywater_top["water_l_ysand"][1])

    if fly_int == 1:
        # fly 1
        return fly_1
    elif fly_int == 2:
        # fly 2
        return fly_2
    else:
        # clean
        while chosen_water_tile == fly_1 or chosen_water_tile == fly_2:
            # get new random tile
            key, value = random.choice(list(island_tiles.ywater_top.items()))
            chosen_water_tile = []
            chosen_water_tile.append(value[0])
            chosen_water_tile.append(value[1])

    return chosen_water_tile


def check_tile_above(top_tile):
    if top_tile in island_tiles.ywater_bottom.values():
        return Bottom_Tile.water_bottom
    elif top_tile in island_tiles.waterL_ysandR_bottom.values():
        return Bottom_Tile.waterL_sandR_bottom
    elif top_tile in island_tiles.waterR_ysandL_bottom.values():
        return Bottom_Tile.waterR_sandL_bottom
    elif top_tile in island_tiles.ysand_bottom.values():
        return Bottom_Tile.sand_bottom


# check what type the left tile is


def check_tile_left(left_tile):
    if left_tile in island_tiles.ywater_right.values():
        return Left_Tile.water_right
    elif left_tile in island_tiles.waterT_ysandB_right.values():
        return Left_Tile.waterT_sandB_right
    elif left_tile in island_tiles.waterB_ysandT_right.values():
        return Left_Tile.waterB_sandT_right
    elif left_tile in island_tiles.ysand_right.values():
        return Left_Tile.sand_right


def get_top(bottom, pos):
    if bottom == Bottom_Tile.water_bottom:
        new_tile = get_water_tile()
        new_tile.insert(0, pos)
        return new_tile
    elif bottom == Bottom_Tile.waterL_sandR_bottom:
        return general_map_methods.get_random_tile(island_tiles.waterL_ysandR_top, pos)
    elif bottom == Bottom_Tile.waterR_sandL_bottom:
        return general_map_methods.get_random_tile(island_tiles.waterR_ysandL_top, pos)
    elif bottom == Bottom_Tile.sand_bottom:
        return general_map_methods.get_random_tile(island_tiles.ysand_top, pos)


def get_left(left, tile):
    tile.pop(0)

    if left == Left_Tile.water_right:
        return tile in island_tiles.ywater_left.values()
    elif left == Left_Tile.waterT_sandB_right:
        return tile in island_tiles.waterT_ysandB_left.values()
    elif left == Left_Tile.waterB_sandT_right:
        return tile in island_tiles.waterB_ysandT_left.values()
    elif left == Left_Tile.sand_right:
        return tile in island_tiles.ysand_left.values()
    return False



# -------------------
# create the tilemap
# -------------------

def create_tile_map(x, y):
    for i in range(y):
        for j in range(x):
            pos = (GD_STEP_SIZE * i) + j
            if i == 0 or pos % GD_STEP_SIZE == 0:
                # get random value from
                tile = general_map_methods.get_random_tile(island_tiles.full_water, pos)

                total_map.append(tile)
            elif i > 0 and j > 0:
                # only check the tile to the left and to the above

                # left tile
                left_tile = []
                left_tile.append(total_map[-1][1])
                left_tile.append(total_map[-1][2])

                # above tile
                above_tile = []
                above_tile.append(total_map[-x][1])
                above_tile.append(total_map[-x][2])

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
                    total_map.append(new_tile)

    return total_map

# separate water from sand tiles
def separate_island(map):
    for i in map:
        tile_to_check = []
        tile_to_check.append(i[1])
        tile_to_check.append(i[2])

        if tile_to_check in island_tiles.most_water.values():
            water_map.append(i[0])
            water_map.append(i[1])
            water_map.append(i[2])
        elif  tile_to_check in island_tiles.fly_water.values():
            fly_map.append(i[0])
            fly_map.append(i[1])
            fly_map.append(i[2])
        else:
            ground_map.append(i[0])
            ground_map.append(i[1])
            ground_map.append(i[2])

    return [ground_map, water_map, fly_map]

# User variables
map_size_x = 35
map_size_y = 35

# Map variables
GD_STEP_SIZE = 65536

# map arrays
total_map = []
water_map = []
fly_map = []
ground_map = []

# execute methods
# total_map = create_tile_map()
# separate_island(total_map)

# print("-------------")
# print("Finished water map start")
# print("-------------")
# print(water_map)
# print("-------------")
# print("Finished water map End")
# print("-------------")
# print("-------------")
# print("Finished fly map start")
# print("-------------")
# print(fly_map)
# print("-------------")
# print("Finished fly map End")
# print("-------------")
# print("-------------")
# print("Finished ground map start")
# print("-------------")
# print(ground_map)
# print("-------------")
# print("Finished ground map End")
# print("-------------")

# ---- How to use ----
# Under user variables, you set the size of the whole map
# Afterwards you don't HAVE TO edit anything, the map should be fine
# However, it's advisable to edit the map in a way that there are more sand tiles
# and less water tiles, because there are going to be places where you can't walk
# but it does look like it.