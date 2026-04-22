from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Item, ItemClassification

if TYPE_CHECKING:
    from .world import SkulWorld

ITEM_NAME_TO_ID = {
    
    # Progression
    "Progressive Stage": 20,
    "Progressive Skull Tree": 21,
    "Progressive Bone Tree": 22,
    "Progressive Spirit Tree": 23,
    
    # Useful
    "Marrow Transplant": 1,
    "Thick Bone": 2,
    "Fatal Mind": 3,
    "Quick Dislocation": 4,
    "Fracture Prevention": 5,
    "Ancestral Fortitude": 6,
    "Nutrition Supply": 7,
    "Heavy Frame": 8,
    "Spirit Acceleration": 9,
    "Exoskeleton Reinforcement": 10,
    "Reassemble": 11,
    "Ancient Alchemy": 12,
    "Fox NPC": 13,
    "Ogre NPC": 14,
    "Druid NPC": 15,
    "Death Knight NPC": 16,

    # Useful Skulls (These start at 100)
    "Carleon Recruit": 100,
    "Ent Skull": 101,
    "Grave Digger": 102,
    "Mage": 103,
    "Petty Thief": 104,
    "Skeleton-Pike": 105,
    "Skeleton-Shield": 106,
    "Skeleton-Sword": 107,
    "Stone Monkey": 108,
    "Werewolf": 109,
    "Viking": 110,
    "Slave": 111,

    # RARE Skulls
    "Alchemist": 112,
    "Clown": 113,
    "Frost Skull": 114,
    "Gargoyle": 115,
    "Gene": 116,
    "Ghoul": 117,
    "Hunter": 118,
    "Minotaurus": 119,
    "Mummy": 120,
    "Rider": 121,
    "Skeleton-Bomber": 122,
    "Warrior": 123,
    "Water Skull": 124,
    "Officer": 125,

    # UNIQUE Skulls
    "Berserker": 126,
    "Dark Paladin": 127,
    "Great Warlock": 128,
    "Living Armor": 129,
    "Ninja": 130,
    "Predator": 131,
    "Prisoner": 132,
    "Rockstar": 133,
    "Samurai": 134,
    "Ascetic": 135,

    # LEGENDARY Skulls
    "Archlich": 136,
    "Champion": 137,
    "Davy Jones": 138,
    "Gambler": 139,
    "Grim Reaper": 140,
    "Yaksha": 141,
    "Dominator": 142,
    "Unknown King": 143,

    # SPECIAL Skulls
    "Guard Captain": 144,

    # Filler
    "Bone x10": 30,
    "Dark Quartz x100": 31,
    "Gold x200": 32,

    # Trap
    "De-Skull Trap": 40,
}

DLC_SKULL_NAMES: frozenset[str] = frozenset({
    "Viking", "Slave", "Officer", "Ascetic", "Unknown King",
})

