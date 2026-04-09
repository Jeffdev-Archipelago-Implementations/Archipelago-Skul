from __future__ import annotations

from typing import TYPE_CHECKING

from rule_builder.rules import Has

if TYPE_CHECKING:
    from .world import SkulWorld


def set_all_rules(world: SkulWorld) -> None:
    set_all_location_rules(world)
    set_completion_condition(world)


def set_all_location_rules(world: SkulWorld) -> None:
    # Castle Repair checks require the Death Knight NPC to be unlocked.
    for i in range(1, 5):
        world.set_rule(
            world.multiworld.get_location(f"Castle Repair {i}", world.player),
            Has("Death Knight NPC"),
        )


def set_completion_condition(world: SkulWorld) -> None:
    world.set_completion_rule(Has("Victory"))
