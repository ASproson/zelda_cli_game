from actors import Player
from utils import generate_enemy, random_encounter, text_printer, zelda_rescue

def battle(player, enemy):
  count = 0
  text_printer(f"\n\n >>>> Random battle encounter, prepare to fight! <<<< \n", color = 32)
  text_printer(f"\n A wild {enemy.name} appeared! \n")
  print(enemy.art)

  player_death = False

  while True:
    if count % 2 == 0:
      # Enemy turn
      count += 1
      player.hp -= enemy.attack
      if player.hp <= 0:
        text_printer(f"{player.name} has been defeated! \nGanon has taken over Hyrule!", color = 32)
        player_death = True
        return player_death
      text_printer(f"\n{player.name} took {enemy.attack} damage! Their current hp is: {player.hp}", color = 31)
    if count % 2 == 1:
      # Player turn
      count += 1
      text_printer(f"\nWhat action will you take, adventurer? (attack/defend/item)")
      # If the player enters an invalid input, they are punished by being attacked - we don't handle this case on purpose
      player_action = input()
      if player_action == 'attack':
        enemy.hp -= player.attack
        if enemy.hp <= 0:
          text_printer(f"\n{enemy.name} has been defeated! ", color = 32)
          break
        text_printer(f"\n{player.name} hit {enemy.name} for {player.attack} damage! The {enemy.name}'s current hp: {enemy.hp}!", color = 32)
        continue
      if player_action == 'defend':
        player.hp += 2
        text_printer(f"\n{player.name} has defended, they'll take reduced damage next round!", color = 32)
        continue
      if player_action == 'item':
        if len(player.inventory) > 0:
          player.hp += 10
          player.inventory.pop()
          text_printer(f"\n{player.name} used a potion! Their current health: {player.hp}", color = 32)
        else:
          text_printer(f"\n{player.name} has no potions left!", color = 32)

        
base_map = [
      ['#','#', '?', '?', '?', '?', '?', '?', '?', '?' ],
      ['#',' ', '?', '?', '?', '?', '?', '?', '?', '?' ],
      ['?', '?', '?', '?', '?', '?', '?', '?', '?', '?'],
      ['?', '?', '?', '?', '?', '?', '?', '?', '?', '?'],
      ['?', '?', '?', '?', '?', '?', '?', '?', '?', '?'],
      ['?', '?', '?', '?', '?', '?', '?', '?', '?', '?'],
      ['?', '?', '?', '?', '?', '?', '?', '?', '?', '?'],
      ['?', '?', '?', '?', '?', '?', '?', '?', '?', '?'],
      ['?', '?', '?', '?', '?', '?', '?', '?', '?', '?'],
      ['?', '?', '?', '?', '?', '?', '?', '?', 'X', '?'],
      ['?', '?', '?', '?', '?', '?', '?', '?', '?', '?'],
]

def print_map():
  global base_map  
  for row in base_map:
    print(row)
  return base_map

def cartographer(row, column, map_element):
  global base_map
  base_map[row][column] = map_element
  return base_map

def traverse_map():
  map = [
      ['#','#','#','#','#','#','#','#','#','#'],
      ['#',' ',' ',' ','#','#','#','#',' ','#'],
      ['#','#',' ',' ','#',' ',' ',' ',' ','#'],
      ['#','#','#',' ',' ',' ','#',' ','#','#'],
      ['#','#',' ',' ','#','#','#',' ','#','#'],
      ['#',' ',' ','#',' ',' ',' ',' ','#','#'],
      ['#',' ','#','#',' ','#','#','#','#','#'],
      ['#',' ',' ',' ',' ','#','#','#','#','#'],
      ['#',' ','#','#','#','#','#','#','#','#'],
      ['#',' ',' ',' ',' ',' ',' ',' ','X','#'],
      ['#','#','#','#','#','#','#','#','#','#'],
    ]
  current_row = 1
  current_column = 1

  while True:
    movement = input("\nWhich direction to move (N/S/E/W/Map)? ").lower()
    if movement == "map":
      print_map()
      continue

    current_row, current_column, break_point = map_traversal(map, movement, current_row, current_column)
    if break_point:
      break

def map_traversal(map, movement, row = 1, column = 1 ):
  updated_row = row
  updated_column = column

  direction = None

  if random_encounter():
    enemy = generate_enemy()
    game_over = battle(player, enemy)
    if game_over:
      return updated_row, updated_column, True

  if movement == 's':
    updated_row += 1
    direction = "South"
  elif movement == 'n':
    updated_row -= 1
    direction = "North"
  elif movement == 'e':
    updated_column += 1
    direction = "East"
  elif movement == 'w':
    updated_column -= 1
    direction = "West"
  else:
    text_printer("Invalid direction")
    return row, column, False

  is_rescue_point = map[updated_row][updated_column] == 'X'
  if is_rescue_point:
    text_printer("\nZelda has been rescued!", color=34)
    print(zelda_rescue)
    text_printer("\nThanks for playing!\n")
    return updated_row, updated_column, True

  map_height = len(map)
  map_width = len(map[0])
  is_within_bounds = 0 <= updated_row < map_height and 0 <= updated_column < map_width
  is_not_wall = map[updated_row][updated_column] != '#'
  map_element = map[updated_row][updated_column]

  cartographer(updated_row, updated_column, map_element)

  if is_within_bounds and is_not_wall:
    print(f"\nYou moved {direction}")
    direction = None
    return updated_row, updated_column, False
  else:
    print(f"\nThe way {direction} is blocked")
    return row, column, False

player = None

def main():
  global player
  text_printer("Enter your name, intrepid adventurer... \n")
  player_name = input()
  player = Player(player_name, 20, 5, ["potion", "potion"])

  text_printer(f"\nWelcome {player_name}! \n\nBefore you venture forth, it's worth looking at your stats and inventory... Yes?\n")

  view_inventory = input("View inventory (yes/no)?:\n\n")

  if view_inventory.lower() == "yes":
    text_printer('\n' + player.__repr__())
  else:
    text_printer("\nVery well, let's begin the journey!")

  text_printer("\nAt any point you could be set upon by vicious enemies, so be prepared!")
  text_printer("\nYou'll have to find your way to Zelda through the dungeon, but it's really dark, so you can barely see!")
  text_printer("\nAs you move through the dungeon you will automatically map out the area...")
  text_printer("\nThe map can be accessed at any point during movement selection, but lets take a look right now to get your bearings!\n")

  print_map()

  text_printer("\nNotice the X in the lower right hand corner? X marks the spot! Find your way to Zelda intrepid adventurer!")

  traverse_map()

main()