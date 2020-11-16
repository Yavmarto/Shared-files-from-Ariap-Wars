import random
import cave_tiles
import general_map_methods
import ground_road_grass_tiles
from enum import Enum


class Left_Tile(Enum):
    canyon_right = 1
    canyonT_emptyB_right = 2
    canyonB_emptyT_right = 3
    empty_right = 4
    # ground_right = 5
    # groundT_emptyB_right = 6
    # groundB_emptyT_right = 7


class Bottom_Tile(Enum):
    canyon_bottom = 1
    canyonR_emptyL_bottom = 2
    canyonL_emptyR_bottom = 3
    empty_bottom = 4
    # ground_bottom = 5
    # groundR_emptyL_bottom = 6
    # groundL_emptyR_bottom = 7

# Check the tile above
def check_tile_above(top_tile):
    if top_tile in cave_tiles.dark_empty_bottom_canyon.values():
        return Bottom_Tile.empty_bottom
    # elif top_tile in cave_tiles.dark_ground_bottom.values():
    #     return Bottom_Tile.ground_bottom
    elif top_tile in cave_tiles.dark_ground_bottom_canyon.values():
        return Bottom_Tile.canyon_bottom
    # elif top_tile in cave_tiles.darkL_emptyR_bottom.values():
    #     return Bottom_Tile.groundL_emptyR_bottom
    elif top_tile in cave_tiles.darkL_emptyR_bottom_canyon.values():
        return Bottom_Tile.canyonL_emptyR_bottom
    # elif top_tile in cave_tiles.darkR_emptyL_bottom.values():
    #     return Bottom_Tile.groundR_emptyL_bottom
    elif top_tile in cave_tiles.darkR_emptyL_bottom_canyon.values():
        return Bottom_Tile.canyonR_emptyL_bottom

# Check the left tile
def check_tile_left(left_tile):
    if left_tile in cave_tiles.dark_empty_right_canyon.values():
        return Left_Tile.empty_right
    # elif left_tile in cave_tiles.dark_ground_right.values():
    #     return Left_Tile.ground_right
    elif left_tile in cave_tiles.dark_ground_right_canyon.values():
        return Left_Tile.canyon_right
    # elif left_tile in cave_tiles.darkT_emptyB_right.values():
    #     return Left_Tile.groundT_emptyB_right
    elif left_tile in cave_tiles.darkT_emptyB_right_canyon.values():
        return Left_Tile.canyonT_emptyB_right
    # elif left_tile in cave_tiles.darkB_emptyT_right.values():
    #     return Left_Tile.groundB_emptyT_right
    elif left_tile in cave_tiles.darkB_emptyT_right_canyon.values():
        return Left_Tile.canyonB_emptyT_right

# get a tile based on the top 
def get_top(bottom, pos):
    if bottom == Bottom_Tile.empty_bottom:
            return general_map_methods.get_random_tile(cave_tiles.dark_empty_top_canyon, pos)
    # elif bottom == Bottom_Tile.ground_bottom:
    #     return get_random_tile(cave_tiles.dark_ground_top, pos)
    # elif bottom == Bottom_Tile.groundR_emptyL_bottom:
    #     return get_random_tile(cave_tiles.darkR_emptyL_top, pos)
    # elif bottom == Bottom_Tile.groundL_emptyR_bottom:
    #     return get_random_tile(cave_tiles.darkL_emptyR_top, pos)
    elif bottom == Bottom_Tile.canyon_bottom:
        return general_map_methods.get_random_tile(cave_tiles.dark_ground_top_canyon, pos)
    elif bottom == Bottom_Tile.canyonR_emptyL_bottom:
        return general_map_methods.get_random_tile(cave_tiles.darkR_emptyL_top_canyon, pos)
    elif bottom == Bottom_Tile.canyonL_emptyR_bottom:
        return general_map_methods.get_random_tile(cave_tiles.darkL_emptyR_top_canyon, pos)

