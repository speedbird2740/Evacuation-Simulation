import utils
import errors
from structures import Walkway, Room


class Building:

    def __init__(self):
        self.structures = {}
        self.structure_connections = []
        self.ID = utils.get_id()

    def add_walkway(self, length: float, max_people: int, is_blocked: bool = False, connection: str = None):
        new_walkway = Walkway(length=length, max_people=max_people, is_blocked=is_blocked)

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

    def add_person(self, room_id: int, count: int=1):
        pass

    def change_struct_status(self, is_blocked: bool = None):
        if is_blocked is None:
            raise Exception
