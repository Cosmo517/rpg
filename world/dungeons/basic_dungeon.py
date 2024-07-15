import os
import random

from world.common.tile import Tile
from world.dungeons.create_dungeon_map import BuildDungeon


class Dungeon:
    def __init__(self, min_room_size, width=10, height=10):
        """
        :param min_room_size: The minimum size of a room
        :param width:  The width of the maze
        :param height: The height of the maze
        """
        # self.entrance_y = entrance_y
        # self.entrance_x = entrance_x
        self.maze_width = width
        self.maze_height = height
        self.player_character = None
        self.player_pos_x = -1
        self.player_pos_y = -1
        self.entrance_pos_x = None
        self.entrance_pos_y = None
        self.dungeon_map = [[Tile() for x in range(self.maze_width)] for y in range(self.maze_height)]
        self.enemies = []
        self.dungeon_generator = BuildDungeon(width, height)
        while len(self.dungeon_generator.rooms) < 8:
            self.dungeon_walls = self.dungeon_generator.generate_dungeon(min_room_size)
        self.create_dungeon_map()

    def create_dungeon_map(self):
        """Create a simple square dungeon that is the width and height of the dungeon"""
        for y in range(self.maze_height):
            for x in range(self.maze_width):
                if self.dungeon_walls[y][x]:
                    self.dungeon_map[y][x].set_walkable(False)
                    self.dungeon_map[y][x].set_display_char('#')
                else:
                    self.dungeon_map[y][x].set_walkable(True)
                    self.dungeon_map[y][x].set_display_char(' ')

    def enter_dungeon(self, player):
        self.player_character = player
        if self.entrance_pos_x is None and self.entrance_pos_y is None:
            while True:
                self.player_pos_x = random.randint(0, self.maze_width)
                self.player_pos_y = random.randint(0, self.maze_height)
                if self.dungeon_map[self.player_pos_y][self.player_pos_x].get_walkable():
                    break
        else:
            self.player_pos_x = self.entrance_pos_x
            self.player_pos_y = self.entrance_pos_y
        self.dungeon_map[self.player_pos_y][self.player_pos_x].set_display_char('@')

    def exit_dungeon(self):
        if self.player_pos_x == self.entrance_pos_x and self.player_pos_y == self.entrance_pos_y:
            self.player_character = None

    def handle_player_movement(self, key_pressed):
        """Handle the movement of the player when they press a related key"""
        move_dict = {'w': (0, -1), 'a': (-1, 0), 's': (0, 1), 'd': (1, 0)}  # this is in x,y form
        new_x, new_y = 0, 0
        if key_pressed in move_dict:
            move_x, move_y = move_dict[key_pressed]
            new_x, new_y = self.player_pos_x + move_x, self.player_pos_y + move_y

        if (0 <= new_y < self.maze_height and 0 <= new_x < self.maze_width and
                not self.dungeon_map[new_y][new_x].is_wall() and self.dungeon_map[new_y][new_x].get_walkable()):
            user_x, user_y = self.player_pos_x, self.player_pos_y
            self.dungeon_map[user_y][user_x].set_display_char(' ')
            self.dungeon_map[user_y][user_x].set_entity(None)
            self.player_pos_y, self.player_pos_x = new_y, new_x
            self.dungeon_map[new_y][new_x].set_display_char('@')
            self.dungeon_map[new_y][new_x].set_entity(self.player_character)
            os.system('cls')
            self.print_map()

    def print_map(self):
        """Print the map of the dungeon"""
        for i in range(self.maze_height):
            s = ' '
            for j in range(self.maze_width):
                s += self.dungeon_map[i][j].get_display_char()
            print(s)
