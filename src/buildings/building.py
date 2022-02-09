from buildings import utils, errors
from buildings.structures import Walkway, Room


class Building:

    def __init__(self):
        self.structures = {}
        self.structure_connections = []
        self.people_data = {}
        self.ID = utils.get_id()

    def add_walkway(self, length: float, max_people: int, is_blocked: bool = False, connection: str = None,
                    is_exit: bool = False):
        new_walkway = Walkway(length=length, max_people=max_people, is_blocked=is_blocked, is_exit=is_exit)

        if connection is not None:
            if connection not in self.structures:
                raise errors.StructureNotFound(connection)

            if any(conn == (connection, new_walkway.ID) for conn in self.structure_connections):
                raise Exception

        while new_walkway.ID in self.structures:
            new_walkway = Walkway(length=length, max_people=max_people, is_blocked=is_blocked)

        self.structures[new_walkway.ID] = new_walkway

        if connection is not None:
            self.structure_connections.append((connection, new_walkway.ID))

    def add_room(self, max_people: int, is_blocked: bool = False, connection: str = None):
        if connection is not None and connection not in self.structures:
            raise errors.StructureNotFound(connection)

        new_room = Room(max_people=max_people, is_blocked=is_blocked)

        while new_room.ID in self.structures:
            new_room = Room(max_people=max_people, is_blocked=is_blocked)

        self.structures[new_room.ID] = new_room

        if connection is not None:
            self.structure_connections.append((connection, new_room.ID))

        return new_room.ID

    def add_person(self, room_id: int, count: int = 1, walk_speed: float = 3.5):
        if room_id not in self.structures:
            raise Exception

        room = self.structures[room_id]
        people_ids = room.add_person(count=count, walk_speed=walk_speed)

        for ID in people_ids:
            self.people_data[ID] = {"location": room_id}

        return people_ids

    async def change_struct_status(self, struct_id: str, name: str, value: int or bool, auto: bool = False):
        if struct_id not in self.structures:
            raise Exception

        struct = self.structures[struct_id]

        if type(value) == bool:
            if name == "is_blocked":
                struct.is_blocked = value
            else:
                raise Exception

        elif type(value) == int:
            if name == "fire":
                await struct.simulate_fire(intensity=value, auto=auto)
            elif name == "smoke":
                await struct.simulate_smoke(intensity=value, auto=auto)

    async def _find_exits(self, person_id: str):
        # a lot of placeholder here
        location = self.people_data[person_id]["location"]
        paths = []

        if person_id not in self.people_data:
            raise Exception
        if location not in self.structures:
            raise Exception

        async def worker(path: int):
            pass

        await worker(1)
        print(paths)

        while True:
            break
