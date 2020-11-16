# Copyright (c) 2020 Celestial Games BV.
# This file is part of Ariap Wars and subject to the terms and conditions defined in file 'LICENSE',
# which is part of this source code package.

extends Node


# Preloaded scenes
var gameboard_scene : PackedScene = preload("res://Game/GameBoard.tscn")
var TurnManager : PackedScene = preload("res://Game/TurnManager.tscn")
var AI : PackedScene = preload("res://Commanders/AI.tscn")
var Human : PackedScene = preload("res://Commanders/Human.tscn")

var camera

# Debug
var all_outcomes = []
var game_boards = []

########################################
# Efficiency Section
# Used to cut down the number of possibilities (redundancies, impossible moves etc)
# Before actually calculating moves
########################################

# Get combination of different lists
func get_combination(input):

	var variation = []
	var first_var = input[0]
	
	if input.size() == 1:
		variation.append(first_var)

		return variation
		
	var second_var
	var temp_list

	if input.size() > 2:
		input.pop_front()
		second_var = get_combination(input)

		for i in first_var:
			for j in second_var:
				temp_list = []
				temp_list.append(i)
				for k in j: temp_list.append(k)
				variation.append(temp_list)

	else :
		for i in first_var:
			for j in input[1]:
				temp_list = []
				temp_list.append(i)
				temp_list.append(j)
				variation.append(temp_list)

	return variation

# Get all possible combinations of a move set
func get_combinations(unit_buildings):
	# Calculate all variations of the calculated moves
	
	var moves_only = []
	for unit in unit_buildings:
		moves_only.append(unit.moves)
		
	var all_moves_variations = []
	if len(unit_buildings) > 1:
		for variation in get_combination(moves_only): 
			all_moves_variations.append(variation)
	else:
		for move in unit_buildings[0].moves:
			all_moves_variations.append([move])
	
	var all_complete_variations = []
	for move_variation in all_moves_variations:
		var turn_variation = []
		for unit in range(len(move_variation)):
			var complete_variation =  {
				"unit" : unit_buildings[unit].unit,
				"moves" : move_variation[unit],
				"duplicate_danger" :  unit_buildings[unit].duplicate_danger
			}
			turn_variation.append(complete_variation)
		all_complete_variations.append(turn_variation)

	return check_unique(all_complete_variations)

# Check whether all variations have unique moves, meaning that moves of different units do not overlap,
# causing a unit not being able to move due to the move of a preceding unit
func check_unique(variations):
	var index_to_remove = []
	
	if len(variations) > 10:
		
		for variation_index in range(len(variations)):
			var variation = variations[variation_index]
			variation.sort_custom(SortingClass, "sort_move_options")
			var converted_var = {
				"duplicate" : false,
				"list" : []
			}
			
			# Before we remove the duplicates we merge the moves and convert it
			# to a more useful dictionary
			for sub in variation:
				var converted
				if sub.moves.sim_battles.move_type == AllEnums.AI_MOVE_TYPE.HUNT_FLEE:
					converted = {
						"unit" : sub.unit,
						"all" : sub.moves.new_zone
					}
				else:
					converted = {
						"unit" : sub.unit,
						"all" : merge_moves(sub.moves.retal, sub.moves.non_retal)
					}
				converted_var.list.append(converted)
			
			var converted_without_dup = remove_duplicates(converted_var)
			
			# If the variation has a duplicate which is the last option
			# of 1 or more units, it should be removed from the possibilies
			if converted_without_dup.duplicate:
				index_to_remove.append(variation_index)
				# remove from list
			# If not, the duplicates can be removed from the move sets of the units
			else:
				for i in range(len(variation)):
					if variation[i].unit == converted_without_dup.list[i].unit:
						if variation[i].moves.sim_battles.move_type == AllEnums.AI_MOVE_TYPE.ATTACK:
							# remove non retal duplicates
							if len(variation[i].moves.non_retal) > 0:
								var non_retal_to_remove = []
								for j in range(len(variation[i].moves.non_retal)):
									if not variation[i].moves.non_retal[j] in converted_without_dup.list[i].all:
										non_retal_to_remove.append(j)
								non_retal_to_remove.invert()
								for k in non_retal_to_remove:
									variation[i].moves.non_retal.remove(k)
									
							# remove retal duplicates
							if len(variation[i].moves.retal) > 0:
								var retal_to_remove = []
								for j in range(len(variation[i].moves.retal)):
									if not variation[i].moves.retal[j] in converted_without_dup.list[i].all:
										retal_to_remove.append(j)
								retal_to_remove.invert()
								for k in retal_to_remove:
									variation[i].moves.retal.remove(k)
			
		# Remove found
		variations = remove_indexes(variations, index_to_remove)
		index_to_remove = []
