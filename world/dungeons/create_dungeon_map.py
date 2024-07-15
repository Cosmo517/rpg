import random


class Room:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def center(self):
        center_x = self.x + self.width // 2
        center_y = self.y + self.height // 2
        return center_x, center_y


class BuildDungeon:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.dungeon_map = [[True for x in range(self.width)] for y in range(self.height)]
        self.rooms = []

    def split(self, x, y, width, height, min_size):
        if width < min_size or height < min_size:
            return [(x, y, width, height)]

        split_horizontal = random.choice([True, False])

        if split_horizontal:
            if height >= 2 * min_size:
                split_y = random.randint(min_size, height - min_size)
                top = self.split(x, y, width, split_y, min_size)
                bottom = self.split(x, y + split_y, width, height - split_y, min_size)
                return top + bottom
        else:
            if width >= 2 * min_size:
                split_x = random.randint(min_size, width - min_size)
                left = self.split(x, y, split_x, height, min_size)
                right = self.split(x + split_x, y, width - split_x, height, min_size)
                return left + right

        return [(x, y, width, height)]

    def create_room(self, x, y, width, height):
        room_width = random.randint(3, width - 2)
        room_height = random.randint(3, height - 2)
        room_x = x + random.randint(1, width - room_width - 1)
        room_y = y + random.randint(1, height - room_height - 1)

        for i in range(room_y, room_y + room_height):
            for j in range(room_x, room_x + room_width):
                self.dungeon_map[i][j] = False

        return Room(room_x, room_y, room_width, room_height)

    def connect_rooms(self, room1, room2):
        x1, y1 = room1.center()
        x2, y2 = room2.center()

        if random.choice([True, False]):
            self.create_h_corridor(x1, x2, y1)
            self.create_v_corridor(y1, y2, x2)
        else:
            self.create_v_corridor(y1, y2, x1)
            self.create_h_corridor(x1, x2, y2)

    def create_h_corridor(self, x1, x2, y):
        for x in range(min(x1, x2), max(x1, x2) + 1):
            self.dungeon_map[y][x] = False

    def create_v_corridor(self, y1, y2, x):
        for y in range(min(y1, y2), max(y1, y2) + 1):
            self.dungeon_map[y][x] = False

    def generate_dungeon(self, min_size):
        regions = self.split(0, 0, self.width, self.height, min_size)

        for (x, y, width, height) in regions:
            if width >= min_size and height >= min_size:
                room = self.create_room(x, y, width, height)
                self.rooms.append(room)

        for i in range(len(self.rooms) - 1):
            self.connect_rooms(self.rooms[i], self.rooms[i + 1])

        return self.dungeon_map
    
