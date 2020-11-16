import random
import general_map_methods
import ground_road_grass_tiles
from enum import Enum

# Enums

class Left_Tile(Enum):
    grass_right = 1
    grassT_sandB_right = 2
    grassB_sandT_right = 3
    sand_right = 4
    grassT_waterB_right = 5
    grassB_waterT_right = 6
    water_right = 7

class Bottom_Tile(Enum):
    grass_bottom = 1
    grassL_sandR_bottom = 2
    grassR_sandL_bottom = 3
    sand_bottom = 4
    grassL_waterR_bottom = 5
    grassR_waterL_bottom = 6
    water_bottom = 7


# -------------------
# Tilemap creation methods
# -------------------

# check what type the above tile is


def check_tile_above(top_tile):
    if top_tile in ground_road_grass_tiles.grass_bottom.values():
        return Bottom_Tile.grass_bottom
    elif top_tile in ground_road_grass_tiles.grassL_sandR_bottom.values():
        return Bottom_Tile.grassL_sandR_bottom
    elif top_tile in ground_road_grass_tiles.grassR_sandL_bottom.values():
        return Bottom_Tile.grassR_sandL_bottom
    elif top_tile in ground_road_grass_tiles.sand_bottom.values():
        return Bottom_Tile.sand_bottom
    else:
        return 0

# check what type the left tile is


def check_tile_left(left_tile):
    if left_tile in ground_road_grass_tiles.grass_right.values():
        return Left_Tile.grass_right
    elif left_tile in ground_road_grass_tiles.grassT_sandB_right.values():
        return Left_Tile.grassT_sandB_right
    elif left_tile in ground_road_grass_tiles.grassB_sandT_right.values():
        return Left_Tile.grassB_sandT_right
    elif left_tile in ground_road_grass_tiles.sand_right.values():
        return Left_Tile.sand_right
    else:
        return 0

# get a tile that matches the tile above


def get_top(bottom, pos):
    if bottom == Bottom_Tile.grass_bottom:
        return general_map_methods.get_random_tile(ground_road_grass_tiles.grass_top, pos)
    elif bottom == Bottom_Tile.grassL_sandR_bottom:
        return general_map_methods.get_random_tile(ground_road_grass_tiles.grassL_sandR_top, pos)
    elif bottom == Bottom_Tile.grassR_sandL_bottom:
        return general_map_methods.get_random_tile(ground_road_grass_tiles.grassR_sandL_top, pos)
    elif bottom == Bottom_Tile.sand_bottom:
        return general_map_methods.get_random_tile(ground_road_grass_tiles.sand_top, pos)

# check if the fetched tile matches the tile to the left


def get_left(left, tile):
    tile.pop(0)

    if left == Left_Tile.grass_right:
        return tile in ground_road_grass_tiles.grass_left.values()
    elif left == Left_Tile.grassT_sandB_right:
        return tile in ground_road_grass_tiles.grassT_sandB_left.values()
    elif left == Left_Tile.grassB_sandT_right:
        return tile in ground_road_grass_tiles.grassB_sandT_left.values()
    elif left == Left_Tile.sand_right:
        return tile in ground_road_grass_tiles.sand_left.values()
    return False



# -------------------
# create the tilemap
# -------------------


def create_tile_map(x, y):
    sub_map = []
    for i in range(y):
        for j in range(x):
            pos = (GD_STEP_SIZE * i) + j
            if i == 0 or pos % GD_STEP_SIZE == 0:
                # get random value from
                tile = general_map_methods.get_random_tile(ground_road_grass_tiles.border_tiles, pos)

                sub_map.append(tile)
            elif i > 0 and j > 0:
                # only check the tile to the left and to the above

                # left tile
                left_tile = []
                left_tile.append(sub_map[-1][1])
                left_tile.append(sub_map[-1][2])

                # above tile
                above_tile = []
                above_tile.append(sub_map[-x][1])
                above_tile.append(sub_map[-x][2])

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
                    sub_map.append(new_tile)
    converted_map = []
    for tile in sub_map:
        for part in tile:
            converted_map.append(part)

    return converted_map

# -------------------
# Road creation methods
# -------------------

# Road variables

# -------------------
# User Variables
# -------------------



# returns a random road tile




# Create a single road
def create_road(height, width, start):
    complete_road = []
    for i in range(height):
        for j in range(width):
            pos = (GD_STEP_SIZE * i) + j + (GD_STEP_SIZE * start[1]) + start[0]
            new_tile = general_map_methods.get_road_tile()
            complete_road.append(pos)
            complete_road.append(new_tile[0])
            complete_road.append(new_tile[1])

    return complete_road

