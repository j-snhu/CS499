# Jenifer Sanchez

# Dictionary to link a room to other rooms as well as a room to its item
rooms = {
    'Foyer': {'North': 'Timeless Antique Shop'},
    'The Vault Basement': {'North': "Mastermind's Labyrinth", 'East': 'Champagne Cellar', 'South': 'Timeless Antique Shop', 'West': 'Cornelia Rose Garden'},
    'Teardrop Pool': {'item': 'Turquoise', 'West': 'Champagne Cellar'},
    'Love Story Library': {'item': 'Citrine', 'North': 'Champagne Cellar', 'West': 'Timeless Antique Shop'},
    'Timeless Antique Shop': {'item': 'Amethyst', 'North': 'The Vault Basement', 'East': 'Love Story Library', 'South': 'Foyer','West': '10 Minute Break Room'},
    '10 Minute Break Room': {'item': 'Ruby', 'North': 'Cornelia Rose Garden', 'East': 'Timeless Antique Shop'},
    'Wildest Dreams Theater': {'item': 'Aquamarine', 'South': "Mastermind's Labyrinth"},
    'Serpentine Sanctuary': {'item': 'Black Spinel', 'East': 'Cornelia Rose Garden'},
    'Cornelia Rose Garden': {'item': 'Rose Quartz', 'North': 'The Alchemist Lab', 'East': 'The Vault Basement', 'South': '10 Minute Break Room', 'West': 'Serpentine Sanctuary'},
    'The Lakes Viewing Room': {'item': 'Grey Pearl', 'South': 'Champagne Cellar', 'West': "Mastermind's Labyrinth"},
    'Champagne Cellar': {'item': 'Topaz', 'North': 'The Lakes Viewing Room', 'East': 'Teardrop Pool', 'South': 'Love Story Library', 'West': 'The Vault Basement'},
    "Mastermind's Labyrinth": {'item': 'Sapphire', 'North': 'Wildest Dreams Theater', 'East': 'The Lakes Viewing Room', 'South': 'The Vault Basement', 'West': 'The Alchemist Lab'},
    'The Alchemist Lab': {'item': 'Diamond', 'East': "Mastermind's Labyrinth", 'South': 'Cornelia Rose Garden'},
}

# Print a menu and instructions
def instructions():
    print('Escaping the Enchanted Castle!')
    print('\nCollect all 11 magical gemstones and defeat the Shadow Thief to escape. '
          '\nGet caught before you have all the gemstones and you will stay trapped in the castle forever')
    print('Move Commands: go North, go East, go South, go West')
    print("Add gemstone to your inventory: get 'gemstone name'")

# Display player's location and inventory
def status(current_room, inventory):
    print('\nYou are currently in: ' + current_room)
    print('Inventory: ' + str(inventory))
    if 'item' in rooms[current_room] and rooms[current_room]['item'] is not None:
        print('\nYou found a gemstone: ' + rooms[current_room]['item'])

# Main Game
def main():
    instructions()
    current_room = 'Foyer'
    inventory = []
    total_items = 11

    # Define valid directions and items
    valid_directions = {'North', 'East', 'South', 'West'}
    valid_items = {'Turquoise', 'Citrine', 'Amethyst', 'Ruby', 'Aquamarine', 'Black Spinel', 'Rose Quartz', 'Grey Pearl', 'Topaz', 'Sapphire', 'Diamond'}

    while True:
        status(current_room, inventory)

        # Validate conditions for inside the villain room
        if current_room == 'The Vault Basement':
            if len(inventory) < total_items:
                print('\nOH NO! You were caught by the Shadow Thief! GAME OVER')
                break
            else:
                print('\nYES! You have defeated the Shadow Thief and can escape! Congratulations!')
                break

        print('---------------------------------------------------')
        command = input('Make your next move: ')

        # Check for directional command
        if command.startswith('go '):
            direction = command[3:].capitalize()
            # Check that the direction is valid
            if direction in valid_directions:
                if direction in rooms[current_room]:
                    current_room = rooms[current_room][direction]  # Move to the new room and set as current room
                else:
                    print("\nYou can't go that way!")  # Invalid direction
            else:
                print('\nInvalid direction!')

        # Check for item collect command
        elif command.startswith('get '):
            item_name = command[4:].strip().title()
            # Check that the item is valid
            if item_name in valid_items:
                if item_name == rooms[current_room].get('item'):
                    inventory.append(item_name)
                    print('\nYou have collected the ' + item_name + ' gemstone!')
                    rooms[current_room]['item'] = None  # Remove the item from the room
                else:
                    print('\nThat item is not in this room or has already been collected!')

                # Check for all 11 items from the player
                if len(inventory) == total_items:
                    print('\nYou have collected all 11 gemstones! Now face the Shadow Thief to escape!')

            else:
                print('\nInvalid Item!')

        # Catch-all for other invalid commands
        else:
            print('\nInvalid command! Please enter a valid direction or item to collect.')

# start game
if __name__ == '__main__':
    main()

