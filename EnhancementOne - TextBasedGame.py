# Jenifer Sanchez

# Escaping the Enchanted Castle
# Enhanced version for CS 499
#
# Improvements in this version:
# - Uses a Game class to organize the code
# - Breaks the code into small, easy-to-read methods
# - Adds simple input checks and helper commands
# - Makes the code cleaner and easier to update

from copy import deepcopy

# Room layout for the game
ROOMS_TEMPLATE = {
    'Foyer': {'North': 'Timeless Antique Shop'},
    'The Vault Basement': {
        'North': "Mastermind's Labyrinth",
        'East': 'Champagne Cellar',
        'South': 'Timeless Antique Shop',
        'West': 'Cornelia Rose Garden'
    },
    'Teardrop Pool': {'item': 'Turquoise', 'West': 'Champagne Cellar'},
    'Love Story Library': {
        'item': 'Citrine',
        'North': 'Champagne Cellar',
        'West': 'Timeless Antique Shop'
    },
    'Timeless Antique Shop': {
        'item': 'Amethyst',
        'North': 'The Vault Basement',
        'East': 'Love Story Library',
        'South': 'Foyer',
        'West': '10 Minute Break Room'
    },
    '10 Minute Break Room': {
        'item': 'Ruby',
        'North': 'Cornelia Rose Garden',
        'East': 'Timeless Antique Shop'
    },
    'Wildest Dreams Theater': {
        'item': 'Aquamarine',
        'South': "Mastermind's Labyrinth"
    },
    'Serpentine Sanctuary': {
        'item': 'Black Spinel',
        'East': 'Cornelia Rose Garden'
    },
    'Cornelia Rose Garden': {
        'item': 'Rose Quartz',
        'North': 'The Alchemist Lab',
        'East': 'The Vault Basement',
        'South': '10 Minute Break Room',
        'West': 'Serpentine Sanctuary'
    },
    'The Lakes Viewing Room': {
        'item': 'Grey Pearl',
        'South': 'Champagne Cellar',
        'West': "Mastermind's Labyrinth"
    },
    'Champagne Cellar': {
        'item': 'Topaz',
        'North': 'The Lakes Viewing Room',
        'East': 'Teardrop Pool',
        'South': 'Love Story Library',
        'West': 'The Vault Basement'
    },
    "Mastermind's Labyrinth": {
        'item': 'Sapphire',
        'North': 'Wildest Dreams Theater',
        'East': 'The Lakes Viewing Room',
        'South': 'The Vault Basement',
        'West': 'The Alchemist Lab'
    },
    'The Alchemist Lab': {
        'item': 'Diamond',
        'East': "Mastermind's Labyrinth",
        'South': 'Cornelia Rose Garden'
    },
}


class Game:
    # This class keeps track of game state
    VALID_DIRECTIONS = {'north', 'east', 'south', 'west'}
    START_ROOM = 'Foyer'
    VILLAIN_ROOM = 'The Vault Basement'

    def __init__(self):
        # Make a fresh copy of the rooms for each playthrough
        self.rooms = deepcopy(ROOMS_TEMPLATE)

        # Player starts in the foyer with an empty inventory
        self.current_room = self.START_ROOM
        self.inventory = []

        # Find all gemstones in the map
        self.all_items = {
            data.get('item') for data in self.rooms.values() if data.get('item')
        }
        self.total_items = len(self.all_items)

    def print_instructions(self):
        # Show the story and basic commands
        print('Escaping the Enchanted Castle!')
        print('\nCollect all 11 gemstones and defeat the Shadow Thief to escape.')
        print('\nCommands:')
        print('  go north / go east / go south / go west')
        print('  get <gemstone name>')
        print('  help')
        print('  quit')

    def print_status(self):
        # Show where the player is and what they have
        print('\nYou are in:', self.current_room)
        print('Inventory:', ', '.join(self.inventory) if self.inventory else 'empty')

        # Show gemstone in the room
        item = self.rooms[self.current_room].get('item')
        if item:
            print('There is a gemstone here:', item)

    def check_villain_room(self):
        # Check if the player entered the Shadow Thief's room
        if self.current_room != self.VILLAIN_ROOM:
            return False

        # If player doesn't have all gemstones, they lose
        if len(self.inventory) < self.total_items:
            print('\nYou were caught by the Shadow Thief! Game over.')
        else:
            print('\nYou defeated the Shadow Thief! You escape the castle!')

        return True

    def move_player(self, direction):
        # Move the player if the direction is allowed
        direction_cap = direction.capitalize()
        room_data = self.rooms[self.current_room]

        if direction_cap in room_data:
            self.current_room = room_data[direction_cap]
        else:
            print('\nYou cannot go that way.')

    def collect_item(self, item_name):
        # Pick up a gemstone if it is in the room
        item_title = item_name.title()
        room_data = self.rooms[self.current_room]
        room_item = room_data.get('item')

        # Check if it's a real gemstone
        if item_title not in self.all_items:
            print('\nThat is not a real gemstone.')
            return

        # Check if the room has this gemstone
        if room_item is None:
            print('\nThere is no gemstone here.')
            return

        if room_item != item_title:
            print('\nThat gemstone is not in this room.')
            return

        # Add gemstone to inventory
        self.inventory.append(item_title)
        room_data['item'] = None
        print('\nYou picked up:', item_title)

        # Check if player has all gemstones
        if len(self.inventory) == self.total_items:
            print('\nYou have all 11 gemstones! Find the Shadow Thief!')

    def handle_help(self):
        # Show a simple list of commands
        print('\nCommands you can use:')
        print('  go <direction>')
        print('  get <gemstone>')
        print('  help')
        print('  quit')

    def parse_and_execute(self, command):
        # Read the player's command and decide what to do
        command = command.strip().lower()

        if not command:
            print('\nPlease type a command.')
            return True

        if command in {'quit', 'exit'}:
            print('\nBetter luck next time.')
            return False

        if command == 'help':
            self.handle_help()
            return True

        parts = command.split(maxsplit=1)
        action = parts[0]

        # Handle movement
        if action == 'go':
            if len(parts) == 1:
                print('\nPlease say a direction.')
                return True

            direction = parts[1]

            if direction not in self.VALID_DIRECTIONS:
                print('\nNot a valid direction.')
                return True

            self.move_player(direction)
            return True

        # Handle item pickup
        if action == 'get':
            if len(parts) == 1:
                print('\nPlease say the gemstone name.')
                return True

            item_name = parts[1]
            self.collect_item(item_name)
            return True

        print('\nInvalid command. Type "help" for help.')
        return True

    def run(self):
        # Main game loop
        self.print_instructions()

        while True:
            self.print_status()

            # Check if player is in the villain room
            if self.check_villain_room():
                break

            print('--------------------------------------')
            command = input('Your move: ')
            keep_playing = self.parse_and_execute(command)

            if not keep_playing:
                break


def main():
    # Start the game
    game = Game()
    game.run()


if __name__ == '__main__':
    main()
