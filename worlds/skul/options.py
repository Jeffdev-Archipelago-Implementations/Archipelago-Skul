from dataclasses import dataclass

from Options import Choice, OptionGroup, PerGameCommonOptions, Range, Toggle

class MoneyIncrease(Range):
    """
    Multiplier increase to the amount of money you get from defeating enemies.
    """

    display_name = "Money Increase"

    range_start = 1
    range_end = 3
    default = 1

# class TrapChance(Range):
#     """
#     Percentage chance that any given Confetti Cannon will be replaced by a Math Trap.
#     """

#     display_name = "Trap Chance"

#     range_start = 0
#     range_end = 100
#     default = 0


# class StartWithOneConfettiCannon(Toggle):
#     """
#     Start with a confetti cannon already in your inventory.
#     Why? Because you deserve it. You get to celebrate yourself without doing any work first.
#     """

#     display_name = "Start With One Confetti Cannon"


# # A Range is a numeric option with a min and max value. This will be represented by a slider on the website.
# class ConfettiExplosiveness(Range):
#     """
#     How much confetti each use of a confetti cannon will fire.
#     """

#     display_name = "Confetti Explosiveness"

#     range_start = 0
#     range_end = 10

#     # Range options must define an explicit default value.
#     default = 3


# # A Choice is an option with multiple discrete choices. This will be represented by a dropdown on the website.
# class PlayerSprite(Choice):
#     """
#     The sprite that the player will have.
#     """

#     display_name = "Player Sprite"

#     option_human = 0
#     option_duck = 1
#     option_horse = 2
#     option_cat = 3

#     # Choice options must define an explicit default value.
#     default = option_human

#     # For choices, you can also define aliases.
#     # For example, we could make it so "player_sprite: kitty" resolves to "player_sprite: cat" like this:
#     alias_kitty = option_cat


# We must now define a dataclass inheriting from PerGameCommonOptions that we put all our options in.
# This is in the format "option_name_in_snake_case: OptionClassName".
@dataclass
class SkulOptions(PerGameCommonOptions):
    money_increase: MoneyIncrease


# If we want to group our options by similar type, we can do so as well. This looks nice on the website.
option_groups = [
    OptionGroup(
        "Quality of Life Options",
        [MoneyIncrease],
    ),
]

option_presets: dict = {}