# Create grass overlap between road and grass
def road_overlap_creation(height, width, start):
    grass_on_top = []
    for i in range(height):
        for j in range(width):
            pos = (GD_STEP_SIZE * i) + j + (GD_STEP_SIZE * start[1]) + start[0]

            # set overlap tiles
            chosen_overlap_tile = []
            if i == 0 and j == 0:
                # left top tile
                chosen_overlap_tile = []
                chosen_overlap_tile.append(
                    ground_road_grass_tiles.overlap_tile_grass["left_top"][0])
                chosen_overlap_tile.append(
                    ground_road_grass_tiles.overlap_tile_grass["left_top"][1])
            elif i == height-1 and j == width-1:
                # right bottom tile
                chosen_overlap_tile = []
                chosen_overlap_tile.append(
                    ground_road_grass_tiles.overlap_tile_grass["right_bottom"][0])
                chosen_overlap_tile.append(
                    ground_road_grass_tiles.overlap_tile_grass["right_bottom"][1])
            elif i == height-1 and j == 0:
                # left bottom tile
                chosen_overlap_tile = []
                chosen_overlap_tile.append(
                    ground_road_grass_tiles.overlap_tile_grass["left_bottom"][0])
                chosen_overlap_tile.append(
                    ground_road_grass_tiles.overlap_tile_grass["left_bottom"][1])
            elif i == 0 and j == width-1:
                # right top tile
                chosen_overlap_tile = []
                chosen_overlap_tile.append(
                    ground_road_grass_tiles.overlap_tile_grass["right_top"][0])
                chosen_overlap_tile.append(
                    ground_road_grass_tiles.overlap_tile_grass["right_top"][1])
            elif i == 0:
                chosen_overlap_tile = []
                chosen_overlap_tile.append(
                    ground_road_grass_tiles.overlap_tile_grass["top_half"][0])
                chosen_overlap_tile.append(
                    ground_road_grass_tiles.overlap_tile_grass["top_half"][1])
            elif j == 0:
                chosen_overlap_tile = []
                chosen_overlap_tile.append(
                    ground_road_grass_tiles.overlap_tile_grass["left_half"][0])
                chosen_overlap_tile.append(
                    ground_road_grass_tiles.overlap_tile_grass["left_half"][1])
            elif i == height-1:
                chosen_overlap_tile = []
                chosen_overlap_tile.append(
                    ground_road_grass_tiles.overlap_tile_grass["bottom_half"][0])
                chosen_overlap_tile.append(
                    ground_road_grass_tiles.overlap_tile_grass["bottom_half"][1])
            elif j == width-1:
                chosen_overlap_tile = []
                chosen_overlap_tile.append(
                    ground_road_grass_tiles.overlap_tile_grass["right_half"][0])
                chosen_overlap_tile.append(
                    ground_road_grass_tiles.overlap_tile_grass["right_half"][1])

            if len(chosen_overlap_tile) > 0:
                grass_on_top.append(pos)
                grass_on_top.append(chosen_overlap_tile[0])
                grass_on_top.append(chosen_overlap_tile[1])

    return grass_on_top

# create all the roads
def create_all_roads(vert_roads, vert_roads_y, vert_roads_x, vert_roads_start, hori_roads, hori_roads_y, hori_roads_x, hori_roads_start):
    all_road_tiles = []
    all_overlap_tiles = []

    if vert_roads > 0:
        vert_road = create_road(vert_roads_y, vert_roads_x, vert_roads_start)
        vert_overlap = road_overlap_creation(vert_roads_y, vert_roads_x, vert_roads_start)

        for i in vert_road:
            all_road_tiles.append(i)
        for j in vert_overlap:
            all_overlap_tiles.append(j)

    if hori_roads > 0:
        hori_road = create_road(hori_roads_y, hori_roads_x, hori_roads_start)
        hori_overlap = road_overlap_creation(hori_roads_y, hori_roads_x, hori_roads_start)

        for i in hori_road:
            all_road_tiles.append(i)
        for j in hori_overlap:
            all_overlap_tiles.append(j)

    print("-------------")
    print("Overlap start")
    print("-------------")
    print(all_overlap_tiles)
    print("-------------")
    print("Overlap End")
    print("-------------")

    return all_road_tiles

# -------------------
# Water creation methods
# -------------------

# -------------------
# User Variables
# -------------------

water_x = 3
water_y = 5
water_start = [1,1]

