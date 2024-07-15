from player.warrior import Warrior
from world.dungeons.basic_dungeon import Dungeon
import keyboard

player_character = Warrior("test")

test_maze = Dungeon(8, 80, 30)
test_maze.enter_dungeon(player_character)
test_maze.print_map()

moves = ['w', 'a', 's', 'd']

# Simple game loop for capturing player input
while True:
    event = keyboard.read_event()
    if event.event_type == keyboard.KEY_DOWN:
        if event.name in moves:
            test_maze.handle_player_movement(event.name)
        #     test_maze.handle_enemy_actions()
        #
        # if event.name == 'f':
        #     test_maze.generate_enemy()
        #
        # # debug for dijkstra map
        # if event.name == 'm':
        #     test_maze.print_map_to_player()