from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Location

from . import items

if TYPE_CHECKING:
    from .world import SkulWorld

# Every location must have a unique integer ID associated with it.
# We will have a lookup from location name to ID here that, in world.py, we will import and bind to the world class.
# Even if a location doesn't exist on specific options, it must be present in this lookup.

BASE_ID = 100

def _build_location_name_to_id() -> dict[str, int]:
    locs: dict[str, int] = {}
    next_id = BASE_ID

    # Dark Quartz upgrades purchasable up to 10 times each
    for name in [
        "Marrow Transplant", "Thick Bone", "Fatal Mind",
        "Quick Dislocation", "Fracture Prevention", "Ancestral Fortitude",
    ]:
        for i in range(1, 11):
            locs[f"{name} {i}"] = next_id
            next_id += 1

    # Dark Quartz upgrades purchasable up to 2 times each
    for name in [
        "Nutrition Supply", "Heavy Frame", "Spirit Acceleration",
        "Exoskeleton Reinforcement", "Reassemble", "Ancient Alchemy",
    ]:
        for i in range(1, 3):
            locs[f"{name} {i}"] = next_id
            next_id += 1

    # Room-cleared checks (10 rooms each across 3 areas)
    for area in ["Forest of Harmony", "Grand Hall", "The Black Lab"]:
        for room in range(1, 11):
            locs[f"{area} Room {room} Cleared"] = next_id
            next_id += 1

    # Shop item unlocks (8 per area)
    for area in ["Forest of Harmony", "Grand Hall", "The Black Lab"]:
        for i in range(1, 9):
            locs[f"{area} Shop Item {i}"] = next_id
            next_id += 1

    # Castle Repair (4 upgrades)
    for i in range(1, 5):
        locs[f"Castle Repair {i}"] = next_id
        next_id += 1

    # Fortress of Fate (4 rooms, 8 shop items)
    for room in range(1, 5):
        locs[f"Fortress of Fate Room {room} Cleared"] = next_id
        next_id += 1
    for i in range(1, 9):
        locs[f"Fortress of Fate Shop Item {i}"] = next_id
        next_id += 1

    # Mini boss and boss defeats for stage areas
    for area in ["Forest of Harmony", "Grand Hall", "The Black Lab"]:
        locs[f"{area} Mini Boss Defeated"] = next_id
        next_id += 1
        locs[f"{area} Boss Defeated"] = next_id
        next_id += 1

    # Fortress of Fate boss defeat
    locs["Fortress of Fate Boss Defeated"] = next_id
    next_id += 1

    # Freed NPC locations
    locs["Fox NPC Freed"] = next_id
    next_id += 1
    locs["Ogre NPC Freed"] = next_id
    next_id += 1
    locs["Druid NPC Freed"] = next_id
    next_id += 1
    locs["Knight NPC Freed"] = next_id
    next_id += 1

    return locs


LOCATION_NAME_TO_ID = _build_location_name_to_id()


# Each Location instance must correctly report the "game" it belongs to.
# To make this simple, it is common practice to subclass the basic Location class and override the "game" field.
class SkulLocation(Location):
    game = "Skul: The Hero Slayer"


# Let's make one more helper method before we begin actually creating locations.
# Later on in the code, we'll want specific subsections of LOCATION_NAME_TO_ID.
# To reduce the chance of copy-paste errors writing something like {"Chest": LOCATION_NAME_TO_ID["Chest"]},
# let's make a helper method that takes a list of location names and returns them as a dict with their IDs.
# Note: There is a minor typing quirk here. Some functions want location addresses to be an "int | None",
# so while our function here only ever returns dict[str, int], we annotate it as dict[str, int | None].
def get_location_names_with_ids(location_names: list[str]) -> dict[str, int | None]:
    return {location_name: LOCATION_NAME_TO_ID[location_name] for location_name in location_names}


def create_all_locations(world: SkulWorld) -> None:
    create_regular_locations(world)
    create_events(world)


def create_regular_locations(world: SkulWorld) -> None:
    stronghold = world.get_region("Stronghold")
    forest = world.get_region("Forest of Harmony")
    grand_hall = world.get_region("Grand Hall")
    black_lab = world.get_region("The Black Lab")
    fortress = world.get_region("Fortress of Fate")

    # Stronghold: bone upgrades and castle repair
    stronghold_locs: list[str] = []
    for name in [
        "Marrow Transplant", "Thick Bone", "Fatal Mind",
        "Quick Dislocation", "Fracture Prevention", "Ancestral Fortitude",
    ]:
        stronghold_locs += [f"{name} {i}" for i in range(1, 11)]
    for name in [
        "Nutrition Supply", "Heavy Frame", "Spirit Acceleration",
        "Exoskeleton Reinforcement", "Reassemble", "Ancient Alchemy",
    ]:
        stronghold_locs += [f"{name} {i}" for i in range(1, 3)]
    stronghold_locs += [f"Castle Repair {i}" for i in range(1, 5)]
    stronghold.add_locations(get_location_names_with_ids(stronghold_locs), SkulLocation)

    # Stage areas: room-cleared checks, shop item unlocks, mini boss + boss defeats
    for area, region in [
        ("Forest of Harmony", forest),
        ("Grand Hall", grand_hall),
        ("The Black Lab", black_lab),
    ]:
        area_locs = {f"{area} Room {i} Cleared": LOCATION_NAME_TO_ID[f"{area} Room {i} Cleared"]
                     for i in range(1, 11)}
        area_locs |= {f"{area} Shop Item {i}": LOCATION_NAME_TO_ID[f"{area} Shop Item {i}"]
                      for i in range(1, 9)}
        area_locs[f"{area} Mini Boss Defeated"] = LOCATION_NAME_TO_ID[f"{area} Mini Boss Defeated"]
        area_locs[f"{area} Boss Defeated"] = LOCATION_NAME_TO_ID[f"{area} Boss Defeated"]
        region.add_locations(area_locs, SkulLocation)

    # Fortress of Fate: rooms, shop, boss defeat
    fortress_locs = {f"Fortress of Fate Room {i} Cleared": LOCATION_NAME_TO_ID[f"Fortress of Fate Room {i} Cleared"]
                     for i in range(1, 5)}
    fortress_locs |= {f"Fortress of Fate Shop Item {i}": LOCATION_NAME_TO_ID[f"Fortress of Fate Shop Item {i}"]
                      for i in range(1, 9)}
    fortress_locs["Fortress of Fate Boss Defeated"] = LOCATION_NAME_TO_ID["Fortress of Fate Boss Defeated"]
    fortress.add_locations(fortress_locs, SkulLocation)

    # Freed NPC locations
    forest.add_locations(get_location_names_with_ids(["Fox NPC Freed"]), SkulLocation)
    grand_hall.add_locations(get_location_names_with_ids(["Ogre NPC Freed"]), SkulLocation)
    black_lab.add_locations(get_location_names_with_ids(["Druid NPC Freed"]), SkulLocation)
    fortress.add_locations(get_location_names_with_ids(["Knight NPC Freed"]), SkulLocation)


def create_events(world: SkulWorld) -> None:
    sacred_grounds = world.get_region("Sacred Grounds")
    sacred_grounds.add_event(
        "Final Boss Defeated", "Victory", location_type=SkulLocation, item_type=items.SkulItem
    )