DEFAULT_ITEM_CLASSIFICATIONS = {
    "Progressive Stage": ItemClassification.progression,
    "Progressive Skull Tree": ItemClassification.progression,
    "Progressive Bone Tree": ItemClassification.progression,
    "Progressive Spirit Tree": ItemClassification.progression,
    
    "Marrow Transplant": ItemClassification.useful,
    "Thick Bone": ItemClassification.useful,
    "Fatal Mind": ItemClassification.useful,
    "Quick Dislocation": ItemClassification.useful,
    "Fracture Prevention": ItemClassification.useful,
    "Ancestral Fortitude": ItemClassification.useful,
    "Nutrition Supply": ItemClassification.useful,
    "Heavy Frame": ItemClassification.useful,
    "Spirit Acceleration": ItemClassification.useful,
    "Exoskeleton Reinforcement": ItemClassification.useful,
    "Reassemble": ItemClassification.useful,
    "Ancient Alchemy": ItemClassification.useful,
    "Fox NPC": ItemClassification.useful,
    "Ogre NPC": ItemClassification.useful,
    "Druid NPC": ItemClassification.useful,
    "Death Knight NPC": ItemClassification.progression,

    # Common Skulls
    "Carleon Recruit": ItemClassification.useful,
    "Ent Skull": ItemClassification.useful,
    "Grave Digger": ItemClassification.useful,
    "Mage": ItemClassification.useful,
    "Petty Thief": ItemClassification.useful,
    "Skeleton-Pike": ItemClassification.useful,
    "Skeleton-Shield": ItemClassification.useful,
    "Skeleton-Sword": ItemClassification.useful,
    "Stone Monkey": ItemClassification.useful,
    "Werewolf": ItemClassification.useful,
    "Viking": ItemClassification.useful, # DLC
    "Slave": ItemClassification.useful, # DLC

    # RARE Skulls
    "Alchemist": ItemClassification.useful,
    "Clown": ItemClassification.useful,
    "Frost Skull": ItemClassification.useful,
    "Gargoyle": ItemClassification.useful,
    "Gene": ItemClassification.useful,
    "Ghoul": ItemClassification.useful,
    "Hunter": ItemClassification.useful,
    "Minotaurus": ItemClassification.useful,
    "Mummy": ItemClassification.useful,
    "Rider": ItemClassification.useful,
    "Skeleton-Bomber": ItemClassification.useful,
    "Warrior": ItemClassification.useful,
    "Water Skull": ItemClassification.useful,
    "Officer": ItemClassification.useful, # DLC

    # UNIQUE Skulls
    "Berserker": ItemClassification.useful,
    "Dark Paladin": ItemClassification.useful,
    "Great Warlock": ItemClassification.useful,
    "Living Armor": ItemClassification.useful,
    "Ninja": ItemClassification.useful,
    "Predator": ItemClassification.useful,
    "Prisoner": ItemClassification.useful,
    "Rockstar": ItemClassification.useful,
    "Samurai": ItemClassification.useful,
    "Ascetic": ItemClassification.useful, # DLC

    # LEGENDARY Skulls
    "Archlich": ItemClassification.progression,
    "Champion": ItemClassification.progression,
    "Davy Jones": ItemClassification.progression,
    "Gambler": ItemClassification.progression,
    "Grim Reaper": ItemClassification.progression,
    "Yaksha": ItemClassification.progression,
    "Dominator": ItemClassification.progression,
    "Unknown King": ItemClassification.progression, # DLC

    # SPECIAL Skulls
    "Guard Captain": ItemClassification.progression,

    "Bone x10": ItemClassification.filler,
    "Dark Quartz x100": ItemClassification.filler,
    "Gold x200": ItemClassification.filler,

    "De-Skull Trap": ItemClassification.trap,
}


class SkulItem(Item):
    game = "Skul: The Hero Slayer"


def get_random_filler_item_name(world: SkulWorld) -> str:
    trap_chance = world.options.de_skull_trap_weight.value
    if trap_chance and world.random.randint(0, 99) < trap_chance:
        return "De-Skull Trap"
    return world.random.choice(["Bone x10", "Dark Quartz x100", "Gold x200"])


def create_item_with_correct_classification(world: SkulWorld, name: str) -> SkulItem:
    classification = DEFAULT_ITEM_CLASSIFICATIONS[name]

    return SkulItem(name, classification, ITEM_NAME_TO_ID[name], world.player)


def create_all_items(world: SkulWorld) -> None:

    itempool: list[Item] = []

    # Progressive Stage (one per area: Forest, Grand Hall, Black Lab, Fortress of Fate, Sacred Grounds)
    itempool += [world.create_item("Progressive Stage") for _ in range(5)]

    # Progressive tree upgrades (3 per tree — gates tiers 1, 2, 3 of each witch tree)
    for name in ["Progressive Skull Tree", "Progressive Bone Tree", "Progressive Spirit Tree"]:
        itempool += [world.create_item(name) for _ in range(3)]

    # Bone upgrades (x10 each)
    for name in [
        "Marrow Transplant", "Thick Bone", "Fatal Mind",
        "Quick Dislocation", "Fracture Prevention", "Ancestral Fortitude",
    ]:
        itempool += [world.create_item(name) for _ in range(10)]

    # Dark Quartz upgrades (x2 each)
    for name in [
        "Nutrition Supply", "Heavy Frame", "Spirit Acceleration",
        "Exoskeleton Reinforcement", "Reassemble", "Ancient Alchemy",
    ]:
        itempool += [world.create_item(name) for _ in range(2)]

    # NPCs
    itempool += [world.create_item("Fox NPC"), world.create_item("Ogre NPC"),
                 world.create_item("Druid NPC"), world.create_item("Death Knight NPC")]

    number_of_items = len(itempool)
    number_of_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))
    needed_number_of_filler_items = number_of_unfilled_locations - number_of_items
    itempool += [world.create_filler() for _ in range(needed_number_of_filler_items)]
    world.multiworld.itempool += itempool