# Create water tile maps
def create_water(height, width, start):
    complete_water = []
    for i in range(height):
        for j in range(width):
            pos = (GD_STEP_SIZE * i) + j + (GD_STEP_SIZE * start[1]) + start[0]
            
            new_water_tile = []
            if i == 0 and j == 0:
                # left top tile
                new_water_tile = []
                new_water_tile.append(
                    ground_road_grass_tiles.water_grass_border["wgrass_lt"][0])
                new_water_tile.append(
                    ground_road_grass_tiles.water_grass_border["wgrass_lt"][1])
            elif i == height-1 and j == width-1:
                # right bottom tile
                new_water_tile = []
                new_water_tile.append(
                    ground_road_grass_tiles.water_grass_border["wgrass_rb"][0])
                new_water_tile.append(
                    ground_road_grass_tiles.water_grass_border["wgrass_rb"][1])
            elif i == height-1 and j == 0:
                # left bottom tile
                new_water_tile = []
                new_water_tile.append(
                    ground_road_grass_tiles.water_grass_border["wgrass_lb"][0])
                new_water_tile.append(
                    ground_road_grass_tiles.water_grass_border["wgrass_lb"][1])
            elif i == 0 and j == width-1:
                # right top tile
                new_water_tile = []
                new_water_tile.append(
                    ground_road_grass_tiles.water_grass_border["wgrass_rt"][0])
                new_water_tile.append(
                    ground_road_grass_tiles.water_grass_border["wgrass_rt"][1])
            elif i == 0:
                new_water_tile = []
                new_water_tile.append(
                    ground_road_grass_tiles.water_grass_border["wgrass_t"][0])
                new_water_tile.append(
                    ground_road_grass_tiles.water_grass_border["wgrass_t"][1])
            elif j == 0:
                new_water_tile = []
                new_water_tile.append(
                    ground_road_grass_tiles.water_grass_border["wgrass_l"][0])
                new_water_tile.append(
                    ground_road_grass_tiles.water_grass_border["wgrass_l"][1])
            elif i == height-1:
                new_water_tile = []
                new_water_tile.append(
                    ground_road_grass_tiles.water_grass_border["wgrass_b"][0])
                new_water_tile.append(
                    ground_road_grass_tiles.water_grass_border["wgrass_b"][1])
            elif j == width-1:
                new_water_tile = []
                new_water_tile.append(
                    ground_road_grass_tiles.water_grass_border["wgrass_r"][0])
                new_water_tile.append(
                    ground_road_grass_tiles.water_grass_border["wgrass_r"][1])
            else:
                key, value = random.choice(list(ground_road_grass_tiles.full_water.items()))
                new_water_tile = []
                new_water_tile.append(value[0])
                new_water_tile.append(value[1])

            if len(new_water_tile) > 0:
                complete_water.append(pos)
                complete_water.append(new_water_tile[0])
                complete_water.append(new_water_tile[1])

    return complete_water



# -------------------
# create everything
# -------------------

# Map variables
GD_STEP_SIZE = 65536


# -------------------
# User Variables
# -------------------
map_size_x = 15
map_size_y = 15

final_map = []
converted_map = []

u_vert_roads = 0
u_vert_roads_y = 17
u_vert_roads_x = 3
u_vert_roads_start = [2, 2]

u_hori_roads = 1
u_hori_roads_y = 3
u_hori_roads_x = 18
u_hori_roads_start = [5, 10]

# tilemaps
# complete_tilemap = create_tile_map(map_size_x, map_size_y)
# road_tile_map = create_all_roads(u_vert_roads, u_vert_roads_y, u_vert_roads_y, u_vert_roads_start, u_hori_roads, u_hori_roads_y, u_hori_roads_x,u_hori_roads_start)
# water_tile_map = create_water(water_y, water_x, water_start)

# final_map = general_map_methods.fuse_map(complete_tilemap, road_tile_map)
# final_map = general_map_methods.replace_pos_dif_lvl(complete_tilemap, water_tile_map)

# print("-------------")
# print("Finished map start")
# print("-------------")
# print(final_map)
# print("-------------")
# print("Finished map End")
# print("-------------")

# print("-------------")
# print("Finished water start")
# print("-------------")
# print(water_tile_map)
# print("-------------")
# print("Finished water End")
# print("-------------")

# ---- How to use ----
# Under user variables, you set the size of the whole map
# Afterwards you don't HAVE TO edit anything, the map should be fine

# Optionally you can add water and roads
# If you are adding roads, you can choose to add vertical and horizontal roads
# In the roads section you can pick the sizes of the road.
# If you don't want any roads, set vert_roads and hori_roads to 0
# 

# If you want to add water, set the size of the water variables 
# If you don't want water, comment out the line that uses the
# final_map and replace_pos_dif_lvl()