#
	if len(variations) > 10:
		# Remove duplicate kills
		for variation_index in range(len(variations)):
			var variation = variations[variation_index]
			var all_kills = []
			var unique_kills = []

			for unit in variation:
				if unit.moves.sim_battles.move_type == AllEnums.AI_MOVE_TYPE.ATTACK:
					if unit.moves.sim_battles.battle_outcome == AllEnums.BATTLE_OUTCOMES.ENEMY_DEAD:
						all_kills.append(unit.moves.enemy)

			if len(all_kills) > 0:
				var enemy_commander = all_kills[0].commander
				for kill in all_kills:
					if not kill in unique_kills:
						unique_kills.append(kill)
				if len(all_kills) > len(unique_kills):
					var enemy_team_size = enemy_commander.current_buildings.size() + enemy_commander.current_units.size()
					if enemy_team_size > len(unique_kills):
						index_to_remove.append(variation_index)

		# Remove found
		variations = remove_indexes(variations, index_to_remove)
		index_to_remove = []

	if len(variations) > 10:
	# Remove Attacks that would overkill the enemy
		for variation_index in range(len(variations)):
			var variation = variations[variation_index]

			var dup_enemies := {}
			for unit_variation in variation:
				if unit_variation.moves.sim_battles.move_type == AllEnums.AI_MOVE_TYPE.ATTACK:
					var enemy_key = unit_variation.moves.enemy.unit_name
					if !dup_enemies.has(enemy_key):
						dup_enemies[enemy_key] = [unit_variation]
					else:
						dup_enemies[enemy_key].append(unit_variation)

			# Check all dup enemies if the length is bigger than 1
			# if so check if it's going to be over killed
			# if so, remove from list
			if dup_enemies.size() > 0:
				for key in dup_enemies:
					if len(dup_enemies[key]) > 1:
						var all_atks = []
						var enemy_health = dup_enemies[key][0].moves.enemy.health_left
						for unit_variation in dup_enemies[key]:
							all_atks.append(unit_variation.moves.sim_battles.mod_atk)

						# Get all combinations while leaving out one, if one of them
						# is more than the combined atk, remove the whole variation
						for atk in range(len(all_atks)):
							var combined_atk = 0
							for j in range(len(all_atks)):
								if atk != j:
									combined_atk += all_atks[j]
							if combined_atk >= enemy_health:
								index_to_remove.append(variation_index)
								break

		# Remove found
		variations = remove_indexes(variations, index_to_remove)
		index_to_remove = []

	return variations
	

# Remove given indexes
func remove_indexes(variations, index_to_remove):
	if len(index_to_remove) < len(variations):
			index_to_remove.invert()
			
			for i in index_to_remove:
				variations.remove(i)

	return variations

# Remove duplicate moves which can possibly prohibit units to move
# due to a move of a preceding unit
func remove_duplicates(variations):
	var all = []
	for unit in variations.list:
		for i in unit.all:
			all.append(i)
			
	# Get all the unique and duplicate moves
	var unique = []
	var duplicate = []
	for i in all:
		if not i in unique:
			unique.append(i)
		else:
			duplicate.append(i)
	
	for j in duplicate:
		if !variations.duplicate:
			var dup_counter = 0
			for unit  in variations.list:
				if j in unit.all and len(unit.all) > 1:
					unit.all.erase(j)
					break
				if j in unit.all and len(unit.all) <= 1:
					dup_counter +=1
				if dup_counter > 1:
					variations.duplicate = true
		else:
			break

	return variations


