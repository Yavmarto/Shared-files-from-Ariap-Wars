import fileinput
import os.path
import general_map_methods
import castle_creation
import cave_dark_creation
import cave_light_creation
import ground_road_grass_creation
import island_creation
import lava_creation
# import tree_creation

new_file_name = "/Users/yoshimartodihardjo/ariap-wars/Levels/LevelCreation_gen"
extension = ".tscn"
while os.path.exists(new_file_name + extension):
    new_file_name += "-1"
f = open(new_file_name + extension, "w+")

file_name = "/Users/yoshimartodihardjo/ariap-wars/Levels/LevelCreation.tscn"


# -------------------
# -------------------
# Creation sections
# -------------------
# -------------------

# -------------------
# Ground road grass sections
# -------------------

sub_ground_map = ground_road_grass_creation.create_tile_map(28, 16)
road_tile_map = ground_road_grass_creation.create_road(5, 28, [0, 0])
ground_extra_map = ground_road_grass_creation.road_overlap_creation(0, 0, [
                                                                    0, 4])

# Final arrays
water_map = ground_road_grass_creation.create_water(0, 0, [0, 6])
ground_map = general_map_methods.fuse_map(sub_ground_map, road_tile_map)
ground_map = general_map_methods.replace_pos_dif_lvl(sub_ground_map, water_map)


# Unused arrays
water_extra_map = []
fly_map = []
fly_extra_map = []
impassable_map = []
impassable_extra_map = []

# -------------------
# castle creation sections
# -------------------

# # Final arrays
# wall_ground = castle_creation.create_tile_map(16,28)
# impassable_map = wall_ground[0]
# ground_map = wall_ground[1]

# # Unused
# ground_extra_map = []
# water_map = []
# water_extra_map = []
# fly_map = []
# fly_extra_map = []
# impassable_extra_map = []

# -------------------
# cave light creation sections
# -------------------


# # tilemaps creation
# complete_tilemap = cave_light_creation.create_tile_map()
# ground_fly = cave_light_creation.add_ground_tiles(complete_tilemap)
# ground1 = ground_fly[0]

# # Optional
# hori_roads_x = 10
# hori_roads_y = 10
# hori_roads_start = [2,2]

# water_x = 7
# water_y = 5
# water_start = [6,6]

# road_map = cave_light_creation.create_road(hori_roads_x, hori_roads_y, hori_roads_start) # merges into ground
# road_overlap = cave_light_creation.overlap_creation(hori_roads_x, hori_roads_y, hori_roads_start) # merges into ground extra
# water_ground_map = cave_light_creation.create_water(water_x, water_y, water_start) # goes into water
# water_overlap = cave_light_creation.overlap_creation(hori_roads_x, hori_roads_y, water_start) 

# ground_map_fused = general_map_methods.fuse_map(ground1, water_ground_map[1]) # merges into ground

# # Final arrays
# ground_map = general_map_methods.fuse_map(ground_map_fused, road_map) # Goes into ground
# ground_extra_map = general_map_methods.append_maps(road_overlap, water_overlap) # Goes into ground extra
# water_map = water_ground_map[0]
# fly_map = ground_fly[1]

# # Unused
# water_extra_map = []
# fly_extra_map = []
# impassable_map = []
# impassable_extra_map = []

# -------------------
# cave dark creation sections
# -------------------

# # tilemaps creation
# complete_tilemap = cave_dark_creation.create_tile_map()
# ground_fly = cave_dark_creation.add_ground_tiles(complete_tilemap)
# ground1 = ground_fly[0]

# # Optional
# hori_roads_x = 0
# hori_roads_y = 0
# hori_roads_start = [2,2]

# water_x = 0
# water_y = 0
# water_start = [6,6]

# road_map = cave_dark_creation.create_road(hori_roads_x, hori_roads_y, hori_roads_start) # merges into ground
# road_overlap = cave_dark_creation.overlap_creation(hori_roads_x, hori_roads_y, hori_roads_start) # merges into ground extra
# water_ground_map = cave_dark_creation.create_water(water_x, water_y, water_start) # goes into water
# water_overlap = cave_dark_creation.overlap_creation(hori_roads_x, hori_roads_y, water_start) 

