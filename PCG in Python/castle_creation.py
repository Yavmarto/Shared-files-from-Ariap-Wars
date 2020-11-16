import random
import general_map_methods
import castle_tiles
import ground_road_grass_tiles
from enum import Enum


class Left_Tile(Enum):
    wall_right = 1
    wall_right_connect = 2
    wallT_emptyB_right = 3
    wallB_emptyT_right = 4
    wall_empty_right = 5


class Bottom_Tile(Enum):
    wall_bottom = 1
    wallL_emptyR_bottom = 2
    wallR_emptyL_bottom = 3
    wallL_emptyR_bottom_connect = 4
    wallR_emptyL_bottom_connect = 5
    wall_empty_bottom = 6

def check_tile_above(top_tile):
    if top_tile in castle_tiles.wall_bottom.values():
        return Bottom_Tile.wall_bottom
    elif top_tile in castle_tiles.wallL_emptyR_bottom.values():
        return Bottom_Tile.wallL_emptyR_bottom
    elif top_tile in castle_tiles.wallR_emptyL_bottom.values():
        return Bottom_Tile.wallR_emptyL_bottom
    elif top_tile in castle_tiles.wallL_emptyR_bottom_connect.values():
        return Bottom_Tile.wallL_emptyR_bottom_connect
    elif top_tile in castle_tiles.wallR_emptyL_bottom_connect.values():
        return Bottom_Tile.wallR_emptyL_bottom_connect
    elif top_tile in castle_tiles.wall_empty_bottom.values():
        return Bottom_Tile.wall_empty_bottom

def check_tile_left(left_tile):
    if left_tile in castle_tiles.wall_right.values():
        return Left_Tile.wall_right
    elif left_tile in castle_tiles.wall_right_connect.values():
        return Left_Tile.wall_right_connect
    elif left_tile in castle_tiles.wallT_emptyB_right.values():
        return Left_Tile.wallT_emptyB_right
    elif left_tile in castle_tiles.wallB_emptyT_right.values():
        return Left_Tile.wallB_emptyT_right
    elif left_tile in castle_tiles.wall_empty_right.values():
        return Left_Tile.wall_empty_right

def get_top(bottom, pos):
    if bottom == Bottom_Tile.wall_bottom:
        return general_map_methods.get_random_tile(castle_tiles.wall_top, pos)
    elif bottom == Bottom_Tile.wallL_emptyR_bottom:
        return general_map_methods.get_random_tile(castle_tiles.wallL_emptyR_top, pos)
    elif bottom == Bottom_Tile.wallL_emptyR_bottom_connect:
        return general_map_methods.get_random_tile(castle_tiles.wallL_emptyR_top_connect, pos)
    elif bottom == Bottom_Tile.wallR_emptyL_bottom:
        return general_map_methods.get_random_tile(castle_tiles.wallR_emptyL_top, pos)
    elif bottom == Bottom_Tile.wallR_emptyL_bottom_connect:
        return general_map_methods.get_random_tile(castle_tiles.wallR_emptyL_top_connect, pos)



def get_left(left, tile):
    tile.pop(0)

    if left == Left_Tile.wall_right:
        return tile in castle_tiles.wall_left.values()
    elif left == Left_Tile.wall_right_connect:
        return tile in castle_tiles.wall_left_connect.values()
    elif left == Left_Tile.wallB_emptyT_right:
        return tile in castle_tiles.wallB_emptyT_right.values()
    elif left == Left_Tile.wallT_emptyB_right:
        return tile in castle_tiles.wallT_emptyB_right.values()
    elif left == Left_Tile.wall_empty_right:
        return tile in castle_tiles.wall_empty_right.values()
    return False

# -------------------
# create the tilemap
# -------------------

def create_tile_map(map_size_y, map_size_x):
    for i in range(map_size_y):
        for j in range(map_size_x):
            pos = (GD_STEP_SIZE * i) + j
            chosen_tile = []
            # set overlap tiles
            
            
            if i == 0 and j == 0:
                # left top tile
                chosen_tile.append(pos)
                chosen_tile.append(
                    castle_tiles.castle_tiles["lt"][0])
                chosen_tile.append(
                    castle_tiles.castle_tiles["lt"][1])
            elif i == map_size_y-1 and j == map_size_x-1:
                # right bottom tile
                chosen_tile.append(pos)
                chosen_tile.append(
                    castle_tiles.castle_tiles["rb"][0])
                chosen_tile.append(
                    castle_tiles.castle_tiles["rb"][1])
            elif i == map_size_y-1 and j == 0:
                # left bottom tile
                chosen_tile.append(pos)
                chosen_tile.append(
                    castle_tiles.castle_tiles["lb"][0])
                chosen_tile.append(
                    castle_tiles.castle_tiles["lb"][1])
            elif i == 0 and j == map_size_x-1:
                # right top tile
                chosen_tile.append(pos)
                chosen_tile.append(
                    castle_tiles.castle_tiles["rt"][0])
                chosen_tile.append(
                    castle_tiles.castle_tiles["rt"][1])
            elif i == 0:
                chosen_tile = general_map_methods.get_random_tile(castle_tiles.castle_full, pos)
            elif j == 0:
                chosen_tile = general_map_methods.get_random_tile(castle_tiles.castle_lh, pos)
            elif i == map_size_y-1:    
                chosen_tile = general_map_methods.get_random_tile(castle_tiles.castle_full, pos)
            elif j == map_size_x-1:
                chosen_tile = general_map_methods.get_random_tile(castle_tiles.castle_rh, pos)
            
            ground_tile = general_map_methods.get_road_tile()
            ground_tile.insert(0, pos)

            if len(ground_tile) > 0:
                for part in ground_tile:
                    floor_map.append(part)

            if len(chosen_tile) > 0:
                for part in chosen_tile:
                    wall_map.append(part)

    return [wall_map, floor_map]


# Map variables
GD_STEP_SIZE = 65536

# map arrays
wall_map = []
floor_map = []

# wall_map = create_tile_map()

# print("ground map") 
# print(wall_map)
# print("floor map")
# print(floor_map)

# Instead of creating a complete level, we can just create a 'smaller' castle 
# and merge it with another map. However we do this, the border tiles are: 
# the full tiles on the top and bottom line and the half tiles on the left 
# and right sides. Close with the relevant corner tiles. The middle part can
# a bit tricky. 
# 
# When you have a full wall tile on top, you can only match it a ground tile below. 
# If you have a ground tile on top, you can have another ground tile (most likely) 
# or new wall (less likely). 
# Otherwise you have to match what's on the top and to the left.
#
# When you have a wall on the left side you can only have ground tile next to it
# If you have a ground tile to the left, you can have another ground tile 
# (most likely), or a new wall (less likely).
# Otherwise you have to match what's on the top and to the left