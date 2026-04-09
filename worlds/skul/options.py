from dataclasses import dataclass

from Options import Choice, DeathLink, OptionGroup, PerGameCommonOptions, Range, Toggle

class QuartzMult(Range):
    """
    Multiplier increase to the amount of dark quartz you get from all sources.
    """

    display_name = "Dark Quartz Multiplier"

    range_start = 1
    range_end = 4
    default = 1

class ReqRoomCount(Range):
    """
    How many rooms must be cleared per area.
    """

    display_name = "Required Room Count"

    range_start = 8
    range_end = 16
    default = 10

class ShrineChecks(Range):
    """
    How many shrine checks to generate per area. Set to 0 to disable shrine checks entirely.
    """

    display_name = "Shrine Check Count"

    range_start = 0
    range_end = 10
    default = 5

class EnableTraps(Toggle):
    """
    When enabled, trap items can be placed into the item pool.
    """

    display_name = "Enable Traps"
    default = 1

@dataclass
class SkulOptions(PerGameCommonOptions):
    quartz_mult: QuartzMult
    req_room_count: ReqRoomCount
    shrine_checks_count: ShrineChecks
    traps_enabled: EnableTraps
    death_link: DeathLink

option_groups = [
    OptionGroup(
        "Location Options",
        [ReqRoomCount, ShrineChecks],
    ),
    OptionGroup(
        "Quality of Life Options",
        [QuartzMult, EnableTraps],
    ),
]

option_presets: dict = {}
