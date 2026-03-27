from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .world import SkulWorld


def set_all_rules(world: SkulWorld) -> None:
    set_all_location_rules(world)
    set_completion_condition(world)


def set_all_location_rules(world: SkulWorld) -> None:
    pass  # Region entrance rules (Progressive Stage) are set inline in regions.py.


def set_completion_condition(world: SkulWorld) -> None:
    world.multiworld.completion_condition[world.player] = lambda state: state.has("Victory", world.player)