# Check whether the left side of the tile fits
def get_left(left, tile):
    if tile == None:
        return False
    tile.pop(0)

    if left == Left_Tile.empty_right:
        return tile in cave_tiles.dark_empty_left.values() or tile in cave_tiles.dark_empty_left_canyon.values()
    # elif left == Left_Tile.ground_right:
    #     return tile in cave_tiles.dark_ground_left.values()
    # elif left == Left_Tile.groundB_emptyT_right:
    #     return tile in cave_tiles.darkB_emptyT_left.values()
    # elif left == Left_Tile.groundT_emptyB_right:
    #     return tile in cave_tiles.darkT_emptyB_left.values()
    elif left == Left_Tile.canyon_right:
        return tile in cave_tiles.dark_ground_left_canyon.values()
    elif left == Left_Tile.canyonB_emptyT_right:
        return tile in cave_tiles.darkB_emptyT_left_canyon.values()
    elif left == Left_Tile.canyonT_emptyB_right:
        return tile in cave_tiles.darkT_emptyB_left_canyon.values()
    return False


# Create the whole tilemap
def create_tile_map():
    for i in range(map_size_y):
        for j in range(map_size_x):
            pos = (GD_STEP_SIZE * i) + j
            if i == 0 or pos % GD_STEP_SIZE == 0:
                # get random value from
                tile = general_map_methods.get_random_tile(cave_tiles.dark_canyon_border, pos)

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

        if ground_tile in cave_tiles.dark_ground_border_tiles.values():
            ground_tile.insert(0, map[i][0])
            temp_ground_map.append(ground_tile)
            index_to_delete.append(i)
        elif ground_tile in cave_tiles.dark_canyon_not_full.values():
            new_tile = [map[i][0]]
            new_tile.append(cave_tiles.dark_cave_ground["full_1"][0])
            new_tile.append(cave_tiles.dark_cave_ground["full_1"][1])

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


# Create a water
def create_water(height, width, start):
    complete_water = []
    for i in range(height):
        for j in range(width):
            pos = (GD_STEP_SIZE * i) + j + (GD_STEP_SIZE * start[1]) + start[0]
            new_tile = general_map_methods.get_random_tile(ground_road_grass_tiles.full_water, pos)

            if i == 0 or j == 0 or i == height-1 or j == width-1:
                ground_water.append(new_tile[0])
                ground_water.append(new_tile[1])
                ground_water.append(new_tile[2])
            else:
                complete_water.append(new_tile[0])
                complete_water.append(new_tile[1])
                complete_water.append(new_tile[2])

    return [complete_water,ground_water]

# returns a random road tile


def get_road_tile():

    road_int = random.randrange(10)
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

# Create a single road
def create_road(height, width, start):
    complete_road = []
    for i in range(height):
        for j in range(width):
            pos = (GD_STEP_SIZE * i) + j + (GD_STEP_SIZE * start[1]) + start[0]
            new_tile = get_road_tile()
            complete_road.append(pos)
            complete_road.append(new_tile[0])
            complete_road.append(new_tile[1])

    return complete_road

# Create grass overlap between road and grass
def overlap_creation(height, width, start):
    overlap = []
    for i in range(height):
        for j in range(width):
            pos = (GD_STEP_SIZE * i) + j + (GD_STEP_SIZE * start[1]) + start[0]

            # set overlap tiles
            chosen_overlap_tile = []
            if i == 0 and j == 0:
                # left top tile
                chosen_overlap_tile = []
                chosen_overlap_tile.append(
                    cave_tiles.dark_cave_ground["lt"][0])
                chosen_overlap_tile.append(
                    cave_tiles.dark_cave_ground["lt"][1])
            elif i == height-1 and j == width-1:
                # right bottom tile
                chosen_overlap_tile = []
                chosen_overlap_tile.append(
                    cave_tiles.dark_cave_ground["rb"][0])
                chosen_overlap_tile.append(
                    cave_tiles.dark_cave_ground["rb"][1])
            elif i == height-1 and j == 0:
                # left bottom tile
                chosen_overlap_tile = []
                chosen_overlap_tile.append(
                    cave_tiles.dark_cave_ground["lb"][0])
                chosen_overlap_tile.append(
                    cave_tiles.dark_cave_ground["lb"][1])
            elif i == 0 and j == width-1:
                # right top tile
                chosen_overlap_tile = []
                chosen_overlap_tile.append(
                    cave_tiles.dark_cave_ground["rt"][0])
                chosen_overlap_tile.append(
                    cave_tiles.dark_cave_ground["rt"][1])
            elif i == 0:
                chosen_overlap_tile = []
                chosen_overlap_tile.append(
                    cave_tiles.dark_cave_ground["th"][0])
                chosen_overlap_tile.append(
                    cave_tiles.dark_cave_ground["th"][1])
            elif j == 0:
                chosen_overlap_tile = []
                chosen_overlap_tile.append(
                    cave_tiles.dark_cave_ground["lh"][0])
                chosen_overlap_tile.append(
                    cave_tiles.dark_cave_ground["lh"][1])
            elif i == height-1:
                chosen_overlap_tile = []
                chosen_overlap_tile.append(
                    cave_tiles.dark_cave_ground["bh"][0])
                chosen_overlap_tile.append(
                    cave_tiles.dark_cave_ground["bh"][1])
            elif j == width-1:
                chosen_overlap_tile = []
                chosen_overlap_tile.append(
                    cave_tiles.dark_cave_ground["rh"][0])
                chosen_overlap_tile.append(
                    cave_tiles.dark_cave_ground["rh"][1])

            if len(chosen_overlap_tile) > 0:
                overlap.append(pos)
                overlap.append(chosen_overlap_tile[0])
                overlap.append(chosen_overlap_tile[1])

    return overlap