# Merge the movs of both non retal and retal
func merge_moves(non_retal, retal):
	var merged_moves = []
	for move in non_retal:
		merged_moves.append(move)
	for move in retal:
		merged_moves.append(move)
		
	return merged_moves

func cut_moves(calc_move_team):
	var cut = 0
	
	# Cut when there are less than 10 units
	if len(calc_move_team) <= 9 and len(calc_move_team) >= 6:
		cut = 2
	elif len(calc_move_team) == 5:
		cut = 3
	elif len(calc_move_team) == 4:
		cut = 4
	elif len(calc_move_team) == 3:
		cut = 8
	elif len(calc_move_team) == 2:
		cut = 22
	elif len(calc_move_team) > 9:
		var lower_cut = len(calc_move_team) - 9
		cut = 2
		for move in range(len(calc_move_team)):
			if move < lower_cut:
				calc_move_team[move].moves =  [calc_move_team[move].moves[0]]
				
	if cut > 0:
		for move in calc_move_team:
			if len(move.moves) > cut:
				move.moves = move.moves.slice(0, cut-1)

	return calc_move_team

########################################
# Calculation section
# Using Minimax to calculate future states to pick the next move
########################################

# DEBUG
var boards = 0
# minimax algorithm to get the best possible move for the AI
func minimax(dict: Dictionary):
	var game_board = dict.game_board
	var move_list = dict.move_list
	var depth = dict.depth
	var alpha = dict.alpha
	var beta = dict.beta
	var max_player = dict.max_player 
	# Return the value of the situation when your at the bottom of the decision tree
	if depth == 0:
		var final_score = calc_situation_value(game_board, max_player)
		var final_move = {
			"move" : move_list,
			"score" : final_score
		}
		all_outcomes.append(final_move.score)
		return final_move
		
	if max_player:
		var max_move = {
			"move" : move_list[0],
			"score" :  -INF
		}

		for child in move_list:
			
			# Create new world
			var new_game_board = create_temp_gb(game_board, child, true, depth)
			var eval
			
			# Calculate new moves and go one step deeper
			if depth > 1:
				var end = check_end(new_game_board, child)
				if end != null:
					eval = end
					
				else:
					var new_gb_dict = {
						"new_game_board": new_game_board,
						"max_player" : false
					}
#					var thread = Thread.new()
#					thread.start(self,"calc_new_moves", new_gb_dict)
#					var new_move_list = thread.wait_to_finish()
					var new_move_list = calc_new_moves(new_gb_dict)
					
					
					var new_dict = {
						"game_board" : new_game_board,
						"move_list" : new_move_list,
						"depth" : depth-1,
						"alpha" : alpha,
						"beta" : beta,
						"max_player" : false
					}
					
					eval = minimax(new_dict)
			else:
				
				var new_dict = {
					"game_board" : new_game_board,
					"move_list" : child,
					"depth" : depth-1,
					"alpha" : alpha,
					"beta" : beta,
					"max_player" : false
					}
				
				eval = minimax(new_dict)
			
			# Check what the best option and compare to alpha
			if eval.score >= max_move.score:
				max_move.score = eval.score
				max_move.move = child
				
			if eval.score >= alpha.score:
				alpha.score = eval.score
				alpha.move = child
			
			if beta.score <= alpha.score:
				break
		return max_move
		
	else:
		var min_move = {
			"move" : move_list[0],
			"score" :  INF
		}
		for child in move_list:
			
			# Create new world
			var new_game_board = create_temp_gb(game_board, child, false, depth)
			var eval
			
			# Calculate new moves and go one step deeper
			if depth > 1:
				var end = check_end(new_game_board, child)
				if end != null:
					eval = end
				else:
					
					var new_gb_dict = {
						"new_game_board": new_game_board,
						"max_player" : true
					}
					var thread = Thread.new()
					thread.start(self,"calc_new_moves", new_gb_dict)
					var new_move_list = thread.wait_to_finish()
