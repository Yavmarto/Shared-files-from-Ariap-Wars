# ------------------------------
# ------------------------------
# Ground tiles
# ------------------------------
# ------------------------------


# ---------------
# All grass and sand tiles
# ---------------

grass_sand = {
    "sand_left": [61, 0],
    "sand_right": [61, 1],
    "sand_middle": [25, 196609],

    "sand_l": [25, 196610],
    "sand_r": [25, 196608],
    "sand_b": [25, 131073],
    "sand_t": [25, 262145],

    "sand_lb": [25, 65537],
    "sand_lt": [25, 1],
    "sand_rb": [25, 65538],
    "sand_rt": [25, 2],

    "grass_rb": [25, 262146],
    "grass_rt": [25, 131074],
    "grass_lb": [25, 262144],
    "grass_lt": [25, 131072],

    "grass_empty": [8, 0],
    "grass_2_sprouts": [8, 1],
    "grass_4_sprouts": [8, 2],
    "grass_4_sprouts_flower1": [8, 3],
    "grass_4_sprouts_flower2": [8, 4],

    "grass_flower_1": [0, 327680],
    "grass_flower_2": [0, 720896],
    "grass_flower_3": [0, 327681],
    "grass_flower_4": [0, 720897],
    "grass_flower_5": [0, 327682],
    "grass_flower_6": [0, 720898]
}

# ------------------------------
# ------------------------------
# Water tiles
# ------------------------------
# ------------------------------

full_water = {
    "water_1" : [1, 196609],
    "water_2" : [7, 0],
    "water_3" : [7, 2],
    "water_4" : [7, 1]
}

water_grass_border = {
    "gwater_lt" : [1, 1],
    "gwater_lb" : [1, 65537],
    "gwater_rt" : [1, 2],
    "gwater_rb" : [1, 65538],

    "wgrass_lt" : [1, 131072],
    "wgrass_lb" : [1, 262144],
    "wgrass_rt" : [1, 131074],
    "wgrass_rb" : [1, 262146],

    "wgrass_l" : [1, 196608],
    "wgrass_t" : [1, 131073],
    "wgrass_b" : [1, 262145],
    "wgrass_r" : [1, 196610]
}

# ------------------------------
# ------------------------------
# Road tiles
# ------------------------------
# ------------------------------

road_tiles = {
    "clean_road": [58, 131073],
    "cracked_road1": [58, 327680],
    "cracked_road2": [58, 327681],
    "cracked_road3": [58, 327682]
}

# ---------------
# Overlap tiles grass
# ---------------
overlap_tile_grass = {
    "left_top": [0, 393216],
    "right_top": [0, 393217],
    "left_bottom": [0, 458752],
    "right_bottom": [0, 458753],

    "top_half": [0, 655361],
    "bottom_half": [0, 524289],
    "right_half": [0, 589824],
    "left_half": [0, 589826],

    "rbquad": [0, 131072],
    "rtquad": [0, 262146],
    "ltquad": [0, 262144],
    "lbquad": [0, 131074]
}


# ---------------
# Border tiles grass
# ---------------

border_tiles = {
    "grass_empty": [8, 0],
    "grass_2_sprouts": [8, 1],
    "grass_4_sprouts": [8, 2],
    "grass_4_sprouts_flower1": [8, 3],
    "grass_4_sprouts_flower2": [8, 4],

    "grass_flower_1": [0, 327680],
    "grass_flower_2": [0, 720896],
    "grass_flower_3": [0, 327681],
    "grass_flower_4": [0, 720897],
    "grass_flower_5": [0, 327682],
    "grass_flower_6": [0, 720898]
}

# ---------------
# Bottom check grass sand
# ---------------

grass_bottom = {
    "grass_rb": [25, 262146],
    "grass_lb": [25, 262144],
    "sand_t": [25, 262145],

    "grass_empty": [8, 0],
    "grass_2_sprouts": [8, 1],
    "grass_4_sprouts": [8, 2],
    "grass_4_sprouts_flower1": [8, 3],
    "grass_4_sprouts_flower2": [8, 4],

    "grass_flower_1": [0, 327680],
    "grass_flower_2": [0, 720896],
    "grass_flower_3": [0, 327681],
    "grass_flower_4": [0, 720897],
    "grass_flower_5": [0, 327682],
    "grass_flower_6": [0, 720898]
}

