"""This module take care of everything npc related """


import json
import pprint
from random_table import RandomTable


class Npc(object):
    """NPC class for building the object representation"""

    APPEARANCE_PATH = "appearance"
    BONDS_PATH = "bonds"
    FLAWS_PATH = "flaws"
    HIGH_ABILITY_PATH = "high_ability"
    IDEALS_PATH = "ideals"
    INTERACTION_PATH = "interaction"
    LOW_ABILITY_PATH = "low_ability"
    MANNERISMS_PATH = "mannerisms"
    TALENT_PATH = "talent"
    
    FILE_EXTENSION = ".json"
    NPC_CONFIG_PATH = "../config/npc/"
    OUTPUT_PATH = "../output/npc/"

    def __init__(self, name):
        self.name = name
        self.appearance = ""
        self.bonds = ""
        self.flaws = ""
        self.high_ability = ""
        self.low_ability = ""
        self.ideals = ""
        self.mannerisms = ""
        self.talent = ""
        self.interaction = ""

    def build_random(self, overwrite=False, verbose=False):
        if verbose:
            print("Randomizing the NPC appearance")
        self.appearance = RandomTable.roll(self.build_config_path(propertie=self.APPEARANCE_PATH))
        if verbose:
            print("-> " + self.appearance)
            print("Randomizing the NPC bond")
        self.bonds = RandomTable.roll(self.build_config_path(propertie=self.BONDS_PATH))
        if verbose:
            print("-> " + self.bonds)
            print("Randomizing the NPC flaw")
        self.flaws = RandomTable.roll(self.build_config_path(propertie=self.FLAWS_PATH))
        if verbose:
            print("-> " + self.flaws)
            print("Randomizing what the NPC ideals")
        self.ideals = RandomTable.roll(self.build_config_path(propertie=self.IDEALS_PATH))
        if verbose:
            print("-> " + self.ideals)
            print("Randomizing the NPC mannerisms")
        self.mannerisms = RandomTable.roll(self.build_config_path(propertie=self.MANNERISMS_PATH))
        if verbose:
            print("-> " + self.mannerisms)
            print("Randomizing the NPC talent")
        self.talent = RandomTable.roll(self.build_config_path(propertie=self.TALENT_PATH))
        if verbose:
            print("-> " + self.talent)
            print("Randomizing the NPC interaction")
        self.interaction = RandomTable.roll(self.build_config_path(propertie=self.INTERACTION_PATH))
        if verbose:
            print("-> " + self.interaction)
            print("Randomizing the NPC high ability")
        self.high_ability = RandomTable.roll(self.build_config_path(propertie=self.HIGH_ABILITY_PATH))
        if verbose:
            print("-> " + self.high_ability)
            print("Randomizing the NPC low ability")
        self.low_ability = RandomTable.roll(self.build_config_path(propertie=self.LOW_ABILITY_PATH))
        if verbose:
            print("-> " + self.low_ability)
            print("Saving the NPC to file")

        save_path = self.OUTPUT_PATH + self.name + self.FILE_EXTENSION
        self.save_to_file(save_path, overwrite, verbose)

        if verbose:
            print("NPC saved under: " + save_path)

    def save_to_file(self, path, overwrite=False, verbose=False):
        if verbose:
            print("Building the NPC dictionary")

        npc = self.build_dictionary()

        if verbose:
            print("-> ")
            pprint.pprint(npc)
            print("Checking overwrite status")

        if overwrite:
            write_mode = "w"
            if verbose:
                print("-> Overwriting")
        else:
            write_mode = "x"
            if verbose:
                print("-> Not Overwriting")

        if verbose:
            print("Opening the file")

        with open(path, write_mode) as outfile:
            json.dump(npc, outfile, indent=4, separators=(',', ': '))

        if verbose:
            print("-> File saved")

    def build_dictionary(self):
        npc_dictionary = {
            "name": self.name,
            "appearabce": self.appearance,
            "bond": self.bonds,
            "flaw": self.flaws,
            "high ability": self.high_ability,
            "low ability": self.low_ability,
            "ideal": self.ideals,
            "mannerisms": self.mannerisms,
            "talent": self.talent,
            "interaction": self.interaction
        }

        return npc_dictionary

    def build_config_path(self, propertie):
        return self.NPC_CONFIG_PATH + propertie + self.FILE_EXTENSION

    @staticmethod
    def show_npc(name):
        path = Npc.OUTPUT_PATH + name + Npc.FILE_EXTENSION
        print(path)
        with open(path, 'r') as outfile:
            pprint.pprint(json.load(outfile))