#					var new_move_list = calc_new_moves(new_gb_dict)
					
					
					var new_dict = {
						"game_board" : new_game_board,
						"move_list" : new_move_list,
						"depth" : depth-1,
						"alpha" : alpha,
						"beta" : beta,
						"max_player" : false
					}
					eval = minimax(new_dict)
			else:
				var new_dict = {
					"game_board" : new_game_board,
					"move_list" : child,
					"depth" : depth-1,
					"alpha" : alpha,
					"beta" : beta,
					"max_player" : true
					}
				eval = minimax(new_dict)
			
			# Check what the worst option and compare to beta
			if eval.score <= min_move.score:
				min_move.score = eval.score
				min_move.move = child
			
			if eval.score <= beta.score:
				beta.score = eval.score
				beta.move = child
			
			if beta.score <= alpha.score:
				break
		return min_move

# Check whether the game has come to an end
func check_end(game_board, move_list):
	var human_units = len(game_board.new_TurnManager.players_in_game[0].current_units)
	var AI_units = len(game_board.new_TurnManager.players_in_game[1].current_units)
	if len(game_board.new_TurnManager.players_in_game[0].current_units) == 0:
		var final_move = {
			"move" : move_list,
			"score" : INF
		}
		all_outcomes.append(final_move.score)
		return final_move
		
	if len(game_board.new_TurnManager.players_in_game[1].current_units) == 0:
		var final_move = {
			"move" : move_list,
			"score" : -INF
		}
		all_outcomes.append(final_move.score)
		return final_move
	return null