# Map variables
GD_STEP_SIZE = 65536

# -----------------------
# ---- User Variables----
# -----------------------
map_size_x = 27
map_size_y = 20

hori_roads_y = 3
hori_roads_x = 18
hori_roads_start = [5, 10]

water_y = 3
water_x = 18
water_start = [0,0]

# Map variables

final_map = []
converted_map = []

ground_map = []
ground_water = [] # Merges with ground_map, Optional
water_map = []
fly_map = []

# tilemaps creation
# complete_tilemap = create_tile_map()
# add_ground_tiles(complete_tilemap)

# # Optional
# road_map = create_road(hori_roads_x, hori_roads_y, hori_roads_start) # merges into ground
# road_overlap = overlap_creation(hori_roads_x, hori_roads_y, hori_roads_start) # merges into ground extra
# water_map = create_water(water_x, water_y, water_start) # goes into water
# water_overlap = overlap_creation(hori_roads_x, hori_roads_y, water_start) # merges into ground extra

# ground_map_fused = general_map_methods.fuse_map(ground_map, ground_water) # merges into ground
# ground_map_fused2 = general_map_methods.fuse_map(ground_map_fused, road_map) # Goes into ground
# ground_extra_map_fused = general_map_methods.append_maps(road_overlap, water_overlap) # Goes into ground extra


# # Optional
# print("-------------")
# print("Ground fused start")
# print("-------------")
# print(ground_map_fused2)
# print("-------------")
# print("Ground extra End")
# print("-------------")
# print(ground_extra_map_fused)
# print("-------------")
# print("Water start")
# print("-------------")
# print(water_map)

# print("-------------")
# print("Ground start")
# print("-------------")
# print(ground_map)

# print("-------------")
# print("Fly map End")
# print("-------------")
# print(fly_map)


# ---- Explanation ----

# If the tile has half or more canyon, it's flying
# all ground tiles are walkable, unless it's paired with an above tile
# Water tiles paired with ground tiles, are placed on the ground level, 
# the ground tiles is placed on the ground extra level
# 
# water tiles will not be incorperated in the generation
# instead it will be done like the grass_road generation:
# you insert them and place them in the right position so 
# that you have to fix it afterwards with the incomplete ground tiles

# ---- How to use ----
# Under user variables, you set the size of the whole map
# If you don't use water and road, you only need the ground_map and the fly_map
# Comment out Everything optional to print, and all road and water map creation
# and the fusing calls
# Afterwards you don't HAVE TO edit anything, the map should be fine
# However, it's advisable to edit the map in a way that there are more ground tiles
# and less flying tiles. Naturally you can add water and other things if you want to

# Optionally you set the size of the road and water
# This case you comment out the ground map printing, the rest is used
# (unless you only use road or only water, then you need to comment out the correct lines)
# After running the program, Copy the arrays to Level
# Afterwards there are going to be holes (because of the generation methods and overlap)
# This means that there can be empty holes in your road or water.
# Now you have to fix this however you like
