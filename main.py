"""
main.py
-------
Main execution script for the RPG Inventory Engine project.
Handles save file loading, error recovery, and user menu operations.
"""

import os

# Safe import block to handle module resolution errors cleanly
try:
    from models import Item, Weapon, Potion, Armor, Inventory
except ImportError:
    print("❌ Error: Could not import classes from 'models.py'.")
    print("👉 Make sure 'models.py' and 'main.py' are in the same folder,")
    print("   and open that folder in VS Code via File > Open Folder.")
    exit(1)

def load_inventory(file_path: str) -> Inventory:
    """Loads items dynamically from an external CSV file with try/except/finally error recovery."""
    inventory = Inventory()
    file_obj = None
    
    try:
        # Check if save file exists before reading
        if not os.path.exists(file_path):
            print(f"Error: The save file {file_path} was not found.")
            return inventory

        # Open file for reading using standard file handling
        file_obj = open(file_path, mode='r', encoding='utf-8')
        lines = file_obj.readlines()
        
        # Skip header row and loop through records
        for line_no, line in enumerate(lines[1:], start=2):
            try:
                parts = [p.strip() for p in line.strip().split(',')]
                
                # Check for correct column count to prevent malformed parsing
                if len(parts) != 5:
                    raise ValueError(f"Malformed row structure (expected 5 columns, got {len(parts)})")
                
                name, item_type, value_str, rarity, extra_str = parts
                
                # Create object based on item type (OOP Polymorphism)
                if item_type.lower() == "weapon":
                    item = Weapon(name, int(value_str), rarity, int(extra_str))
                elif item_type.lower() == "potion":
                    item = Potion(name, int(value_str), rarity, int(extra_str))
                elif item_type.lower() == "armor":
                    item = Armor(name, int(value_str), rarity, int(extra_str))
                else:
                    item = Item(name, item_type, int(value_str), rarity)
                
                inventory.add_item(item)
                
            except ValueError as row_error:
                # Catch corrupted records and display warning without crashing program
                print(f"⚠️ Warning: Skipped corrupted record on line {line_no} -> {row_error}")
                
    except Exception as e:
        print(f"An unexpected error occurred while accessing the file: {e}")
        
    finally:
        # Finally block guarantees file resources are safely closed
        if file_obj:
            file_obj.close()
            print("🔒 Save file successfully closed and resources released.")
            
    return inventory

def display_items(item_list):
    """Utility function to print a numbered list of items."""
    if not item_list:
        print("No items found.")
        return
    for idx, item in enumerate(item_list, 1):
        print(f"{idx}. {item}")

def main():
    # Set path to items data file inside the data folder
    csv_file = os.path.join("data", "items.csv")
    print("Loading game inventory from save file...")
    player_inventory = load_inventory(csv_file)
    
    if not player_inventory.items:
        print("Inventory is empty or file could not be read.")
        return

    while True:
        # Display 5-option user menu
        print("\n=== RPG INVENTORY ENGINE ===")
        print("1. View Full Inventory (Nested by Category)")
        print("2. Search Item by Name")
        print("3. Filter by Rarity (Common / Rare / Epic)")
        print("4. Calculate Total Gold Value & Unique Categories")
        print("5. Exit")

        # Safely handle non-numeric user inputs
        try:
            choice = int(input("Enter your choice (1-5): "))
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 5.")
            continue

        # Option 1: View Inventory nested by category using dictionaries
        if choice == 1:
            print("\n=== Inventory Categories ===")
            nested_data = player_inventory.get_nested_inventory()
            for cat, items in nested_data.items():
                print(f"\n[{cat.upper()}]")
                for item in items:
                    print(f"  - {item}")

        # Option 2: Search item by name using list comprehension
        elif choice == 2:
            query = input("Enter item name to search: ").strip().lower()
            found = [i for i in player_inventory.items if query in i.name.lower()]
            print(f"\n--- Search Results for '{query}' ---")
            display_movies_list = found # reusing display utility format
            display_items(display_movies_list)

        # Option 3: Filter by rarity using list comprehension
        elif choice == 3:
            rarity_query = input("Enter rarity to filter (Common, Rare, Epic): ").strip().lower()
            filtered = [i for i in player_inventory.items if i.rarity.lower() == rarity_query]
            print(f"\n--- Items with Rarity: {rarity_query.title()} ---")
            display_items(filtered)

        # Option 4: Calculate total gold value and unique categories using sets
        elif choice == 4:
            total_gold = sum(item.value for item in player_inventory.items)
            unique_categories = player_inventory.get_categories()
            
            print("\n=== Inventory Analytics ===")
            print(f"Total Valid Items: {len(player_inventory.items)}")
            print(f"Total Gold Value: {total_gold} Gold 🪙")
            print(f"Unique Categories (Set): {unique_categories}")

        # Option 5: Exit application
        elif choice == 5:
            print("Exiting RPG Inventory Engine. Safe travels, adventurer!")
            break
        else:
            print("Invalid option. Please choose between 1 and 5.")

if __name__ == "__main__":
    main()