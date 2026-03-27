from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Region

if TYPE_CHECKING:
    from .world import SkulWorld


def create_and_connect_regions(world: SkulWorld) -> None:
    create_all_regions(world)
    connect_regions(world)


def create_all_regions(world: SkulWorld) -> None:
    regions = [
        Region("Stronghold", world.player, world.multiworld),
        Region("Forest of Harmony", world.player, world.multiworld),
        Region("Grand Hall", world.player, world.multiworld),
        Region("The Black Lab", world.player, world.multiworld),
        Region("Fortress of Fate", world.player, world.multiworld),
        Region("Sacred Grounds", world.player, world.multiworld),
    ]
    world.multiworld.regions += regions


def connect_regions(world: SkulWorld) -> None:
    stronghold = world.get_region("Stronghold")
    forest = world.get_region("Forest of Harmony")
    grand_hall = world.get_region("Grand Hall")
    black_lab = world.get_region("The Black Lab")
    fortress = world.get_region("Fortress of Fate")
    sacred_grounds = world.get_region("Sacred Grounds")

    # Each stage area requires a certain number of Progressive Stage items.
    stronghold.connect(forest, "Stronghold to Forest of Harmony",
                       lambda state: state.has("Progressive Stage", world.player, 1))
    forest.connect(grand_hall, "Forest of Harmony to Grand Hall",
                   lambda state: state.has("Progressive Stage", world.player, 2))
    grand_hall.connect(black_lab, "Grand Hall to The Black Lab",
                       lambda state: state.has("Progressive Stage", world.player, 3))
    black_lab.connect(fortress, "The Black Lab to Fortress of Fate",
                      lambda state: state.has("Progressive Stage", world.player, 4))
    fortress.connect(sacred_grounds, "Fortress of Fate to Sacred Grounds",
                     lambda state: state.has("Progressive Stage", world.player, 5))
