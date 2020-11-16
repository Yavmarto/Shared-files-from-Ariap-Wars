import csv

csv_columns = ['buildings_left', 'current_test_cycle','duration','end_turn',
'enemies_needed',
'level',
'losers_units_left',
'tested_enemy',
'tested_unit',
'winner',
'winner_units',
'winner_units_left']

dict =  [ {
"buildings_left": 0,
"current_test_cycle": 0,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Greaper",
"tested_unit": "Greaper",
"winner": "AI",
"winner_units": [ {
"health": 822.355,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
} ],
"winner_units_left": 119
}, {
"buildings_left": 0,
"current_test_cycle": 0,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Laser Dolphin",
"tested_unit": "Greaper",
"winner": "AI",
"winner_units": [ {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
} ],
"winner_units_left": 113
}, {
"buildings_left": 0,
"current_test_cycle": 0,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Laser Shell",
"tested_unit": "Greaper",
"winner": "AI",
"winner_units": [ {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
} ],
"winner_units_left": 116
}, {
"buildings_left": 0,
"current_test_cycle": 0,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Shuttle Carrier",
"tested_unit": "Greaper",
"winner": "AI",
"winner_units": [ {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 839.571,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
} ],
"winner_units_left": 118
}, {
"buildings_left": 0,
"current_test_cycle": 0,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Caterflame",
"tested_unit": "Greaper",
"winner": "AI",
"winner_units": [ {
"health": 267.252,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
} ],
"winner_units_left": 119
}, {
"buildings_left": 0,
"current_test_cycle": 0,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Divine Spear",
"tested_unit": "Greaper",
"winner": "AI",
"winner_units": [ {
"health": 1154.23,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
} ],
"winner_units_left": 119
}, {
"buildings_left": 0,
"current_test_cycle": 0,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Flonine",
"tested_unit": "Greaper",
"winner": "AI",
"winner_units": [ {
"health": 750.0,
"name": "Flonine"
}, {
"health": 736.199,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
} ],
"winner_units_left": 118
}, {
"buildings_left": 0,
"current_test_cycle": 0,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Flying Warrior",
"tested_unit": "Greaper",
"winner": "AI",
"winner_units": [ {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
} ],
"winner_units_left": 118
}, {
"buildings_left": 0,
"current_test_cycle": 0,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Glidog",
"tested_unit": "Greaper",
"winner": "AI",
"winner_units": [ {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 414.978,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
} ],
"winner_units_left": 117
}, {
"buildings_left": 0,
"current_test_cycle": 0,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Humming sabre",
"tested_unit": "Greaper",
"winner": "AI",
"winner_units": [ {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 345.217,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
} ],
"winner_units_left": 116
}, {
"buildings_left": 0,
"current_test_cycle": 0,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Battle Bear",
"tested_unit": "Greaper",
"winner": "AI",
"winner_units": [ {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 823.87,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
} ],
"winner_units_left": 118
}, {
"buildings_left": 0,
"current_test_cycle": 0,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Percen",
"tested_unit": "Greaper",
"winner": "AI",
"winner_units": [ {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 238.517,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
} ],
"winner_units_left": 117
}, {
"buildings_left": 0,
"current_test_cycle": 0,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Bowshot",
"tested_unit": "Greaper",
"winner": "AI",
"winner_units": [ {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 168.439,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
} ],
"winner_units_left": 118
}, {
"buildings_left": 0,
"current_test_cycle": 0,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Clawrex",
"tested_unit": "Greaper",
"winner": "AI",
"winner_units": [ {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 238.294,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
} ],
"winner_units_left": 118
}, {
"buildings_left": 0,
"current_test_cycle": 0,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Drill",
"tested_unit": "Greaper",
"winner": "AI",
"winner_units": [ {
"health": 850.0,
"name": "Drill"
}, {
"health": 668.918,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
} ],
"winner_units_left": 118
}, {
"buildings_left": 0,
"current_test_cycle": 0,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Farshot",
"tested_unit": "Greaper",
"winner": "AI",
"winner_units": [ {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
} ],
"winner_units_left": 118
}, {
"buildings_left": 0,
"current_test_cycle": 0,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Imtail",
"tested_unit": "Greaper",
"winner": "AI",
"winner_units": [ {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 217.118,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
} ],
"winner_units_left": 112
}, {
"buildings_left": 0,
"current_test_cycle": 0,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Mechanic",
"tested_unit": "Greaper",
"winner": "AI",
"winner_units": [ {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 434.26,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
} ],
"winner_units_left": 115
}, {
"buildings_left": 0,
"current_test_cycle": 0,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Rocket Moose",
"tested_unit": "Greaper",
"winner": "AI",
"winner_units": [ {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 578.89,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
} ],
"winner_units_left": 118
}, {
"buildings_left": 0,
"current_test_cycle": 0,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Gun bot",
"tested_unit": "Greaper",
"winner": "AI",
"winner_units": [ {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 391.223,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
} ],
"winner_units_left": 114
}, {
"buildings_left": 0,
"current_test_cycle": 0,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Tank",
"tested_unit": "Greaper",
"winner": "AI",
"winner_units": [ {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
} ],
"winner_units_left": 118
}, {
"buildings_left": 0,
"current_test_cycle": 0,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Warrior",
"tested_unit": "Greaper",
"winner": "AI",
"winner_units": [ {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 438.789,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
} ],
"winner_units_left": 117
}, {
"buildings_left": 0,
"current_test_cycle": 0,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Hoverflop",
"tested_unit": "Greaper",
"winner": "AI",
"winner_units": [ {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 706.708,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
} ],
"winner_units_left": 118
}, {
"buildings_left": 0,
"current_test_cycle": 0,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Octospike",
"tested_unit": "Greaper",
"winner": "AI",
"winner_units": [ {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 853.439,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
} ],
"winner_units_left": 118
}, {
"buildings_left": 0,
"current_test_cycle": 1,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Greaper",
"tested_unit": "Laser Dolphin",
"winner": "AI",
"winner_units": [ {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
} ],
"winner_units_left": 119
}, {
"buildings_left": 0,
"current_test_cycle": 1,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Laser Dolphin",
"tested_unit": "Laser Dolphin",
"winner": "AI",
"winner_units": [ {
"health": 275.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
} ],
"winner_units_left": 119
}, {
"buildings_left": 0,
"current_test_cycle": 1,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Laser Shell",
"tested_unit": "Laser Dolphin",
"winner": "AI",
"winner_units": [ {
"health": 611.922,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
} ],
"winner_units_left": 119
}, {
"buildings_left": 0,
"current_test_cycle": 1,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Shuttle Carrier",
"tested_unit": "Laser Dolphin",
"winner": "AI",
"winner_units": [ {
"health": 999.281,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
} ],
"winner_units_left": 119
}, {
"buildings_left": 0,
"current_test_cycle": 1,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Caterflame",
"tested_unit": "Laser Dolphin",
"winner": "AI",
"winner_units": [ {
"health": 859.302,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
} ],
"winner_units_left": 119
}, {
"buildings_left": 0,
"current_test_cycle": 1,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Divine Spear",
"tested_unit": "Laser Dolphin",
"winner": "AI",
"winner_units": [ {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
} ],
"winner_units_left": 119
}, {
"buildings_left": 0,
"current_test_cycle": 1,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Flonine",
"tested_unit": "Laser Dolphin",
"winner": "AI",
"winner_units": [ {
"health": 699.254,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
} ],
"winner_units_left": 119
}, {
"buildings_left": 0,
"current_test_cycle": 1,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Flying Warrior",
"tested_unit": "Laser Dolphin",
"winner": "AI",
"winner_units": [ {
"health": 792.52,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
} ],
"winner_units_left": 119
}, {
"buildings_left": 0,
"current_test_cycle": 1,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Glidog",
"tested_unit": "Laser Dolphin",
"winner": "AI",
"winner_units": [ {
"health": 321.076,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
} ],
"winner_units_left": 119
}, {
"buildings_left": 0,
"current_test_cycle": 1,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Humming sabre",
"tested_unit": "Laser Dolphin",
"winner": "AI",
"winner_units": [ {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
} ],
"winner_units_left": 118
}, {
"buildings_left": 0,
"current_test_cycle": 1,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Battle Bear",
"tested_unit": "Laser Dolphin",
"winner": "AI",
"winner_units": [ {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
} ],
"winner_units_left": 119
}, {
"buildings_left": 0,
"current_test_cycle": 1,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Percen",
"tested_unit": "Laser Dolphin",
"winner": "AI",
"winner_units": [ {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
} ],
"winner_units_left": 119
}, {
"buildings_left": 0,
"current_test_cycle": 1,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Bowshot",
"tested_unit": "Laser Dolphin",
"winner": "AI",
"winner_units": [ {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
} ],
"winner_units_left": 119
}, {
"buildings_left": 0,
"current_test_cycle": 1,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Clawrex",
"tested_unit": "Laser Dolphin",
"winner": "AI",
"winner_units": [ {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
} ],
"winner_units_left": 119
}, {
"buildings_left": 0,
"current_test_cycle": 1,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Drill",
"tested_unit": "Laser Dolphin",
"winner": "AI",
"winner_units": [ {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
} ],
"winner_units_left": 119
}, {
"buildings_left": 0,
"current_test_cycle": 1,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Farshot",
"tested_unit": "Laser Dolphin",
"winner": "AI",
"winner_units": [ {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
} ],
"winner_units_left": 119
}, {
"buildings_left": 0,
"current_test_cycle": 1,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Imtail",
"tested_unit": "Laser Dolphin",
"winner": "AI",
"winner_units": [ {
"health": 191.25,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
} ],
"winner_units_left": 119
}, {
"buildings_left": 0,
"current_test_cycle": 1,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Mechanic",
"tested_unit": "Laser Dolphin",
"winner": "AI",
"winner_units": [ {
"health": 405.469,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
} ],
"winner_units_left": 119
}, {
"buildings_left": 0,
"current_test_cycle": 1,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Rocket Moose",
"tested_unit": "Laser Dolphin",
"winner": "AI",
"winner_units": [ {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
} ],
"winner_units_left": 119
}, {
"buildings_left": 0,
"current_test_cycle": 1,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Gun bot",
"tested_unit": "Laser Dolphin",
"winner": "AI",
"winner_units": [ {
"health": 343.75,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
} ],
"winner_units_left": 119
}, {
"buildings_left": 0,
"current_test_cycle": 1,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Tank",
"tested_unit": "Laser Dolphin",
"winner": "AI",
"winner_units": [ {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
} ],
"winner_units_left": 119
}, {
"buildings_left": 0,
"current_test_cycle": 1,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Warrior",
"tested_unit": "Laser Dolphin",
"winner": "AI",
"winner_units": [ {
"health": 589.411,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
} ],
"winner_units_left": 119
}, {
"buildings_left": 0,
"current_test_cycle": 1,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Hoverflop",
"tested_unit": "Laser Dolphin",
"winner": "AI",
"winner_units": [ {
"health": 691.008,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
} ],
"winner_units_left": 119
}, {
"buildings_left": 0,
"current_test_cycle": 1,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Octospike",
"tested_unit": "Laser Dolphin",
"winner": "AI",
"winner_units": [ {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
} ],
"winner_units_left": 119
}, {
"buildings_left": 0,
"current_test_cycle": 2,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Greaper",
"tested_unit": "Laser Shell",
"winner": "AI",
"winner_units": [ {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
} ],
"winner_units_left": 119
}, {
"buildings_left": 0,
"current_test_cycle": 2,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Laser Dolphin",
"tested_unit": "Laser Shell",
"winner": "AI",
"winner_units": [ {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 317.266,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
} ],
"winner_units_left": 118
}, {
"buildings_left": 0,
"current_test_cycle": 2,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Laser Shell",
"tested_unit": "Laser Shell",
"winner": "AI",
"winner_units": [ {
"health": 441.554,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
} ],
"winner_units_left": 119
}, {
"buildings_left": 0,
"current_test_cycle": 2,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Shuttle Carrier",
"tested_unit": "Laser Shell",
"winner": "AI",
"winner_units": [ {
"health": 819.242,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
} ],
"winner_units_left": 119
}, {
"buildings_left": 0,
"current_test_cycle": 2,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Caterflame",
"tested_unit": "Laser Shell",
"winner": "AI",
"winner_units": [ {
"health": 682.622,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
} ],
"winner_units_left": 119
}, {
"buildings_left": 0,
"current_test_cycle": 2,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Divine Spear",
"tested_unit": "Laser Shell",
"winner": "AI",
"winner_units": [ {
"health": 1167.15,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
} ],
"winner_units_left": 119
}, {
"buildings_left": 0,
"current_test_cycle": 2,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Flonine",
"tested_unit": "Laser Shell",
"winner": "AI",
"winner_units": [ {
"health": 386.605,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
} ],
"winner_units_left": 119
}, {
"buildings_left": 0,
"current_test_cycle": 2,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Flying Warrior",
"tested_unit": "Laser Shell",
"winner": "AI",
"winner_units": [ {
"health": 628.125,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
} ],
"winner_units_left": 119
}, {
"buildings_left": 0,
"current_test_cycle": 2,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Glidog",
"tested_unit": "Laser Shell",
"winner": "AI",
"winner_units": [ {
"health": 500.0,
"name": "Glidog"
}, {
"health": 395.582,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
} ],
"winner_units_left": 118
}, {
"buildings_left": 0,
"current_test_cycle": 2,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Humming sabre",
"tested_unit": "Laser Shell",
"winner": "AI",
"winner_units": [ {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 369.623,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
} ],
"winner_units_left": 117
}, {
"buildings_left": 0,
"current_test_cycle": 2,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Battle Bear",
"tested_unit": "Laser Shell",
"winner": "AI",
"winner_units": [ {
"health": 881.907,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
} ],
"winner_units_left": 119
}, {
"buildings_left": 0,
"current_test_cycle": 2,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Percen",
"tested_unit": "Laser Shell",
"winner": "AI",
"winner_units": [ {
"health": 302.771,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
} ],
"winner_units_left": 119
}, {
"buildings_left": 0,
"current_test_cycle": 2,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Bowshot",
"tested_unit": "Laser Shell",
"winner": "AI",
"winner_units": [ {
"health": 451.855,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
} ],
"winner_units_left": 119
}, {
"buildings_left": 0,
"current_test_cycle": 2,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Clawrex",
"tested_unit": "Laser Shell",
"winner": "AI",
"winner_units": [ {
"health": 620.312,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
} ],
"winner_units_left": 119
}, {
"buildings_left": 0,
"current_test_cycle": 2,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Drill",
"tested_unit": "Laser Shell",
"winner": "AI",
"winner_units": [ {
"health": 801.58,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
} ],
"winner_units_left": 119
}, {
"buildings_left": 0,
"current_test_cycle": 2,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Farshot",
"tested_unit": "Laser Shell",
"winner": "AI",
"winner_units": [ {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
} ],
"winner_units_left": 119
}, {
"buildings_left": 0,
"current_test_cycle": 2,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Imtail",
"tested_unit": "Laser Shell",
"winner": "AI",
"winner_units": [ {
"health": 300.0,
"name": "Imtail"
}, {
"health": 202.437,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
} ],
"winner_units_left": 118
}, {
"buildings_left": 0,
"current_test_cycle": 2,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Mechanic",
"tested_unit": "Laser Shell",
"winner": "AI",
"winner_units": [ {
"health": 263.533,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
} ],
"winner_units_left": 119
}, {
"buildings_left": 0,
"current_test_cycle": 2,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Rocket Moose",
"tested_unit": "Laser Shell",
"winner": "AI",
"winner_units": [ {
"health": 750.403,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
} ],
"winner_units_left": 119
}, {
"buildings_left": 0,
"current_test_cycle": 2,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Gun bot",
"tested_unit": "Laser Shell",
"winner": "AI",
"winner_units": [ {
"health": 115.562,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
} ],
"winner_units_left": 119
}, {
"buildings_left": 0,
"current_test_cycle": 2,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Tank",
"tested_unit": "Laser Shell",
"winner": "AI",
"winner_units": [ {
"health": 989.864,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
} ],
"winner_units_left": 119
}, {
"buildings_left": 0,
"current_test_cycle": 2,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Warrior",
"tested_unit": "Laser Shell",
"winner": "AI",
"winner_units": [ {
"health": 486.344,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
} ],
"winner_units_left": 119
}, {
"buildings_left": 0,
"current_test_cycle": 2,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Hoverflop",
"tested_unit": "Laser Shell",
"winner": "AI",
"winner_units": [ {
"health": 474.029,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
} ],
"winner_units_left": 119
}, {
"buildings_left": 0,
"current_test_cycle": 2,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Octospike",
"tested_unit": "Laser Shell",
"winner": "AI",
"winner_units": [ {
"health": 1237.5,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
} ],
"winner_units_left": 119
}, {
"buildings_left": 0,
"current_test_cycle": 3,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Greaper",
"tested_unit": "Shuttle Carrier",
"winner": "AI",
"winner_units": [ {
"health": 1167.97,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
} ],
"winner_units_left": 119
}, {
"buildings_left": 0,
"current_test_cycle": 3,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Laser Dolphin",
"tested_unit": "Shuttle Carrier",
"winner": "AI",
"winner_units": [ {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
} ],
"winner_units_left": 117
}, {
"buildings_left": 0,
"current_test_cycle": 3,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Laser Shell",
"tested_unit": "Shuttle Carrier",
"winner": "AI",
"winner_units": [ {
"health": 260.366,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
} ],
"winner_units_left": 119
}, {
"buildings_left": 0,
"current_test_cycle": 3,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Shuttle Carrier",
"tested_unit": "Shuttle Carrier",
"winner": "AI",
"winner_units": [ {
"health": 681.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
} ],
"winner_units_left": 119
}, {
"buildings_left": 0,
"current_test_cycle": 3,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Caterflame",
"tested_unit": "Shuttle Carrier",
"winner": "AI",
"winner_units": [ {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 872.927,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
} ],
"winner_units_left": 118
}, {
"buildings_left": 0,
"current_test_cycle": 3,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Divine Spear",
"tested_unit": "Shuttle Carrier",
"winner": "AI",
"winner_units": [ {
"health": 788.133,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
} ],
"winner_units_left": 119
}, {
"buildings_left": 0,
"current_test_cycle": 3,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Flonine",
"tested_unit": "Shuttle Carrier",
"winner": "AI",
"winner_units": [ {
"health": 750.0,
"name": "Flonine"
}, {
"health": 550.07,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
} ],
"winner_units_left": 118
}, {
"buildings_left": 0,
"current_test_cycle": 3,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Flying Warrior",
"tested_unit": "Shuttle Carrier",
"winner": "AI",
"winner_units": [ {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 792.447,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
} ],
"winner_units_left": 118
}, {
"buildings_left": 0,
"current_test_cycle": 3,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Glidog",
"tested_unit": "Shuttle Carrier",
"winner": "AI",
"winner_units": [ {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 452.35,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
} ],
"winner_units_left": 116
}, {
"buildings_left": 0,
"current_test_cycle": 3,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Humming sabre",
"tested_unit": "Shuttle Carrier",
"winner": "AI",
"winner_units": [ {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 306.795,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
} ],
"winner_units_left": 115
}, {
"buildings_left": 0,
"current_test_cycle": 3,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Battle Bear",
"tested_unit": "Shuttle Carrier",
"winner": "AI",
"winner_units": [ {
"health": 730.449,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
} ],
"winner_units_left": 119
}, {
"buildings_left": 0,
"current_test_cycle": 3,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Percen",
"tested_unit": "Shuttle Carrier",
"winner": "AI",
"winner_units": [ {
"health": 400.0,
"name": "Percen"
}, {
"health": 391.674,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
} ],
"winner_units_left": 118
}, {
"buildings_left": 0,
"current_test_cycle": 3,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Bowshot",
"tested_unit": "Shuttle Carrier",
"winner": "AI",
"winner_units": [ {
"health": 235.083,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
} ],
"winner_units_left": 119
}, {
"buildings_left": 0,
"current_test_cycle": 3,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Clawrex",
"tested_unit": "Shuttle Carrier",
"winner": "AI",
"winner_units": [ {
"health": 420.679,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
} ],
"winner_units_left": 119
}, {
"buildings_left": 0,
"current_test_cycle": 3,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Drill",
"tested_unit": "Shuttle Carrier",
"winner": "AI",
"winner_units": [ {
"health": 642.506,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
} ],
"winner_units_left": 119
}, {
"buildings_left": 0,
"current_test_cycle": 3,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Farshot",
"tested_unit": "Shuttle Carrier",
"winner": "AI",
"winner_units": [ {
"health": 509.891,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
} ],
"winner_units_left": 119
}, {
"buildings_left": 0,
"current_test_cycle": 3,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Imtail",
"tested_unit": "Shuttle Carrier",
"winner": "AI",
"winner_units": [ {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 289.392,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
} ],
"winner_units_left": 116
}, {
"buildings_left": 0,
"current_test_cycle": 3,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Mechanic",
"tested_unit": "Shuttle Carrier",
"winner": "AI",
"winner_units": [ {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 313.135,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
} ],
"winner_units_left": 118
}, {
"buildings_left": 0,
"current_test_cycle": 3,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Rocket Moose",
"tested_unit": "Shuttle Carrier",
"winner": "AI",
"winner_units": [ {
"health": 572.291,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
} ],
"winner_units_left": 119
}, {
"buildings_left": 0,
"current_test_cycle": 3,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Gun bot",
"tested_unit": "Shuttle Carrier",
"winner": "AI",
"winner_units": [ {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
} ],
"winner_units_left": 117
}, {
"buildings_left": 0,
"current_test_cycle": 3,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Tank",
"tested_unit": "Shuttle Carrier",
"winner": "AI",
"winner_units": [ {
"health": 842.85,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
} ],
"winner_units_left": 119
}, {
"buildings_left": 0,
"current_test_cycle": 3,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Warrior",
"tested_unit": "Shuttle Carrier",
"winner": "AI",
"winner_units": [ {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
} ],
"winner_units_left": 118
}, {
"buildings_left": 0,
"current_test_cycle": 3,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Hoverflop",
"tested_unit": "Shuttle Carrier",
"winner": "AI",
"winner_units": [ {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 491.47,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
} ],
"winner_units_left": 118
}, {
"buildings_left": 0,
"current_test_cycle": 3,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Octospike",
"tested_unit": "Shuttle Carrier",
"winner": "AI",
"winner_units": [ {
"health": 1160.2,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
} ],
"winner_units_left": 119
}, {
"buildings_left": 0,
"current_test_cycle": 4,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Greaper",
"tested_unit": "Caterflame",
"winner": "AI",
"winner_units": [ {
"health": 1065.73,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
} ],
"winner_units_left": 119
}, {
"buildings_left": 0,
"current_test_cycle": 4,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Laser Dolphin",
"tested_unit": "Caterflame",
"winner": "AI",
"winner_units": [ {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 251.542,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
} ],
"winner_units_left": 118
}, {
"buildings_left": 0,
"current_test_cycle": 4,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Laser Shell",
"tested_unit": "Caterflame",
"winner": "AI",
"winner_units": [ {
"health": 398.395,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
} ],
"winner_units_left": 119
}, {
"buildings_left": 0,
"current_test_cycle": 4,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Shuttle Carrier",
"tested_unit": "Caterflame",
"winner": "AI",
"winner_units": [ {
"health": 893.963,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
} ],
"winner_units_left": 119
}, {
"buildings_left": 0,
"current_test_cycle": 4,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Caterflame",
"tested_unit": "Caterflame",
"winner": "AI",
"winner_units": [ {
"health": 643.221,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
} ],
"winner_units_left": 119
}, {
"buildings_left": 0,
"current_test_cycle": 4,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Divine Spear",
"tested_unit": "Caterflame",
"winner": "AI",
"winner_units": [ {
"health": 1112.5,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
} ],
"winner_units_left": 119
}, {
"buildings_left": 0,
"current_test_cycle": 4,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Flonine",
"tested_unit": "Caterflame",
"winner": "AI",
"winner_units": [ {
"health": 306.551,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
} ],
"winner_units_left": 119
}, {
"buildings_left": 0,
"current_test_cycle": 4,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Flying Warrior",
"tested_unit": "Caterflame",
"winner": "AI",
"winner_units": [ {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 756.909,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
} ],
"winner_units_left": 118
}, {
"buildings_left": 0,
"current_test_cycle": 4,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Glidog",
"tested_unit": "Caterflame",
"winner": "AI",
"winner_units": [ {
"health": 500.0,
"name": "Glidog"
}, {
"health": 279.232,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
} ],
"winner_units_left": 118
}, {
"buildings_left": 0,
"current_test_cycle": 4,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Humming sabre",
"tested_unit": "Caterflame",
"winner": "AI",
"winner_units": [ {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 309.563,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
} ],
"winner_units_left": 117
}, {
"buildings_left": 0,
"current_test_cycle": 4,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Battle Bear",
"tested_unit": "Caterflame",
"winner": "AI",
"winner_units": [ {
"health": 518.74,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
} ],
"winner_units_left": 119
}, {
"buildings_left": 0,
"current_test_cycle": 4,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Percen",
"tested_unit": "Caterflame",
"winner": "AI",
"winner_units": [ {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
} ],
"winner_units_left": 118
}, {
"buildings_left": 0,
"current_test_cycle": 4,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Bowshot",
"tested_unit": "Caterflame",
"winner": "AI",
"winner_units": [ {
"health": 219.995,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
} ],
"winner_units_left": 119
}, {
"buildings_left": 0,
"current_test_cycle": 4,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Clawrex",
"tested_unit": "Caterflame",
"winner": "AI",
"winner_units": [ {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
} ],
"winner_units_left": 118
}, {
"buildings_left": 0,
"current_test_cycle": 4,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Drill",
"tested_unit": "Caterflame",
"winner": "AI",
"winner_units": [ {
"health": 409.528,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
} ],
"winner_units_left": 119
}, {
"buildings_left": 0,
"current_test_cycle": 4,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Farshot",
"tested_unit": "Caterflame",
"winner": "AI",
"winner_units": [ {
"health": 539.824,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
} ],
"winner_units_left": 119
}, {
"buildings_left": 0,
"current_test_cycle": 4,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Imtail",
"tested_unit": "Caterflame",
"winner": "AI",
"winner_units": [ {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 254.285,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
} ],
"winner_units_left": 115
}, {
"buildings_left": 0,
"current_test_cycle": 4,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Mechanic",
"tested_unit": "Caterflame",
"winner": "AI",
"winner_units": [ {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 381.65,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
} ],
"winner_units_left": 117
}, {
"buildings_left": 0,
"current_test_cycle": 4,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Rocket Moose",
"tested_unit": "Caterflame",
"winner": "AI",
"winner_units": [ {
"health": 288.023,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
} ],
"winner_units_left": 119
}, {
"buildings_left": 0,
"current_test_cycle": 4,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Gun bot",
"tested_unit": "Caterflame",
"winner": "AI",
"winner_units": [ {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 176.182,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
} ],
"winner_units_left": 117
}, {
"buildings_left": 0,
"current_test_cycle": 4,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Tank",
"tested_unit": "Caterflame",
"winner": "AI",
"winner_units": [ {
"health": 737.283,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
} ],
"winner_units_left": 119
}, {
"buildings_left": 0,
"current_test_cycle": 4,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Warrior",
"tested_unit": "Caterflame",
"winner": "AI",
"winner_units": [ {
"health": 600.0,
"name": "Warrior"
}, {
"health": 495.168,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
} ],
"winner_units_left": 118
}, {
"buildings_left": 0,
"current_test_cycle": 4,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Hoverflop",
"tested_unit": "Caterflame",
"winner": "AI",
"winner_units": [ {
"health": 268.26,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
} ],
"winner_units_left": 119
}, {
"buildings_left": 0,
"current_test_cycle": 4,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Octospike",
"tested_unit": "Caterflame",
"winner": "AI",
"winner_units": [ {
"health": 1205.47,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
} ],
"winner_units_left": 119
}, {
"buildings_left": 0,
"current_test_cycle": 5,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Greaper",
"tested_unit": "Divine Spear",
"winner": "AI",
"winner_units": [ {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
} ],
"winner_units_left": 118
}, {
"buildings_left": 0,
"current_test_cycle": 5,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Laser Dolphin",
"tested_unit": "Divine Spear",
"winner": "AI",
"winner_units": [ {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
} ],
"winner_units_left": 116
}, {
"buildings_left": 0,
"current_test_cycle": 5,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Laser Shell",
"tested_unit": "Divine Spear",
"winner": "AI",
"winner_units": [ {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 598.052,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
} ],
"winner_units_left": 118
}, {
"buildings_left": 0,
"current_test_cycle": 5,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Shuttle Carrier",
"tested_unit": "Divine Spear",
"winner": "AI",
"winner_units": [ {
"health": 725.013,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
} ],
"winner_units_left": 119
}, {
"buildings_left": 0,
"current_test_cycle": 5,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Caterflame",
"tested_unit": "Divine Spear",
"winner": "AI",
"winner_units": [ {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
} ],
"winner_units_left": 118
}, {
"buildings_left": 0,
"current_test_cycle": 5,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Divine Spear",
"tested_unit": "Divine Spear",
"winner": "AI",
"winner_units": [ {
"health": 880.736,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
} ],
"winner_units_left": 119
}, {
"buildings_left": 0,
"current_test_cycle": 5,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Flonine",
"tested_unit": "Divine Spear",
"winner": "AI",
"winner_units": [ {
"health": 750.0,
"name": "Flonine"
}, {
"health": 558.532,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
} ],
"winner_units_left": 118
}, {
"buildings_left": 0,
"current_test_cycle": 5,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Flying Warrior",
"tested_unit": "Divine Spear",
"winner": "AI",
"winner_units": [ {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
} ],
"winner_units_left": 117
}, {
"buildings_left": 0,
"current_test_cycle": 5,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Glidog",
"tested_unit": "Divine Spear",
"winner": "AI",
"winner_units": [ {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
} ],
"winner_units_left": 116
}, {
"buildings_left": 0,
"current_test_cycle": 5,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Humming sabre",
"tested_unit": "Divine Spear",
"winner": "AI",
"winner_units": [ {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 367.294,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
} ],
"winner_units_left": 115
}, {
"buildings_left": 0,
"current_test_cycle": 5,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Battle Bear",
"tested_unit": "Divine Spear",
"winner": "AI",
"winner_units": [ {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 814.062,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
} ],
"winner_units_left": 118
}, {
"buildings_left": 0,
"current_test_cycle": 5,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Percen",
"tested_unit": "Divine Spear",
"winner": "AI",
"winner_units": [ {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
} ],
"winner_units_left": 117
}, {
"buildings_left": 0,
"current_test_cycle": 5,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Bowshot",
"tested_unit": "Divine Spear",
"winner": "AI",
"winner_units": [ {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 431.537,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
} ],
"winner_units_left": 118
}, {
"buildings_left": 0,
"current_test_cycle": 5,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Clawrex",
"tested_unit": "Divine Spear",
"winner": "AI",
"winner_units": [ {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 243.787,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
} ],
"winner_units_left": 118
}, {
"buildings_left": 0,
"current_test_cycle": 5,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Drill",
"tested_unit": "Divine Spear",
"winner": "AI",
"winner_units": [ {
"health": 850.0,
"name": "Drill"
}, {
"health": 727.769,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
} ],
"winner_units_left": 118
}, {
"buildings_left": 0,
"current_test_cycle": 5,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Farshot",
"tested_unit": "Divine Spear",
"winner": "AI",
"winner_units": [ {
"health": 153.247,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
} ],
"winner_units_left": 119
}, {
"buildings_left": 0,
"current_test_cycle": 5,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Imtail",
"tested_unit": "Divine Spear",
"winner": "AI",
"winner_units": [ {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 233.57,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
} ],
"winner_units_left": 113
}, {
"buildings_left": 0,
"current_test_cycle": 5,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Mechanic",
"tested_unit": "Divine Spear",
"winner": "AI",
"winner_units": [ {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 218.801,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
} ],
"winner_units_left": 116
}, {
"buildings_left": 0,
"current_test_cycle": 5,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Rocket Moose",
"tested_unit": "Divine Spear",
"winner": "AI",
"winner_units": [ {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 610.755,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
} ],
"winner_units_left": 118
}, {
"buildings_left": 0,
"current_test_cycle": 5,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Gun bot",
"tested_unit": "Divine Spear",
"winner": "AI",
"winner_units": [ {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 303.488,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
} ],
"winner_units_left": 115
}, {
"buildings_left": 0,
"current_test_cycle": 5,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Tank",
"tested_unit": "Divine Spear",
"winner": "AI",
"winner_units": [ {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
} ],
"winner_units_left": 118
}, {
"buildings_left": 0,
"current_test_cycle": 5,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Warrior",
"tested_unit": "Divine Spear",
"winner": "AI",
"winner_units": [ {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 438.611,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
} ],
"winner_units_left": 117
}, {
"buildings_left": 0,
"current_test_cycle": 5,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Hoverflop",
"tested_unit": "Divine Spear",
"winner": "AI",
"winner_units": [ {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 573.102,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
} ],
"winner_units_left": 118
}, {
"buildings_left": 0,
"current_test_cycle": 5,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Octospike",
"tested_unit": "Divine Spear",
"winner": "AI",
"winner_units": [ {
"health": 1168.46,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
} ],
"winner_units_left": 119
}, {
"buildings_left": 0,
"current_test_cycle": 6,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Greaper",
"tested_unit": "Flonine",
"winner": "AI",
"winner_units": [ {
"health": 1171.88,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
} ],
"winner_units_left": 119
}, {
"buildings_left": 0,
"current_test_cycle": 6,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Laser Dolphin",
"tested_unit": "Flonine",
"winner": "AI",
"winner_units": [ {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 362.663,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
} ],
"winner_units_left": 118
}, {
"buildings_left": 0,
"current_test_cycle": 6,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Laser Shell",
"tested_unit": "Flonine",
"winner": "AI",
"winner_units": [ {
"health": 527.806,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
} ],
"winner_units_left": 119
}, {
"buildings_left": 0,
"current_test_cycle": 6,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Shuttle Carrier",
"tested_unit": "Flonine",
"winner": "AI",
"winner_units": [ {
"health": 953.125,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
} ],
"winner_units_left": 119
}, {
"buildings_left": 0,
"current_test_cycle": 6,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Caterflame",
"tested_unit": "Flonine",
"winner": "AI",
"winner_units": [ {
"health": 771.288,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
} ],
"winner_units_left": 119
}, {
"buildings_left": 0,
"current_test_cycle": 6,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Divine Spear",
"tested_unit": "Flonine",
"winner": "AI",
"winner_units": [ {
"health": 1200.06,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
} ],
"winner_units_left": 119
}, {
"buildings_left": 0,
"current_test_cycle": 6,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Flonine",
"tested_unit": "Flonine",
"winner": "AI",
"winner_units": [ {
"health": 547.818,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
} ],
"winner_units_left": 119
}, {
"buildings_left": 0,
"current_test_cycle": 6,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Flying Warrior",
"tested_unit": "Flonine",
"winner": "AI",
"winner_units": [ {
"health": 360.665,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
} ],
"winner_units_left": 119
}, {
"buildings_left": 0,
"current_test_cycle": 6,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Glidog",
"tested_unit": "Flonine",
"winner": "AI",
"winner_units": [ {
"health": 500.0,
"name": "Glidog"
}, {
"health": 461.569,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
} ],
"winner_units_left": 118
}, {
"buildings_left": 0,
"current_test_cycle": 6,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Humming sabre",
"tested_unit": "Flonine",
"winner": "AI",
"winner_units": [ {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 134.668,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
} ],
"winner_units_left": 118
}, {
"buildings_left": 0,
"current_test_cycle": 6,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Battle Bear",
"tested_unit": "Flonine",
"winner": "AI",
"winner_units": [ {
"health": 712.5,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
} ],
"winner_units_left": 119
}, {
"buildings_left": 0,
"current_test_cycle": 6,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Percen",
"tested_unit": "Flonine",
"winner": "AI",
"winner_units": [ {
"health": 160.837,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
} ],
"winner_units_left": 119
}, {
"buildings_left": 0,
"current_test_cycle": 6,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Bowshot",
"tested_unit": "Flonine",
"winner": "AI",
"winner_units": [ {
"health": 368.749,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
} ],
"winner_units_left": 119
}, {
"buildings_left": 0,
"current_test_cycle": 6,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Clawrex",
"tested_unit": "Flonine",
"winner": "AI",
"winner_units": [ {
"health": 345.604,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
} ],
"winner_units_left": 119
}, {
"buildings_left": 0,
"current_test_cycle": 6,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Drill",
"tested_unit": "Flonine",
"winner": "AI",
"winner_units": [ {
"health": 633.373,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
} ],
"winner_units_left": 119
}, {
"buildings_left": 0,
"current_test_cycle": 6,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Farshot",
"tested_unit": "Flonine",
"winner": "AI",
"winner_units": [ {
"health": 624.012,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
} ],
"winner_units_left": 119
}, {
"buildings_left": 0,
"current_test_cycle": 6,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Imtail",
"tested_unit": "Flonine",
"winner": "AI",
"winner_units": [ {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 262.588,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
} ],
"winner_units_left": 116
}, {
"buildings_left": 0,
"current_test_cycle": 6,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Mechanic",
"tested_unit": "Flonine",
"winner": "AI",
"winner_units": [ {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 253.819,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
} ],
"winner_units_left": 118
}, {
"buildings_left": 0,
"current_test_cycle": 6,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Rocket Moose",
"tested_unit": "Flonine",
"winner": "AI",
"winner_units": [ {
"health": 586.545,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
} ],
"winner_units_left": 119
}, {
"buildings_left": 0,
"current_test_cycle": 6,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Gun bot",
"tested_unit": "Flonine",
"winner": "AI",
"winner_units": [ {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
}, {
"health": 400.0,
"name": "Gun bot"
} ],
"winner_units_left": 117
}, {
"buildings_left": 0,
"current_test_cycle": 6,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Tank",
"tested_unit": "Flonine",
"winner": "AI",
"winner_units": [ {
"health": 843.75,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
}, {
"health": 1000.0,
"name": "Tank"
} ],
"winner_units_left": 119
}, {
"buildings_left": 0,
"current_test_cycle": 6,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Warrior",
"tested_unit": "Flonine",
"winner": "AI",
"winner_units": [ {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
}, {
"health": 600.0,
"name": "Warrior"
} ],
"winner_units_left": 118
}, {
"buildings_left": 0,
"current_test_cycle": 6,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Hoverflop",
"tested_unit": "Flonine",
"winner": "AI",
"winner_units": [ {
"health": 529.174,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
}, {
"health": 750.0,
"name": "Hoverflop"
} ],
"winner_units_left": 119
}, {
"buildings_left": 0,
"current_test_cycle": 6,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Octospike",
"tested_unit": "Flonine",
"winner": "AI",
"winner_units": [ {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
}, {
"health": 1250.0,
"name": "Octospike"
} ],
"winner_units_left": 119
}, {
"buildings_left": 0,
"current_test_cycle": 7,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Greaper",
"tested_unit": "Flying Warrior",
"winner": "AI",
"winner_units": [ {
"health": 1137.52,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
}, {
"health": 1250.0,
"name": "Greaper"
} ],
"winner_units_left": 119
}, {
"buildings_left": 0,
"current_test_cycle": 7,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Laser Dolphin",
"tested_unit": "Flying Warrior",
"winner": "AI",
"winner_units": [ {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 314.702,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
}, {
"health": 400.0,
"name": "Laser Dolphin"
} ],
"winner_units_left": 118
}, {
"buildings_left": 0,
"current_test_cycle": 7,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Laser Shell",
"tested_unit": "Flying Warrior",
"winner": "AI",
"winner_units": [ {
"health": 442.44,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
}, {
"health": 650.0,
"name": "Laser Shell"
} ],
"winner_units_left": 119
}, {
"buildings_left": 0,
"current_test_cycle": 7,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Shuttle Carrier",
"tested_unit": "Flying Warrior",
"winner": "AI",
"winner_units": [ {
"health": 917.969,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
}, {
"health": 1000.0,
"name": "Shuttle Carrier"
} ],
"winner_units_left": 119
}, {
"buildings_left": 0,
"current_test_cycle": 7,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Caterflame",
"tested_unit": "Flying Warrior",
"winner": "AI",
"winner_units": [ {
"health": 824.516,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
}, {
"health": 900.0,
"name": "Caterflame"
} ],
"winner_units_left": 119
}, {
"buildings_left": 0,
"current_test_cycle": 7,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Divine Spear",
"tested_unit": "Flying Warrior",
"winner": "AI",
"winner_units": [ {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
}, {
"health": 1250.0,
"name": "Divine Spear"
} ],
"winner_units_left": 119
}, {
"buildings_left": 0,
"current_test_cycle": 7,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Flonine",
"tested_unit": "Flying Warrior",
"winner": "AI",
"winner_units": [ {
"health": 611.89,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
}, {
"health": 750.0,
"name": "Flonine"
} ],
"winner_units_left": 119
}, {
"buildings_left": 0,
"current_test_cycle": 7,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Flying Warrior",
"tested_unit": "Flying Warrior",
"winner": "AI",
"winner_units": [ {
"health": 561.594,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
}, {
"health": 800.0,
"name": "Flying Warrior"
} ],
"winner_units_left": 119
}, {
"buildings_left": 0,
"current_test_cycle": 7,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Glidog",
"tested_unit": "Flying Warrior",
"winner": "AI",
"winner_units": [ {
"health": 108.097,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
}, {
"health": 500.0,
"name": "Glidog"
} ],
"winner_units_left": 119
}, {
"buildings_left": 0,
"current_test_cycle": 7,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Humming sabre",
"tested_unit": "Flying Warrior",
"winner": "AI",
"winner_units": [ {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 342.804,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
}, {
"health": 400.0,
"name": "Humming sabre"
} ],
"winner_units_left": 118
}, {
"buildings_left": 0,
"current_test_cycle": 7,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Battle Bear",
"tested_unit": "Flying Warrior",
"winner": "AI",
"winner_units": [ {
"health": 681.25,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
}, {
"health": 900.0,
"name": "Battle Bear"
} ],
"winner_units_left": 119
}, {
"buildings_left": 0,
"current_test_cycle": 7,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Percen",
"tested_unit": "Flying Warrior",
"winner": "AI",
"winner_units": [ {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
}, {
"health": 400.0,
"name": "Percen"
} ],
"winner_units_left": 118
}, {
"buildings_left": 0,
"current_test_cycle": 7,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Bowshot",
"tested_unit": "Flying Warrior",
"winner": "AI",
"winner_units": [ {
"health": 344.904,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
}, {
"health": 500.0,
"name": "Bowshot"
} ],
"winner_units_left": 119
}, {
"buildings_left": 0,
"current_test_cycle": 7,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Clawrex",
"tested_unit": "Flying Warrior",
"winner": "AI",
"winner_units": [ {
"health": 121.27,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
}, {
"health": 700.0,
"name": "Clawrex"
} ],
"winner_units_left": 119
}, {
"buildings_left": 0,
"current_test_cycle": 7,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Drill",
"tested_unit": "Flying Warrior",
"winner": "AI",
"winner_units": [ {
"health": 549.629,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
}, {
"health": 850.0,
"name": "Drill"
} ],
"winner_units_left": 119
}, {
"buildings_left": 0,
"current_test_cycle": 7,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Farshot",
"tested_unit": "Flying Warrior",
"winner": "AI",
"winner_units": [ {
"health": 589.44,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
}, {
"health": 650.0,
"name": "Farshot"
} ],
"winner_units_left": 119
}, {
"buildings_left": 0,
"current_test_cycle": 7,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Imtail",
"tested_unit": "Flying Warrior",
"winner": "AI",
"winner_units": [ {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 232.357,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
}, {
"health": 300.0,
"name": "Imtail"
} ],
"winner_units_left": 116
}, {
"buildings_left": 0,
"current_test_cycle": 7,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Mechanic",
"tested_unit": "Flying Warrior",
"winner": "AI",
"winner_units": [ {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 79.4072,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
}, {
"health": 450.0,
"name": "Mechanic"
} ],
"winner_units_left": 118
}, {
"buildings_left": 0,
"current_test_cycle": 7,
"duration": 1,
"end_turn": 2,
"enemies_needed": 0,
"level": 1,
"losers_units_left": 0,
"tested_enemy": "Rocket Moose",
"tested_unit": "Flying Warrior",
"winner": "AI",
"winner_units": [ {
"health": 471.875,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
"name": "Rocket Moose"
}, {
"health": 800.0,
}, {
}, {
}, {