# ground_map_fused = general_map_methods.fuse_map(ground1, water_ground_map[1]) # merges into ground

# # Final arrays
# ground_map = general_map_methods.fuse_map(ground_map_fused, road_map) # Goes into ground
# ground_extra_map = general_map_methods.append_maps(road_overlap, water_overlap) # Goes into ground extra
# water_map = water_ground_map[0]
# fly_map = ground_fly[1]

# # Unused
# water_extra_map = []
# fly_extra_map = []
# impassable_map = []
# impassable_extra_map = []

# -------------------
# island creation sections
# -------------------

# total_map = island_creation.create_tile_map(22,22)
# all_maps = island_creation.separate_island(total_map)

# # Final arrays
# ground_map = all_maps[0]
# water_map = all_maps[1]
# fly_map = all_maps[2]


# # Unused arrays
# ground_extra_map = []
# water_extra_map = []
# fly_extra_map = []
# impassable_map = []
# impassable_extra_map = []

# -------------------
# lava cave creation sections
# -------------------

# complete_tilemap = lava_creation.create_tile_map(20, 20)
# mixed_map = lava_creation.add_ground_tiles(complete_tilemap)

# ground_map = mixed_map[0]
# ground_extra_map = []
# water_map = []
# water_extra_map = []
# fly_map = mixed_map[1]
# fly_extra_map = []
# impassable_map = lava_creation.create_lava(4,4, [0,0])
# impassable_extra_map = []


def create_file():
    ground = False
    ground_extra = False
    water = False
    water_extra = False
    fly = False
    fly_extra = False
    impassable = False
    impassable_extra = False

    for line in fileinput.FileInput(file_name, inplace=0):
        if "Ground" in line and "TileMap" in line and not "extra" in line:
            ground = True
            f.write(line)

        elif ground and "format" in line:
            f.write(line)
            ground = False

            if len(ground_map) > 0:
                f.write("tile_data =  PoolIntArray(" +
                        str(ground_map).strip('[]') + ")")

        elif "Ground" in line and "extra" in line:
            ground_extra = True
            f.write(line)

        elif ground_extra and "format" in line:
            f.write(line)
            ground_extra = False

            if len(ground_extra_map) > 0:
                f.write("tile_data =  PoolIntArray(" +
                        str(ground_extra_map).strip('[]') + ")")

        elif "Water" in line and not "extra" in line:
            water = True
            f.write(line)

        elif water and "format" in line:
            f.write(line)
            water = False

            if len(water_map) > 0:
                f.write("tile_data =  PoolIntArray(" +
                        str(water_map).strip('[]') + ")")

        elif "Water" in line and "extra" in line:
            water_extra = True
            f.write(line)

        elif water_extra and "format" in line:
            f.write(line)
            water_extra = False

            if len(water_extra_map) > 0:
                f.write("tile_data =  PoolIntArray(" +
                        str(water_extra_map).strip('[]') + ")")

        elif "Fly" in line and not "extra" in line:
            fly = True
            f.write(line)

        elif fly and "format" in line:
            f.write(line)
            fly = False

            if len(fly_map) > 0:
                f.write("tile_data =  PoolIntArray(" +
                        str(fly_map).strip('[]') + ")")

        elif "Fly" in line and "extra" in line:
            fly_extra = True
            f.write(line)

        elif fly_extra and "format" in line:
            f.write(line)
            fly_extra = False

            if len(fly_extra_map) > 0:
                f.write("tile_data =  PoolIntArray(" +
                        str(fly_extra_map).strip('[]') + ")")

        elif "Impassable" in line and not "extra" in line:
            impassable = True
            f.write(line)

        elif impassable and "format" in line:
            f.write(line)
            impassable = False

            if len(impassable_map) > 0:
                f.write("tile_data =  PoolIntArray(" +
                        str(impassable_map).strip('[]') + ")")

        elif "Impassable" in line and "extra" in line:
            impassable_extra = True
            f.write(line)

        elif impassable_extra and "format" in line:
            f.write(line)
            impassable_extra = False

            if len(impassable_extra_map) > 0:
                f.write("tile_data =  PoolIntArray(" +
                        str(impassable_extra_map).strip('[]') + ")")

        else:
            f.write(line)

    f.close()


create_file()