# Manually create a new temporary gameboard for the simulation
func create_temp_gb(old_gameboard: Gameboard, last_turn_moves, max_player, depth):
	var new_gameboard = gameboard_scene.instance()
	game_boards.append(new_gameboard)
	boards += 1
	
	# Grid and obstacles
	new_gameboard.grid_size = old_gameboard.grid_size
	new_gameboard.max_x = old_gameboard.max_x
	new_gameboard.max_y = old_gameboard.max_y
	
	for arr in old_gameboard.grid:
		var new_grid = []
		for pos in arr:
			new_grid.append(pos)
		new_gameboard.grid.append(new_grid)
	
	
	new_gameboard.ground_obstacles = old_gameboard.ground_obstacles
	new_gameboard.water_obstacles = old_gameboard.water_obstacles
	new_gameboard.air_obstacles = old_gameboard.air_obstacles
	new_gameboard.impassable = old_gameboard.impassable
	new_gameboard.impassable_extra = old_gameboard.impassable_extra
	new_gameboard.astar_node_ground = old_gameboard.astar_node_ground
	new_gameboard.astar_node_water = old_gameboard.astar_node_water
	new_gameboard.astar_node_air = old_gameboard.astar_node_air

	# Turn manager
	var old_turn_manager = old_gameboard.new_TurnManager
	new_gameboard.new_TurnManager = TurnManager.instance()
	new_gameboard.add_child(new_gameboard.new_TurnManager)

	# Commanders
	var old_AI = old_gameboard.new_AI
	new_gameboard.new_AI = AI.instance()
	new_gameboard.add_child(new_gameboard.new_AI)
	new_gameboard.new_AI.game_board = new_gameboard
	new_gameboard.new_AI.turn_manager = new_gameboard.new_TurnManager
	new_gameboard.new_AI.commander_name = old_AI.commander_name
	new_gameboard.new_AI.team_income = old_AI.team_income
	new_gameboard.new_AI.team_money = old_AI.team_money
	new_gameboard.new_AI.team_starting_value = old_AI.team_starting_value

	
	var old_human = old_gameboard.new_Human
	new_gameboard.new_Human = Human.instance()
	new_gameboard.add_child(new_gameboard.new_Human)
	new_gameboard.new_Human.game_board = new_gameboard
	new_gameboard.new_Human.turn_manager = new_gameboard.new_TurnManager
	new_gameboard.new_Human.commander_name = old_human.commander_name
	new_gameboard.new_Human.team_income = old_human.team_income
	new_gameboard.new_Human.team_money = old_human.team_money
	new_gameboard.new_Human.team_starting_value = old_human.team_starting_value

	# Prepare Turn manager
	new_gameboard.new_TurnManager.players_in_game.append(new_gameboard.new_Human)
	new_gameboard.new_TurnManager.players_in_game.append(new_gameboard.new_AI)
	if old_turn_manager.current_player.commander_name == "Human":
		new_gameboard.new_TurnManager.current_player = new_gameboard.new_TurnManager.players_in_game[0]
		new_gameboard.new_TurnManager.other_player = new_gameboard.new_TurnManager.players_in_game[1]
	else:
		new_gameboard.new_TurnManager.current_player = new_gameboard.new_TurnManager.players_in_game[1]
		new_gameboard.new_TurnManager.other_player = new_gameboard.new_TurnManager.players_in_game[0]
	new_gameboard.new_TurnManager.current_player.activate_units(true)
	
	# Add and place all the units
	for player in old_turn_manager.players_in_game:
		for unit in player.current_units:
			var new_unit = UnitPicker.find_unit(unit.character_class_enum).instance()

			new_unit.current_player = new_gameboard.new_TurnManager.current_player
			new_unit.other_player = new_gameboard.new_TurnManager.other_player
			new_unit.game_board = new_gameboard
			new_unit.position = unit.position
			new_unit.current_pos = unit.current_pos
			new_unit.current_pos_map = unit.current_pos_map
			new_unit.health_left = unit.health_left
			new_unit.type = unit.type
			new_unit.has_moved = false
			new_unit.sim = true
			
			new_gameboard.add_child(new_unit)
			if new_unit.type == AllEnums.CELL_TYPES.UNIT:
				new_gameboard.grid[new_unit.current_pos_map.x][new_unit.current_pos_map.y] = AllEnums.CELL_TYPES.UNIT
				if player.commander_name == "Human":
					new_gameboard.new_Human.current_units.append(new_unit)
					new_unit.commander = new_gameboard.new_Human
				else:
					new_gameboard.new_AI.current_units.append(new_unit)
					new_unit.commander = new_gameboard.new_AI

	var new_atk_units
	
	if max_player:
		new_atk_units = new_gameboard.new_AI.current_units
	else:
		new_atk_units = new_gameboard.new_Human.current_units

	# Execute moves for units
	# TODO Move only and hunt flee might not work yet
	for i in range(len(new_atk_units), 0, -1):
		var current_unit = new_atk_units[i-1]
#	for current_unit in new_atk_units:
		for old_unit in last_turn_moves:
			if current_unit.position == old_unit.unit.position:
				var move_type = old_unit.moves.sim_battles.move_type
				
				match move_type:
					AllEnums.AI_MOVE_TYPE.ATTACK:
						execute_attack(old_unit, new_gameboard, true, current_unit)
					AllEnums.AI_MOVE_TYPE.MOVE_ONLY:
						execute_move_only(old_unit, new_gameboard, true, current_unit)
					AllEnums.AI_MOVE_TYPE.HUNT_FLEE:
						execute_hunt_flee(old_unit, new_gameboard, true, current_unit)
	
	new_gameboard.new_TurnManager.next_player()
	return new_gameboard

