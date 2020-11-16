
castle_tiles = {
    "lt": [28, 4],
    "rt": [28, 6],
    "lb": [28, 131076],
    "rb": [28, 131078],

    "lo": [28, 65543],
    "ro": [28, 65544],

    "lbh": [28, 9],
    "lth": [1610612764, 10],
    "rbh": [28, 10],
    "rth": [1610612764, 9],

    "lh_1": [28, 65540],
    "lh_2": [28, 65545],

    "rh_1": [28, 65542],
    "rh_2": [28, 65546],

    "full_1": [28, 7],
    "full_2": [28, 5],
    "full_3": [28, 131077],
    "full_4": [28, 8]
}

castle_full = {
    "full_1": [28, 7],
    "full_2": [28, 5],
    "full_3": [28, 131077],
    "full_4": [28, 8]
}

castle_lh = {
    "lh_1": [28, 65540],
    "lh_2": [28, 65545]
}

castle_rh = {
    "rh_1": [28, 65542],
    "rh_2": [28, 65546]
}

# These checks mean, that the mentioned side connect that way, meaning the wall_bottom connects to a wall_top

# Bottom Check

# has no real connection with the tile below, most likely will be connected to a floor tile
wall_bottom = {
    "lb": [28, 131076],
    "rb": [28, 131078],
    "full_1": [28, 7],
    "full_2": [28, 5],
    "full_3": [28, 131077],
    "full_4": [28, 8]
}

wallL_emptyR_bottom = {
    "lt": [28, 4],
    "lh_1": [28, 65540],
    "lh_2": [28, 65545],
    "lbh": [28, 9]
}

wallR_emptyL_bottom = {
    "rt": [28, 6],
    "lh_1": [28, 65540],
    "lh_2": [28, 65545],
    "rbh": [28, 10]
}

wallL_emptyR_bottom_connect = {
    "lo": [28, 65543]
}

wallR_emptyL_bottom_connect = {
    "ro": [28, 65544]
}

wall_empty_bottom = {
    "lth": [1610612764, 10],
    "rth": [1610612764, 9]
}

# Top Check


# has no real connection with the tile below, most likely will be connected to a floor tile
wall_top = {
    "lt": [28, 4],
    "rt": [28, 6],
    "full_1": [28, 7],
    "full_2": [28, 5],
    "full_3": [28, 131077],
    "full_4": [28, 8]
}

wallL_emptyR_top = {
    "lb": [28, 131076],
    "lth": [1610612764, 10],
    "lh_1": [28, 65540],
    "lh_2": [28, 65545]
}

wallR_emptyL_top = {
    "rb": [28, 131078],
    "rth": [1610612764, 9],
    "rh_1": [28, 65542],
    "rh_2": [28, 65546]
}

wallL_emptyR_top_connect = {
    "lo": [28, 65543]
}

wallR_emptyL_top_connect = {
    "ro": [28, 65544]
}

wall_empty_top = {
    "rbh": [28, 10],
    "lbh": [28, 9]
}


# Left Check


# has no real connection with the tile below, most likely will be connected to a floor tile
wall_left = {
    "lt": [28, 4],
    "lb": [28, 131076],
    "lh_1": [28, 65540],
    "lh_2": [28, 65545],
}

wall_left_connect = {
    "lo": [28, 65543],
    "full_1": [28, 7],
    "full_2": [28, 5],
    "full_3": [28, 131077],
    "full_4": [28, 8]
}

wallT_emptyB_left = {
    "rt": [28, 6],
    "lth": [1610612764, 10]
}

wallB_emptyT_left = {
    "rb": [28, 131078],
    "lbh": [28, 9]
}


wall_empty_left = {
    "rbh": [28, 10],
    "rth": [1610612764, 9],
    "rh_1": [28, 65542],
    "rh_2": [28, 65546],
    "ro": [28, 65544]
}

# Left Check


# has no real connection with the tile below, most likely will be connected to a floor tile
wall_right = {
    "rt": [28, 6],
    "rb": [28, 131078],
    "rh_1": [28, 65542],
    "rh_2": [28, 65546]
}

wall_right_connect = {
    "ro": [28, 65544],
    "full_1": [28, 7],
    "full_2": [28, 5],
    "full_3": [28, 131077],
    "full_4": [28, 8]
}

wallT_emptyB_right = {
    "lt": [28, 4],
    "rth": [1610612764, 9]
}

wallB_emptyT_right = {
    "lb": [28, 131076],
    "rbh": [28, 10]
}


wall_empty_right = {
    "lh_1": [28, 65540],
    "lh_2": [28, 65545],
    "lbh": [28, 9],
    "lth": [1610612764, 10],
    "lo": [28, 65543]
}
