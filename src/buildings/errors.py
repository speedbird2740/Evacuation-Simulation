class WalkwayFull(Exception):
    def __str__(self):
        return "walkway is full"


class RoomFull(Exception):
    def __str__(self):
        return "room is full"


class WalkwayBlocked(Exception):
    def __str__(self):
        return "walkway is blocked"


class RoomBlocked(Exception):
    def __str__(self):
        return "room is blocked"


class StructureNotFound(Exception):
    def __str__(self):
        return "structure ID is not a valid structure"