# Calculate the new moves during simulation
func calc_new_moves(dict: Dictionary):
	var new_gameboard = dict.new_game_board
	var max_player = dict.max_player
	var enemy
	
	var calc_move_all_units_and_buildings = []
	var current_units = []
	var current_buildings = []
	
	if max_player:
		current_units = new_gameboard.new_AI.current_units
		current_buildings = new_gameboard.new_AI.current_buildings
		enemy = new_gameboard.new_Human
	else:
		current_units = new_gameboard.new_Human.current_units
		current_buildings = new_gameboard.new_Human.current_buildings
		enemy = new_gameboard.new_AI
	
	# Calculate moves for all units and buildings
	for unit in current_units:
		calc_move_all_units_and_buildings.append(unit.total_move_calc())
	
	for building in current_buildings:
		calc_move_all_units_and_buildings.append(building.total_move_calc())
	
	var calc_move_all_units_and_buildings2 = cut_moves(calc_move_all_units_and_buildings)
	
	var all_complete_variations = get_combinations(calc_move_all_units_and_buildings2)

	return all_complete_variations

# Calculate the value of a move
func calc_situation_value(game_board: Gameboard, max_player: bool):
	var total_score = 0

	for commander in game_board.new_TurnManager.players_in_game:
		var situation_score = 0
		for unit in commander.current_units:
			situation_score += unit.health_left / unit.starting_health
			
		for building in commander.current_buildings:
			situation_score += building.health_left / building.starting_health
		
		var final_score = situation_score / commander.team_starting_value
		
		if total_score != 0:
			total_score += final_score
		else:
			total_score -= final_score

	return total_score

########################################
# Action section
# Execute or simulate actions
########################################

# Execute an attack
func execute_attack(calc_move: Dictionary, game_board: Gameboard, simulate: bool, new_unit: Unit) -> void:
	var unit = null
	if simulate and new_unit != null:
		unit = new_unit
	else:
		unit = calc_move.unit
	
	var unit_moves = calc_move.moves
	var enemy = null
	var end_move
	
	# Activate unit
	unit.is_clicked = true
	game_board.active_unit = unit
	unit.possibilities = game_board.show_possiblities(unit, AllEnums.MOVEMENT_TYPES.MOVE, [])
	
	# Find move to execute
	if !unit.has_moved or (simulate and unit.has_moved):
		if simulate:
			for new_enemy in game_board.new_TurnManager.other_player.current_units:
				if new_enemy.position == unit_moves.enemy.position:
					enemy = new_enemy
		else:
			enemy = unit_moves.enemy
			
		# If enemy is null, this means it's already killed and this is the last turn
		if enemy != null:
			var parent = enemy.get_parent()
			if enemy.get_parent() == game_board:
				var non_retal = unit_moves.non_retal
				var retal = unit_moves.retal
			
				# First check whether a non retaliating move is possible before moving on to retaliating moves
				if len(non_retal) > 0:
					for move in non_retal:
						if move != unit.current_pos_map and game_board.is_cell_vacant(game_board.map_to_world(move)):
							end_move = move
							check_sim(unit, move, game_board, simulate)
				elif len(retal) > 0 :
					for move in retal:
						if move != unit.current_pos_map and game_board.is_cell_vacant(game_board.map_to_world(move)):
							end_move = move
							check_sim(unit, move, game_board, simulate)
	
	# Wait if you are not simulating
	if !simulate:
		unit.is_attacking = true
		unit.AI_target = enemy
		if end_move != null:
			
			var timer = Timer.new()
			timer.set_wait_time(5)
			unit.add_child(timer)
			timer.start()
			yield(timer, "timeout")

		else:
			game_board.movement = false
			unit.has_moved = true
			unit.animate_attack(null, enemy, false)
	else:
		# Attack and deactivate
		# If enemy is null, this means it's already killed and this is the last turn
		var wr_unit
		if unit != null:
			wr_unit = weakref(unit);
		
		var wr_enemy
		if enemy != null:
			wr_enemy = weakref(enemy);
		
		if wr_unit.get_ref():
			if enemy != null and wr_enemy.get_ref():
				unit.attack(null, enemy)
	
	# Check if the game is over or not
#	if unit != null and weakref(unit).get_ref():
#		unit.deactivate_unit()
#		unit.remove_possibilities()