grassL_sandR_bottom = {
    "sand_r": [25, 196608],
    "sand_rt": [25, 2],
    "grass_lt": [25, 131072],
}

grassR_sandL_bottom = {
    "sand_l": [25, 196610],
    "sand_lt": [25, 1],
    "grass_rt": [25, 131074],
}

sand_bottom = {
    "sand_left": [61, 0],
    "sand_right": [61, 1],
    "sand_middle": [25, 196609],
    "sand_b": [25, 131073],
    "sand_lb": [25, 65537],
    "sand_rb": [25, 65538]
}

# ---------------
# Right check grass sand
# ---------------

grass_right = {
    "sand_l": [25, 196610],
    "grass_rb": [25, 262146],
    "grass_rt": [25, 131074],

    "grass_empty": [8, 0],
    "grass_2_sprouts": [8, 1],
    "grass_4_sprouts": [8, 2],
    "grass_4_sprouts_flower1": [8, 3],
    "grass_4_sprouts_flower2": [8, 4],

    "grass_flower_1": [0, 327680],
    "grass_flower_2": [0, 720896],
    "grass_flower_3": [0, 327681],
    "grass_flower_4": [0, 720897],
    "grass_flower_5": [0, 327682],
    "grass_flower_6": [0, 720898]
}

grassT_sandB_right = {
    "sand_b": [25, 131073],
    "grass_lt": [25, 131072],
    "sand_lb": [25, 65537],
}

grassB_sandT_right = {
    "sand_t": [25, 262145],
    "sand_lt": [25, 1],
    "grass_lb": [25, 262144],
}

sand_right = {
    "sand_left": [61, 0],
    "sand_right": [61, 1],
    "sand_middle": [25, 196609],
    "sand_rb": [25, 65538],
    "sand_rt": [25, 2],
    "sand_r": [25, 196608]
}

# ---------------
# Top check grass sand
# ---------------

grass_top = {
    "sand_b": [25, 131073],
    "grass_rt": [25, 131074],
    "grass_lt": [25, 131072],

    "grass_empty": [8, 0],
    "grass_2_sprouts": [8, 1],
    "grass_4_sprouts": [8, 2],
    "grass_4_sprouts_flower1": [8, 3],
    "grass_4_sprouts_flower2": [8, 4],

    "grass_flower_1": [0, 327680],
    "grass_flower_2": [0, 720896],
    "grass_flower_3": [0, 327681],
    "grass_flower_4": [0, 720897],
    "grass_flower_5": [0, 327682],
    "grass_flower_6": [0, 720898]
}

grassL_sandR_top = {
    "sand_r": [25, 196608],
    "sand_rb": [25, 65538],
    "grass_lb": [25, 262144]
}

grassR_sandL_top = {
    "sand_l": [25, 196610],
    "grass_rb": [25, 262146],
    "sand_lb": [25, 65537]
}

sand_top = {
    "sand_left": [61, 0],
    "sand_right": [61, 1],
    "sand_middle": [25, 196609],
    "sand_t": [25, 262145],
    "sand_lt": [25, 1],
    "sand_rt": [25, 2]
}

# ---------------
# Left match grass sand
# ---------------

grass_left = {
    "sand_r": [25, 196608],
    "grass_lb": [25, 262144],
    "grass_lt": [25, 131072],

    "grass_empty": [8, 0],
    "grass_2_sprouts": [8, 1],
    "grass_4_sprouts": [8, 2],
    "grass_4_sprouts_flower1": [8, 3],
    "grass_4_sprouts_flower2": [8, 4],

    "grass_flower_1": [0, 327680],
    "grass_flower_2": [0, 720896],
    "grass_flower_3": [0, 327681],
    "grass_flower_4": [0, 720897],
    "grass_flower_5": [0, 327682],
    "grass_flower_6": [0, 720898]
}

