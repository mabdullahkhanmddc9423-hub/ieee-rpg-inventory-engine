"""
models.py
---------
Module defining OOP Inheritance classes for the RPG Inventory Engine.
"""

class Item:
    # Base class representing a generic item in the game
    def __init__(self, name: str, item_type: str, value: int, rarity: str):
        self.name = name.strip()
        self.item_type = item_type.strip().title()
        self.value = int(value)
        self.rarity = rarity.strip().title()

    def __str__(self) -> str:
        return f"{self.name} [{self.item_type}] - Value: {self.value} Gold | Rarity: {self.rarity}"


class Weapon(Item):
    # Child class for weapons, adding attack power
    def __init__(self, name: str, value: int, rarity: str, attack_power: int):
        super().__init__(name, "Weapon", value, rarity)
        self.attack_power = int(attack_power)

    def __str__(self) -> str:
        return f"{self.name} [Weapon] - Attack: {self.attack_power} | Value: {self.value} Gold | Rarity: {self.rarity}"


class Potion(Item):
    # Child class for potions, adding heal amount
    def __init__(self, name: str, value: int, rarity: str, heal_amount: int):
        super().__init__(name, "Potion", value, rarity)
        self.heal_amount = int(heal_amount)

    def __str__(self) -> str:
        return f"{self.name} [Potion] - Heal: {self.heal_amount} HP | Value: {self.value} Gold | Rarity: {self.rarity}"


class Armor(Item):
    # Child class for armor, adding defense rating
    def __init__(self, name: str, value: int, rarity: str, defense_rating: int):
        super().__init__(name, "Armor", value, rarity)
        self.defense_rating = int(defense_rating)

    def __str__(self) -> str:
        return f"{self.name} [Armor] - Defense: {self.defense_rating} | Value: {self.value} Gold | Rarity: {self.rarity}"


class Inventory:
    # Manages the player's collection of items
    def __init__(self):
        self.items = []

    def add_item(self, item: Item):
        self.items.append(item)

    def get_categories(self) -> set:
        return {item.item_type for item in self.items}

    def get_nested_inventory(self) -> dict:
        nested = {}
        for item in self.items:
            if item.item_type not in nested:
                nested[item.item_type] = []
            nested[item.item_type].append(item)
        return nested