# Execute a move without attacking
func execute_move_only(calc_move: Dictionary, game_board: Gameboard, simulate: bool, new_unit: Unit)  -> void:
	var unit
	
	if simulate and new_unit != null:
		unit = new_unit
	else:
		unit = calc_move.unit
		
	var unit_moves = calc_move.moves
	var enemy
	
	# Activate unit
	unit.is_clicked = true
	game_board.active_unit = unit
	unit.possibilities = game_board.show_possiblities(unit, AllEnums.MOVEMENT_TYPES.MOVE, [])
	
	# Find move to execute
	if !unit.has_moved or (simulate and unit.has_moved):
		if simulate:
			for new_enemy in game_board.new_TurnManager.other_player.current_units:
				if new_enemy.position == unit_moves.enemy.position:
					enemy = new_enemy
		else:
			enemy = unit_moves.enemy
		var battle_outcome = unit_moves.sim_battles.battle_outcome
		var non_retal = unit_moves.non_retal
		var retal = unit_moves.retal
		
		var final_move
		
		for move in retal:
			if not move in calc_move.duplicate_danger and game_board.is_cell_vacant(game_board.map_to_world(move)):
				final_move = move
		
		# TODO If all moves in retal (current unit is defending) can be targeted by 2 or more enemies
		# We can check if the unit should move to a non retal position, stand still or simply move to the first
		# retal position (which is the case now)
		if final_move == null:
			if len(retal) > 0:
				for move in retal:
					if game_board.is_cell_vacant(game_board.map_to_world(move)) and final_move == null:
						final_move = move
			elif len(non_retal) > 0:
				for move in non_retal:
					if game_board.is_cell_vacant(game_board.map_to_world(move)) and final_move == null:
						final_move = move
						
		if final_move == null:
			final_move = Vector2(0,0)

		check_sim(unit, final_move, game_board, simulate)

# Execute a hunt or flee move
func execute_hunt_flee(calc_move: Dictionary, game_board: Gameboard, simulate: bool, new_unit: Unit)  -> void:
	var unit
	if simulate and new_unit != null:
		unit = new_unit
	else:
		unit = calc_move.unit
	var unit_moves = calc_move.moves.new_zone

	# Activate unit
	unit.is_clicked = true
	game_board.active_unit = unit
	unit.possibilities = game_board.show_possiblities(unit, AllEnums.MOVEMENT_TYPES.MOVE, [])
	
	# Find move to execute
	if !unit.has_moved or (simulate and unit.has_moved):
		if len(unit_moves) > 0:
			for move in unit_moves:
					if game_board.is_cell_vacant(game_board.map_to_world(move.zone)):
						check_sim(unit, move.zone, game_board, simulate)
		else:
			# Stand still
			check_sim(unit, Vector2(0,0), game_board, simulate)


# Check whether we are simulating or not, based on that teleport the unit or 'physically' move it
func check_sim(unit: Unit, move: Vector2, game_board: Gameboard, simulate: bool):
	if simulate:
		unit.teleport_unit(move, game_board)
	else:
		move_unit(unit, move, game_board)

# Move a unit
func move_unit(unit: Unit, target_position: Vector2, game_board: Gameboard) -> void:
	if game_board.is_cell_vacant(game_board.map_to_world(target_position)) and !unit.has_moved:
		
		if camera != null and weakref(camera).get_ref():
			camera.position = game_board.map_to_world(target_position)
		unit.handle_activated_unit(game_board.map_to_world(target_position) + Vector2(16,16))
		unit.has_moved = true
		unit.target_pos = target_position
	if target_position ==  Vector2(0,0):
		if camera != null and weakref(camera).get_ref():
			camera.position = game_board.map_to_world(target_position)
		unit.has_moved = true
		unit.target_pos = target_position

# Clean gameboards
func clean_gameboards():
	print(str(len(game_boards)) + " boards")
	for board in game_boards:
		board.queue_free()
	
	game_boards = []