grassT_sandB_left = {
    "sand_b": [25, 131073],
    "sand_rb": [25, 65538],
    "grass_rt": [25, 131074],
}

grassB_sandT_left = {
    "sand_t": [25, 262145],
    "sand_rt": [25, 2],
    "grass_rb": [25, 262146],
}

sand_left = {
    "sand_left": [61, 0],
    "sand_right": [61, 1],
    "sand_middle": [25, 196609],
    "sand_lb": [25, 65537],
    "sand_lt": [25, 1],
    "sand_l": [25, 196610],
}



# ---------------
# Bottom check grass water
# ---------------

wgrass_bottom = {
    "wgrass_lb" : [1, 262144],
    "wgrass_rb" : [1, 262146],
    "wgrass_b" : [1, 262145]
}

grassL_waterR_bottom = {
    "wgrass_lt" : [1, 131072],
    "wgrass_l" : [1, 196608],
    "gwater_rt" : [1, 2],
}

grassR_waterL_bottom = {
    "wgrass_rt" : [1, 131074],
    "wgrass_r" : [1, 196610],
    "gwater_lt" : [1, 1],
}

water_bottom = {
    "water_1" : [1, 196609],
    "water_2" : [7, 0],
    "water_3" : [7, 2],
    "water_4" : [7, 1],

    "wgrass_t" : [1, 131073],
    "gwater_lb" : [1, 65537],
    "gwater_rb" : [1, 65538]
}

# ---------------
# Right check grass water
# ---------------

wgrass_right = {
    "wgrass_rt" : [1, 131074],
    "wgrass_rb" : [1, 262146],
    "wgrass_r" : [1, 196610]
}

grassT_waterB_right = {
    "wgrass_t" : [1, 131073],
    "wgrass_lt" : [1, 131072],
    "gwater_lb" : [1, 65537],
}

grassB_waterT_right = {
    "wgrass_b" : [1, 262145],
    "wgrass_lb" : [1, 262144],
    "gwater_lt" : [1, 1],
}

water_right = {
    "water_1" : [1, 196609],
    "water_2" : [7, 0],
    "water_3" : [7, 2],
    "water_4" : [7, 1],

    "wgrass_l" : [1, 196608],
    "gwater_rt" : [1, 2],
    "gwater_rb" : [1, 65538],
}

# ---------------
# Top check grass water
# ---------------

wgrass_top = {
    "wgrass_lt" : [1, 131072],
    "wgrass_rt" : [1, 131074],
    "wgrass_t" : [1, 131073]
}

water_top = {
    "water_1" : [1, 196609],
    "water_2" : [7, 0],
    "water_3" : [7, 2],
    "water_4" : [7, 1],

    "wgrass_b" : [1, 262145],
    "gwater_lt" : [1, 1],
    "gwater_rt" : [1, 2]
}

grassL_waterR_top = {
    "wgrass_l" : [1, 196608],
    "wgrass_lb" : [1, 262144],
    "gwater_rb" : [1, 65538]
}

grassR_waterL_top = {
   "wgrass_r" : [1, 196610],
   "wgrass_rb" : [1, 262146],
   "gwater_lb" : [1, 65537]
}

# ---------------
# Left check grass water
# ---------------

wgrass_left = {
    "wgrass_l" : [1, 196608],
    "wgrass_lt" : [1, 131072],
    "wgrass_lb" : [1, 262144]
}

water_left = {
    "water_1" : [1, 196609],
    "water_2" : [7, 0],
    "water_3" : [7, 2],
    "water_4" : [7, 1],

    "gwater_lt" : [1, 1],
    "gwater_lb" : [1, 65537],
    "wgrass_r" : [1, 196610]
}

grassT_waterB_left = {
    "wgrass_t" : [1, 131073],
    "wgrass_rt" : [1, 131074],
    "gwater_rb" : [1, 65538],
}

grassB_waterT_left = {
    "wgrass_b" : [1, 262145],
    "wgrass_rb" : [1, 262146],
    "gwater_rt" : [1, 2]
}