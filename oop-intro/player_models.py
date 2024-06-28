#!/usr/bin/python3
"""
player_models.py
"""

class Kart:
        """Create Kart objects for Mario Kart game"""

        def __init__(self, playername, character, acc, vel):
            self.name = playername # Player name (Zach, Bob, TimTim, etc)
            self.character = character # nmae of character (Mario, Toad, Princess, etc)
            self.inventory = []  # what is your inventory
            self.movement = {"acceleration": acc, "velocity": vel}

        def __str__(self):
            return self.name

        def change_movement(self, acc, vel):
            self.movement["acceleration"] = acc
            self.movement["velocity"] = vel

        def add_inventory(self, item_to_add):
            """ all players may have a max of 3 items"""
            if len(self.inventory) == 3:
                return
            else:
                self.inventory.append(item_to_add)

        def del_inventory(self, item_to_remove):
            """ player removes an item from their inventory"""
            if len(self.inventory) == 0:
                return
            else:
                self.inventory.remove(item_to_remove)
