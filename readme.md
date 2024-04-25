# Rescue Zelda! 

Intrepid adventurer, Ganon has kidnapped Zelda and it's down to you to rescue her! 

- Brave the ASCII CLI dungeon
- Plot your way through the ASCII maze in real time
- Fight ASCII enemies from the _Zelda_ franchise in turn-based combat
- Use items to heal
- Reach the end to rescue Zelda and claim your reward!

## Installation

Python is required to be installed to run the game

> `git clone https://github.com/ASproson/zelda_cli_game.git`

> `cd zelda_cli_game`

> `python main.py`

## Gameplay

The game is intended to last between 5-10 minutes, below is a GIF demonstrating the core gameplay (frames limited to produce a small GIF size):

![Animation](https://github.com/ASproson/zelda_cli_game/assets/77736272/56f797e8-a752-4113-9721-8db9e36e7b29)

Above, towards the end of the GIF animation, you will see a Bokoblin be rendered to the console in ASCII. Here is the original for reference:

![Bokoblin](https://img.rankedboost.com/wp-content/uploads/2023/05/Zelda-Tears-of-the-Kingdom-Bokoblin-1.png)

## Technical Walkthrough

This was a fun project I decided to take on one weekend as I wanted to see if I could produce various game systems from scratch, specifically:

- Turn based combat
- Random enemy encounters
- Automatic character mapping
- Enabling user input to direct combat/dungeon traversal

#### Battle System

The battle system is turn based, which allows the use of a counter that gets incremented on each turn. Whenever the turn counter is even and the current actors are still alive (PC and NPC), it's the enemies turn and vice versa. This was a fun excuse to reaffirm my knowledge of OOP, which lead to the creaton of `actors.py`. This file allows me to create an `actor` object that can be shaped into either a player character or an NPC.

In this system the player can attack, defend, or use an item (so long as they have enough potions in their inventory) based on their input. Invalid inputs are 'punished' intentionally, meaning that when a user does not enter a valid input they effectively 'miss' their turn and as such get attacked by the enemy.

Battles are randomy generated for each step taken (even when it's an invalid step in the dungeon), triggering 10% of the time. This felt like the right encounter rate as it mostly ensures that _at least_ one encounter will happen per playthrough. 

#### Dialogue System

The diaglogue system accepts player input to direct combat and map traversal. I created the `text_printer` function so that the characters would 'type' onto the screen rather than appear in full length immediately, this was just to give the game a little more flavor, and it allowed me to easily reuse that function but with different colors to represent specific player/NPC actions

#### Traversing the Dungeon

Working out traversal was the most challenging aspect of the project. Essentially I created two maps, a 'blank' and a 'completed' map. I would then use the `cartographer` function to update the blank based on player input and whether or not the entered direction was valid. The reason for the blank map was so that players could `print_map()` at any point to get a sense of their bearings, realistically if this wasn't a feature we would have only needed a single completed map. 

#### ASCII Art Generator

ASCII art was generated using [asciiart.eu](https://www.asciiart.eu/image-to-ascii)
