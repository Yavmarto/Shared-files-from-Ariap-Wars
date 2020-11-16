
all_island = {
    "ysand_lt": [3, 1],
    "ysand_rt": [3, 2],
    "ysand_lb": [3, 65537],
    "ysand_rb": [3, 65538],

    "ywater_lt": [3, 131072],
    "ywater_lb": [3, 262144],
    "ywater_rt": [3, 131074],
    "ywater_rb": [3, 262146],

    "ywater_t": [3, 131073],
    "ywater_l": [3, 196608],
    "ywater_r": [3, 196610],
    "ywater_b": [3, 262145],

    "water_s_ysand": [3, 0],
    "water_l_ysand": [3, 65536],
    "full_ysand": [3, 196609]

}

full_water = {
    "water_1": [1, 196609],
    "water_2": [7, 0],
    "water_3": [7, 2],
    "water_4": [7, 1],
    "water_s_ysand": [3, 0],
    "water_l_ysand": [3, 65536]
}

most_water = {
    "water_1": [1, 196609],
    "water_2": [7, 0],
    "water_3": [7, 2],
    "water_4": [7, 1],
    
    "ywater_lt": [3, 131072],
    "ywater_lb": [3, 262144],
    "ywater_rt": [3, 131074],
    "ywater_rb": [3, 262146],

    "ywater_t": [3, 131073],
    "ywater_l": [3, 196608],
    "ywater_r": [3, 196610],
    "ywater_b": [3, 262145]
}

fly_water = {
    "water_s_ysand": [3, 0],
    "water_l_ysand": [3, 65536]
}

# bottom check

ysand_bottom = {
    "full_ysand": [3, 196609],

    "ywater_t": [3, 131073],

    "ysand_lb": [3, 65537],
    "ysand_rb": [3, 65538]
}

ywater_bottom = {
    "water_1": [1, 196609],
    "water_2": [7, 0],
    "water_3": [7, 2],
    "water_4": [7, 1],
    "water_s_ysand": [3, 0],
    "water_l_ysand": [3, 65536],

    "ywater_lb": [3, 262144],
    "ywater_rb": [3, 262146],
    "ywater_b": [3, 262145]
}

waterL_ysandR_bottom = {
    "ywater_l": [3, 196608],
    "ywater_lt": [3, 131072],
    "ysand_rt": [3, 2]
}

waterR_ysandL_bottom = {
    "ywater_r": [3, 196610],
    "ywater_rt": [3, 131074],
    "ysand_lt": [3, 1]
}

# right check

ysand_right = {
    "full_ysand": [3, 196609],

    "ywater_l": [3, 196608],

    "ysand_rb": [3, 65538],
    "ysand_rt": [3, 2]
}

ywater_right = {
    "water_1": [1, 196609],
    "water_2": [7, 0],
    "water_3": [7, 2],
    "water_4": [7, 1],
    "water_s_ysand": [3, 0],
    "water_l_ysand": [3, 65536],

    "ywater_rt": [3, 131074],
    "ywater_rb": [3, 262146],
    "ywater_r": [3, 196610]
}

waterT_ysandB_right = {
    "ywater_lt": [3, 131072],
    "ysand_lb": [3, 65537],
    "ywater_t": [3, 131073]
}

waterB_ysandT_right = {
    "ywater_lb": [3, 262144],
    "ysand_lt": [3, 1],
    "ywater_b": [3, 262145]
}

# top check

ysand_top = {
    "full_ysand": [3, 196609],

    "ywater_b": [3, 262145],
    "ysand_lt": [3, 1],
    "ysand_rt": [3, 2]
}

ywater_top = {
    "water_1": [1, 196609],
    "water_2": [7, 0],
    "water_3": [7, 2],
    "water_4": [7, 1],
    "water_s_ysand": [3, 0],
    "water_l_ysand": [3, 65536],

    "ywater_t": [3, 131073],
    "ywater_lt": [3, 131072],
    "ywater_rt": [3, 131074]
}

waterL_ysandR_top = {
    "ywater_l": [3, 196608],
    "ywater_lb": [3, 262144],
    "ysand_rb": [3, 65538]
}

waterR_ysandL_top = {
    "ywater_r": [3, 196610],
    "ywater_rb": [3, 262146],
    "ysand_lb": [3, 65537]
}

# left check

ysand_left = {
    "full_ysand": [3, 196609],

    "ywater_r": [3, 196610],
    "ysand_lt": [3, 1],
    "ysand_lb": [3, 65537]
}

ywater_left = {
    "water_1": [1, 196609],
    "water_2": [7, 0],
    "water_3": [7, 2],
    "water_4": [7, 1],
    "water_s_ysand": [3, 0],
    "water_l_ysand": [3, 65536],

    "ywater_l": [3, 196608],
    "ywater_lt": [3, 131072],
    "ywater_lb": [3, 262144]
}

waterT_ysandB_left = {
    "ywater_rt": [3, 131074],
    "ywater_t": [3, 131073],
    "ysand_rb": [3, 65538]
}

waterB_ysandT_left = {
   "ywater_rb": [3, 262146],
   "ywater_b": [3, 262145],
   "ysand_rt": [3, 2]
}