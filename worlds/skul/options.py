from dataclasses import dataclass

from Options import Toggle, DeathLink, OptionGroup, PerGameCommonOptions, Range

class QuartzMult(Range):
    """
    Multiplier increase to the amount of dark quartz you get from all sources.
    """

    display_name = "Dark Quartz Multiplier"

    range_start = 1
    range_end = 8
    default = 3

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

class DeSkullTrapWeight(Range):
    """
    Percentage chance for a filler item to be a De-Skull Trap. Set to 0 to disable traps entirely.
    """

    display_name = "De-Skull Trap Weight"
    range_start = 0
    range_end = 100
    default = 20

class SkullRandomization(Toggle):
    """
    Randomize all skulls in the game, so that you must be sent each one.
    """
    display_name = "Killable Thieves"

class EnableDLC(Toggle):
    """
    Include DLC skulls (Viking, Slave, Officer, Ascetic, Unknown King) in the randomization pool.
    Requires owning the corresponding DLC.
    """
    display_name = "Enable DLC"

@dataclass
class SkulOptions(PerGameCommonOptions):
    quartz_mult: QuartzMult
    req_room_count: ReqRoomCount
    shrine_checks_count: ShrineChecks
    de_skull_trap_weight: DeSkullTrapWeight
    death_link: DeathLink
    skull_randomization: SkullRandomization
    enable_dlc: EnableDLC

option_groups = [
    OptionGroup(
        "Skull Randomization Options",
        [SkullRandomization, EnableDLC],
    ),
    OptionGroup(
        "Location Options",
        [ReqRoomCount, ShrineChecks],
    ),
    OptionGroup(
        "Quality of Life Options",
        [QuartzMult, DeSkullTrapWeight],
    ),
]

option_presets: dict = {}
