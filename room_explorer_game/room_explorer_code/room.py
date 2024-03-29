from items import Item, Grabbable, SoundItem, CodeItem

class Room:
    
    def __init__(self, name):
        self.name = name
        self.exit_directions = [] # north, south, east, west, etc.
        self.exit_destinations = [] #the Rooms each exit leads to
        self.items = [] #the items in the room
        self.room_description = "" #description of the room
        self.locked = False #controls whether a room can be entered
        self.hints_used = 0

    #getters/setters
    @property                               #name
    def name(self):
        return self._name

    @name.setter
    def name(self, new_value):
        self._name = new_value

    @property                               #exit_directions
    def exit_directions(self):
        return self._exit_directions

    @exit_directions.setter
    def exit_directions(self, new_value):
        self._exit_directions = new_value

    @property                               #exit_destinations
    def exit_destinations(self):
        return self._exit_destinations

    @exit_destinations.setter
    def exit_destinations(self, new_value):
        self._exit_destinations = new_value

    @property                               #room_description
    def room_description(self):
        return self._room_description

    @room_description.setter
    def room_description(self, new_value):
        self._room_description = new_value

    #additional methods
    def add_exit(self, exit_direction, exit_destination):
        self.exit_directions.append(exit_direction)
        self.exit_destinations.append(exit_destination)

    def add_item(self, name:str, description:str):
        item = Item(name, description)
        self.items.append(item)

    def add_grabbable(self, name:str, description:str):
        item = Grabbable(name, description)
        self.items.append(item)

    def add_sound_item(self, name:str, description:str, sound_file:str):
        item = SoundItem(name, description, sound_file)
        self.items.append(item)

    def add_code_item(self, name:str, description:str, correct_code:str):
        item = CodeItem(name, description, correct_code)
        self.items.append(item)





    # __str__ func
    def __str__(self):
        result = '\n\n'

        #room name 
        result += f"You find yourself in what appears to be the {self.name}.\n"

        #description
        result += f"{self.room_description}\n"

        #items
        if len(self.items) != 0:
            result += "\nYou see:\n"
            for item in self.items:
                result += f"{item.name}\n"

        #exits
        if len(self.exit_directions) != 0:
            result += "\nExits:\n"
            for exit in self.exit_directions:
                result += f"{exit}\n"

        return result 
    