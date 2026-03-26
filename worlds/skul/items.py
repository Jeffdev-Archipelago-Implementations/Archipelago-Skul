from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Item, ItemClassification

if TYPE_CHECKING:
    from .world import SkulWorld

# Every item must have a unique integer ID associated with it.
# We will have a lookup from item name to ID here that, in world.py, we will import and bind to the world class.
# Even if an item doesn't exist on specific options, it must be present in this lookup.
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

    # Filler
    "Bone x10": 30,
    "Dark Quartz x100": 31,
    "Gold x100": 32,
    "Castle Renovation": 33
}

# Items should have a defined default classification.
# In our case, we will make a dictionary from item name to classification.
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
    
    "Bone x10": ItemClassification.filler,
    "Dark Quartz x100": ItemClassification.filler,
    "Gold x200": ItemClassification.filler,
    
    "De-Skull Trap": ItemClassification.trap,
}


# Each Item instance must correctly report the "game" it belongs to.
# To make this simple, it is common practice to subclass the basic Item class and override the "game" field.
class SkulItem(Item):
    game = "Skul: The Hero Slayer"


# Ontop of our regular itempool, our world must be able to create arbitrary amounts of filler as requested by core.
# To do this, it must define a function called world.get_filler_item_name(), which we will define in world.py later.
# For now, let's make a function that returns the name of a random filler item here in items.py.
def get_random_filler_item_name(world: SkulWorld) -> str:
    
    rand_fill_pick = world.random.randint(0, 3)
    
    match rand_fill_pick:
        case 0:
            return "Bone x10"
        case 1:
            return "Dark Quartz x100"
        case 2:
            return "Gold x100"
        case 3:
            return "De-Skull Trap"


def create_item_with_correct_classification(world: SkulWorld, name: str) -> SkulItem:
    classification = DEFAULT_ITEM_CLASSIFICATIONS[name]

    return SkulItem(name, classification, ITEM_NAME_TO_ID[name], world.player)


# With those two helper functions defined, let's now get to actually creating and submitting our itempool.
def create_all_items(world: SkulWorld) -> None:
    # This is the function in which we will create all the items that this world submits to the multiworld item pool.
    # There must be exactly as many items as there are locations.
    # In our case, there are either six or seven locations.
    # We must make sure that when there are six locations, there are six items,
    # and when there are seven locations, there are seven items.

    # Creating items should generally be done via the world's create_item method.
    # First, we create a list containing all the items that always exist.

    itempool: list[Item] = [
        world.create_item("Progressive Stage"),
        world.create_item("Progressive Skull Tree"),
        world.create_item("Progressive Bone Tree"),
        world.create_item("Progressive Spirit Tree"),
        world.create_item("Marrow Transplant"),
        world.create_item("Thick Bone"),
        world.create_item("Fatal Mind"),
        world.create_item("Quick Dislocation"),
        world.create_item("Fracture Prevention"),
        world.create_item("Ancestral Fortitude"),
        world.create_item("Nutrition Supply"),
        world.create_item("Heavy Frame"),
        world.create_item("Spirit Acceleration"),
        world.create_item("Exoskeleton Reinforcement"),
        world.create_item("Reassemble"),
        world.create_item("Ancient Alchemy"),
        world.create_item("Fox NPC"),
        world.create_item("Ogre NPC"),
        world.create_item("Druid NPC")
    ]

    # Archipelago requires that each world submits as many locations as it submits items.
    # This is where we can use our filler and trap items.
    # APQuest has two of these: The Confetti Cannon and the Math Trap.
    # (Unfortunately, Archipelago is a bit ambiguous about its terminology here:
    #  "filler" is an ItemClassification separate from "trap", but in a lot of its functions,
    #  Archipelago will use "filler" to just mean "an additional item created to fill out the itempool".
    #  "Filler" in this sense can technically have any ItemClassification,
    #  but most commonly ItemClassification.filler or ItemClassification.trap.
    #  Starting here, the word "filler" will be used to collectively refer to APQuest's Confetti Cannon and Math Trap,
    #  which are ItemClassification.filler and ItemClassification.trap respectively.)
    # Creating filler items works the same as any other item. But there is a question:
    # How many filler items do we actually need to create?
    # In regions.py, we created either six or seven locations depending on the "extra_starting_chest" option.
    # In this function, we have created five or six items depending on whether the "hammer" option is enabled.
    # We *could* have a really complicated if-else tree checking the options again, but there is a better way.
    # We can compare the size of our itempool so far to the number of locations in our world.

    # The length of our itempool is easy to determine, since we have it as a list.
    number_of_items = len(itempool)

    # The number of locations is also easy to determine, but we have to be careful.
    # Just calling len(world.get_locations()) would report an incorrect number, because of our *event locations*.
    # What we actually want is the number of *unfilled* locations. Luckily, there is a helper method for this:
    number_of_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))

    # Now, we just subtract the number of items from the number of locations to get the number of empty item slots.
    needed_number_of_filler_items = number_of_unfilled_locations - number_of_items

    # Finally, we create that many filler items and add them to the itempool.
    # To create our filler, we could just use world.create_item("Confetti Cannon").
    # But there is an alternative that works even better for most worlds, including APQuest.
    # As discussed above, our world must have a get_filler_item_name() function defined,
    # which must return the name of an infinitely repeatable filler item.
    # Defining this function enables the use of a helper function called world.create_filler().
    # You can just use this function directly to create as many filler items as you need to complete your itempool.
    itempool += [world.create_filler() for _ in range(needed_number_of_filler_items)]

    # But... is that the right option for your game? Let's explore that.
    # For some games, the concepts of "regular itempool filler" and "additionally created filler" are different.
    # These games might want / require specific amounts of specific filler items in their regular pool.
    # To achieve this, they will have to intentionally create the correct quantities using world.create_item().
    # They may still use world.create_filler() to fill up the rest of their itempool with "repeatable filler",
    # after creating their "specific quantity" filler and still having room left over.

    # But there are many other games which *only* have infinitely repeatable filler items.
    # They don't care about specific amounts of specific filler items, instead only caring about the proportions.
    # In this case, world.create_filler() can just be used for the entire filler itempool.
    # APQuest is one of these games:
    # Regardless of whether it's filler for the regular itempool or additional filler for item links / etc.,
    # we always just want a Confetti Cannon or a Math Trap depending on the "trap_chance" option.
    # We defined this behavior in our get_random_filler_item_name() function, which in world.py,
    # we'll bind to world.get_filler_item_name(). So, we can just use world.create_filler() for all of our filler.

    # Anyway. With our world's itempool finalized, we now need to submit it to the multiworld itempool.
    # This is how the generator actually knows about the existence of our items.
    world.multiworld.itempool += itempool

    # Sometimes, you might want the player to start with certain items already in their inventory.
    # These items are called "precollected items".
    # They will be sent as soon as they connect for the first time (depending on your client's item handling flag).
    # Players can add precollected items themselves via the generic "start_inventory" option.
    # If you want to add your own precollected items, you can do so via world.push_precollected().